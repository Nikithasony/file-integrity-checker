#!/usr/bin/env python3
"""
File Integrity Checker
----------------------
A CLI tool to detect unauthorized changes in files using SHA-256 hashing.

Usage:
    python integrity_check.py init <file_or_directory>
    python integrity_check.py check <file_or_directory>
    python integrity_check.py update <file>
"""

import hashlib
import json
import sys
from pathlib import Path

HASH_FILE = "file_hashes.json"

def calculate_hash(file_path: Path) -> str:
    """Calculate SHA-256 hash for a file."""
    sha256 = hashlib.sha256()
    with file_path.open("rb") as f:
        while chunk := f.read(8192):
            sha256.update(chunk)
    return sha256.hexdigest()

def load_hashes() -> dict:
    """Load stored hashes from a JSON file."""
    if not Path(HASH_FILE).exists():
        return {}
    with open(HASH_FILE, "r") as f:
        return json.load(f)

def save_hashes(hashes: dict):
    """Save hashes to a JSON file."""
    with open(HASH_FILE, "w") as f:
        json.dump(hashes, f, indent=4)

def list_files(target: Path):
    """Get all files inside a directory or a single file."""
    if target.is_file():
        return [target]
    return [file for file in target.rglob("*") if file.is_file()]

def init_baseline(target: Path):
    """Initialize hashes for given files."""
    hashes = {}
    for file in list_files(target):
        hashes[str(file.resolve())] = calculate_hash(file)
    save_hashes(hashes)
    print("✅ Baseline hashes created successfully.")

def check_integrity(target: Path):
    """Check integrity of files against stored hashes."""
    stored_hashes = load_hashes()
    modified_files = []

    for file in list_files(target):
        abs_path = str(file.resolve())
        current_hash = calculate_hash(file)
        stored_hash = stored_hashes.get(abs_path)

        if stored_hash is None:
            print(f"🆕 New file detected: {abs_path}")
        elif stored_hash != current_hash:
            modified_files.append(abs_path)

    if modified_files:
        print("❌ Tampering detected in:")
        for f in modified_files:
            print(f"   - {f}")
    else:
        print("✅ All files are intact (no tampering).")

def update_hash(file: Path):
    """Update hash for a file after legitimate change."""
    if not file.is_file():
        print("⚠️ Error: Not a valid file.")
        return

    hashes = load_hashes()
    hashes[str(file.resolve())] = calculate_hash(file)
    save_hashes(hashes)
    print("✅ Hash updated successfully.")

def main():
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)

    cmd, target = sys.argv[1].lower(), Path(sys.argv[2])

    if cmd == "init":
        init_baseline(target)
    elif cmd == "check":
        check_integrity(target)
    elif cmd == "update":
        update_hash(target)
    else:
        print("⚠️ Invalid command. Use init, check, or update.")

if __name__ == "__main__":
    main()
