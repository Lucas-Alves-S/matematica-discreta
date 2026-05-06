import sys
import time
import subprocess
import platform
import webview
from pathlib import Path

from src.api import Api

UI_DIR = Path(__file__).parent / "ui"
DIST_DIR = UI_DIR / "dist"
DEV_URL = "http://localhost:5173"


def _wait_for_server(url: str, timeout: int = 10) -> bool:
    import urllib.request
    deadline = time.time() + timeout
    while time.time() < deadline:
        try:
            urllib.request.urlopen(url, timeout=1)
            return True
        except Exception:
            time.sleep(0.3)
    return False


def main():
    dev_mode = "--dev" in sys.argv or not DIST_DIR.exists()
    dev_proc = None

    if dev_mode:
        dev_proc = subprocess.Popen(
            ["pnpm", "dev"],
            cwd=UI_DIR,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        if not _wait_for_server(DEV_URL):
            print("Erro: servidor Vite não iniciou a tempo.", file=sys.stderr)
            dev_proc.terminate()
            sys.exit(1)
        url = DEV_URL
    else:
        url = str(DIST_DIR / "index.html")

    webview.create_window(
        title="Matematica Discreta",
        url=url,
        js_api=Api(),
        width=1024,
        height=768,
        min_size=(800, 600),
    )

    gui = "qt" if platform.system() == "Linux" else None

    try:
        webview.start(debug=dev_mode, gui=gui)
    finally:
        if dev_proc:
            dev_proc.terminate()


if __name__ == "__main__":
    main()
