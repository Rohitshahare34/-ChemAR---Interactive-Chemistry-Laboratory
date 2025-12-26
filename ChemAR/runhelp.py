"""
ChemAR runhelp - One-file installer & launcher

Run this single file to install dependencies and start the app on any PC/laptop.

Usage:
  python runhelp.py    # Windows
  python3 runhelp.py   # macOS/Linux
"""

from __future__ import annotations

import os
import sys
import subprocess
import time
import webbrowser
from typing import List


def print_banner() -> None:
    print("=" * 62)
    print("  ChemAR - Interactive Chemistry Lab (runhelp)")
    print("=" * 62)


def ensure_python_version() -> None:
    major, minor = sys.version_info.major, sys.version_info.minor
    if not (major == 3 and 8 <= minor <= 12):
        print(f"[WARN] Detected Python {major}.{minor}. Recommended: 3.8–3.12.")
        print("       Continuing anyway...")


def run(cmd: List[str], cwd: str | None = None) -> int:
    print(f"[RUN] {' '.join(cmd)}")
    completed = subprocess.run(cmd, cwd=cwd)
    return completed.returncode


def upgrade_pip() -> None:
    print("\n[STEP] Upgrading pip ...")
    rc = run([sys.executable, "-m", "pip", "install", "--upgrade", "pip"])
    if rc != 0:
        print("[WARN] Failed to upgrade pip. Proceeding with existing version.")


def install_requirements() -> None:
    print("\n[STEP] Installing Python dependencies from requirements.txt ...")
    req_file = os.path.join(os.path.dirname(__file__), "requirements.txt")
    if not os.path.exists(req_file):
        print("[ERROR] requirements.txt not found. Please make sure you're in the project folder.")
        sys.exit(1)

    rc = run([sys.executable, "-m", "pip", "install", "-r", req_file])
    if rc != 0:
        print("[ERROR] Failed to install dependencies. Check your internet connection and try again.")
        sys.exit(rc)


def start_app() -> None:
    print("\n[STEP] Starting ChemAR server ...")
    url = "http://localhost:5000"
    try:
        # Open the browser shortly after the server starts
        def _open_later() -> None:
            time.sleep(1.2)
            try:
                webbrowser.open(url)
            except Exception:
                pass

        # Spawn a background thread to open the browser
        import threading

        opener = threading.Thread(target=_open_later, daemon=True)
        opener.start()

    except Exception:
        pass

    # Run app.py in the foreground
    app_path = os.path.join(os.path.dirname(__file__), "app.py")
    rc = run([sys.executable, app_path])
    if rc != 0:
        print("[ERROR] App exited with a non-zero status.")
        sys.exit(rc)


def main() -> None:
    print_banner()
    ensure_python_version()
    upgrade_pip()
    install_requirements()
    print("\n[OK] All dependencies are installed.")
    print("[INFO] Launching the application...\n")
    start_app()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[INFO] Interrupted by user.")
    except Exception as exc:
        print(f"\n[FATAL] {exc}")
        sys.exit(1)
