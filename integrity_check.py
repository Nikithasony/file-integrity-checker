#!/usr/bin/env python3
import hashlib
import json
import sys
from pathlib import Path

HASH_FILE = "file_hashes.json"

def calculate_hash(file_path: Path) -> str:
    sha256 = hashlib.sha256()
    with file_path.open("rb") as f:
        while chunk := f.read(8192):
            sha256.update(chunk)
    return sha256.hexdigest()

def load_hashes() -> dict:
    if not Path(HASH_FILE).exists():
        return {}
    with open(HASH_FILE, "r") as f:
        return json.load(f)

def save_hashes(hashes: dict):
    with open(HASH_FILE, "w") as f:
        json.dump(hashes, f, indent=4)

def list_files(target: Path):
    if target.is_file():
        return [target]
    return [file for file in target.rglob("*") if file.is_file()]

def init_baseline(target: Path):
    hashes = {}
    for file in list_files(target):
        hashes[str(file.resolve())] = calculate_hash(file)
    save_hashes(hashes)
    print("Hashes stored successfully.")

def check_integrity(target: Path):
    stored_hashes = load_hashes()
    modified_files = []

    for file in list_files(target):
        abs_path = str(file.resolve())
        current_hash = calculate_hash(file)
        stored_hash = stored_hashes.get(abs_path)

        if stored_hash and stored_hash != current_hash:
            modified_files.append(abs_path)

    if modified_files:
        print("Status: Modified (Hash mismatch)")
        print("Tampered files:")
        for f in modified_files:
            print(f"   - {f}")
    else:
        print("Status: Unmodified")

def update_hash(file: Path):
    if not file.is_file():
        print("Error: File does not exist.")
        return

    hashes = load_hashes()
    hashes[str(file.resolve())] = calculate_hash(file)
    save_hashes(hashes)
    print("Hash updated successfully.")

def main():
    if len(sys.argv) < 3:
        print("Usage:")
        print("./integrity-check init <directory_or_file>")
        print("./integrity-check check <file_or_directory>")
        print("./integrity-check update <file>")
        sys.exit(1)

    cmd, target = sys.argv[1].lower(), Path(sys.argv[2])

    if cmd == "init":
        init_baseline(target)
    elif cmd == "check":
        check_integrity(target)
    elif cmd == "update":
        update_hash(target)
    else:
        print("Invalid command. Use init, check, or update.")

if __name__ == "__main__":
    main()

