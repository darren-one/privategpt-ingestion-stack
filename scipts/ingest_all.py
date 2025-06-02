#!/usr/bin/env python3

import os
import sys
import argparse
import logging

EXCLUDE_EXTENSIONS = {
    '.DS_Store', 'Thumbs.db', 'desktop.ini', '.tmp', '.part', '.crdownload',
    '.bak', '.swp', '.lock', '.log', '.sqlite', '.db'
}

def should_exclude(filename, include_logs=False, include_db=False):
    ext = os.path.splitext(filename)[1].lower()
    if ext in EXCLUDE_EXTENSIONS:
        if ext in ['.log'] and include_logs:
            return False
        if ext in ['.sqlite', '.db'] and include_db:
            return False
        return True
    return False

def ingest_file(filepath):
    print(f"Ingesting {filepath}")
    # Here you would implement actual ingestion logic calling PrivateGPT ingestion API or CLI

def recursive_ingest(base_dir, include_logs=False, include_db=False):
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if not should_exclude(file, include_logs, include_db):
                full_path = os.path.join(root, file)
                ingest_file(full_path)

def main():
    parser = argparse.ArgumentParser(description='Global ingestion script')
    parser.add_argument('--include-logs', action='store_true', help='Include log files')
    parser.add_argument('--include-db', action='store_true', help='Include database files')

    args = parser.parse_args()

    # Example base directories to ingest from
    base_dirs = [
        './notes_ingest',
        './archivebox_data',
        './email_exports',
        './obsidian',
        './financial_data',
        './calendar'
    ]

    for base_dir in base_dirs:
        if os.path.exists(base_dir):
            recursive_ingest(base_dir, args.include_logs, args.include_db)
        else:
            print(f"Warning: Base directory {base_dir} does not exist, skipping.")

if __name__ == "__main__":
    main()
