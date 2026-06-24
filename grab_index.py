#!/usr/bin/env python3
"""Grab the most recent downloaded index___.html file and save it here as index.html."""

import glob
import os
import shutil
import subprocess

DOWNLOADS = os.path.expanduser("~/Downloads")
DEST = os.path.join(os.getcwd(), "index.html")


def main():
    candidates = glob.glob(os.path.join(DOWNLOADS, "*index*.html"))
    if not candidates:
        raise SystemExit(f"No 'index*.html' files found in {DOWNLOADS}")

    newest = max(candidates, key=os.path.getmtime)

    if os.path.exists(DEST):
        answer = input(f"{DEST} already exists. Overwrite? [y/N] ").strip().lower()
        if answer not in ("y", "yes"):
            raise SystemExit("Aborted.")

    shutil.copy2(newest, DEST)
    print(f"Copied:\n  {newest}\n-> {DEST}")

    answer = input("Push index.html to GitHub? [y/N] ").strip().lower()
    if answer not in ("y", "yes"):
        print("Skipped push.")
        return

    subprocess.run(["git", "add", "index.html"], check=True)
    subprocess.run(["git", "commit", "-m", "Update index.html"], check=True)
    subprocess.run(["git", "push"], check=True)
    print("Pushed to GitHub.")


if __name__ == "__main__":
    main()
