#!/usr/bin/env python3
"""Local server for Kid Games, with a Claude bridge.

    python3 serve.py            # then open http://localhost:8765/

Serves the repo like `python3 -m http.server`, plus one extra endpoint:

    POST /api/claude   {"system": str, "message": str, "model": "haiku"|"sonnet", "read": bool,
                        "session_id": str|null}

It runs one turn through the local `claude` CLI (your Claude Code login, no API
key) and streams the CLI's stream-json output back as NDJSON, one event per
line. The game supplies its own system prompt, so this server knows nothing
about any one game. `read: true` lets Claude Read/Grep files inside the game's
folder (the folder named by the request's Referer), nothing else; otherwise it
gets no tools at all. Pass back the session_id from the last turn's events to
continue the same conversation (one thread, any model); leave it out to start
a new one. The system prompt is sent fresh on every turn, so each model in the
thread gets its own instructions.

    GET /api/claude/ping  -> {"ok": true}   (games use it to show their Claude panel)

The hosted copy on GitHub Pages has no /api/claude, so the panel never shows
there. Binds 127.0.0.1 only, and refuses requests from other web origins.
"""
import http.server
import json
import os
import shutil
import signal
import subprocess
import sys
import threading
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent
PORT = int(os.environ.get("PORT", "8765"))
MODELS = {"haiku", "sonnet", "opus"}


def find_claude_bin():
    """PATH first, then the usual install spots (PATH is minimal under launchd)."""
    p = shutil.which("claude")
    if p:
        return p
    for cand in (Path.home() / ".claude" / "local" / "claude",
                 Path("/opt/homebrew/bin/claude"),
                 Path("/usr/local/bin/claude")):
        if cand.exists():
            return str(cand)
    return None


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *a, **kw):
        super().__init__(*a, directory=str(ROOT), **kw)

    def log_message(self, fmt, *args):
        if "/api/" in (self.path or ""):
            sys.stderr.write("%s %s\n" % (self.log_date_time_string(), fmt % args))

    def end_headers(self):
        self.send_header("Cache-Control", "no-cache")
        super().end_headers()

    def _same_origin(self):
        """Only pages served by this server may talk to Claude."""
        origin = self.headers.get("Origin")
        if not origin:
            return True
        o = urlparse(origin)
        return o.hostname in ("localhost", "127.0.0.1") and (o.port or 80) == PORT

    def _json(self, code, obj):
        body = json.dumps(obj).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        if self.path.startswith("/api/claude/ping"):
            self._json(200, {"ok": bool(find_claude_bin())})
            return
        super().do_GET()

    def do_POST(self):
        if self.path != "/api/claude":
            self.send_error(404)
            return
        if not self._same_origin():
            self.send_error(403, "only from pages on this server")
            return
        try:
            n = int(self.headers.get("Content-Length") or 0)
            payload = json.loads(self.rfile.read(n) or b"{}")
        except ValueError:
            self.send_error(400, "invalid JSON")
            return
        message = (payload.get("message") or "").strip()
        system = (payload.get("system") or "").strip()
        model = payload.get("model") or "haiku"
        if not message or model not in MODELS:
            self.send_error(400, "need message, and model in " + ", ".join(sorted(MODELS)))
            return
        claude = find_claude_bin()
        if not claude:
            self.send_error(500, "claude CLI not found - install Claude Code first")
            return

        # Run inside the calling game's folder, so `read` can only see that game.
        cwd = ROOT
        ref = urlparse(self.headers.get("Referer") or "").path.strip("/").split("/")
        if ref and ref[0] and (ROOT / ref[0]).is_dir() and not ref[0].startswith("."):
            cwd = ROOT / ref[0]

        cmd = [claude, "-p",
               "--output-format", "stream-json", "--verbose", "--include-partial-messages",
               "--model", model,
               "--strict-mcp-config",            # none of your MCP servers: faster start, nothing to reach
               "--setting-sources", "",          # no hooks, no CLAUDE.md, no memory
               "--system-prompt-snapshot", "off"]   # each turn's own system prompt, even on resume
        session_id = (payload.get("session_id") or "").strip()
        if session_id:
            if not all(c.isalnum() or c == "-" for c in session_id):
                self.send_error(400, "bad session_id")
                return
            cmd += ["--resume", session_id]
        if system:
            cmd += ["--system-prompt", system]
        if payload.get("read"):
            cmd += ["--tools", "Read,Grep"]   # default permissions: reads inside cwd only
        else:
            cmd += ["--tools", ""]

        try:
            proc = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE, cwd=str(cwd), start_new_session=True)
        except OSError as e:
            self.send_error(500, "could not start claude: %s" % e)
            return
        errs = []
        t = threading.Thread(target=lambda: errs.append(proc.stderr.read()), daemon=True)
        t.start()

        def kill():
            if proc.poll() is None:
                try:
                    os.killpg(proc.pid, signal.SIGTERM)
                except (ProcessLookupError, PermissionError):
                    pass

        self.send_response(200)
        self.send_header("Content-Type", "application/x-ndjson; charset=utf-8")
        self.end_headers()
        try:
            proc.stdin.write(message.encode("utf-8"))
            proc.stdin.close()
            for line in proc.stdout:
                self.wfile.write(line)
                self.wfile.flush()
            rc = proc.wait()
            t.join(timeout=2)
            if rc != 0:
                err = b"".join(e for e in errs if e).decode("utf-8", "replace").strip()
                self.wfile.write(json.dumps({"type": "server_error",
                                             "error": err[-400:] or "claude exited with code %d" % rc}).encode() + b"\n")
                self.wfile.flush()
        except (BrokenPipeError, ConnectionResetError):
            pass
        finally:
            kill()


if __name__ == "__main__":
    srv = http.server.ThreadingHTTPServer(("127.0.0.1", PORT), Handler)
    print("Kid Games with Claude: http://localhost:%d/" % PORT)
    print("claude CLI: %s" % (find_claude_bin() or "NOT FOUND"))
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        pass
