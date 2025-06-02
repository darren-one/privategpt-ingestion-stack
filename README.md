# PrivateGPT Ingestion Stack

## Overview

This project provides a Docker Compose-based self-hosted AI ingestion environment built around **PrivateGPT** for personal knowledge management and AI-assisted workflows. It integrates with your local data sources and syncing tools to enable seamless ingestion, indexing, and querying of your documents, notes, emails, financial data, calendar, and web archives.

---

## Components

- **PrivateGPT** — Your self-hosted AI assistant, ingesting all your synced data for private AI interaction.
- **ChromaDB** — Vector database backend for storing document embeddings and enabling fast semantic search.
- **Syncthing** — Peer-to-peer continuous file synchronization tool used to securely sync your files from your devices (e.g., Mac running Apple Notes exports) to the ingestion server.
- **Global ingestion script** — A Python script that scans synced folders, excludes unwanted files, and ingests your content into PrivateGPT.
- **Wrapper scripts and automation** — Shell scripts, Makefile commands, and cron job examples to automate ingestion runs on flexible schedules.

---

## Supported Data Sources

| Data Source          | Description                                  | Sync Method             | Ingestion Frequency    |
|----------------------|----------------------------------------------|-------------------------|-----------------------|
| Apple Notes (export) | Daily note-taking app, exported every 5 min  | Syncthing from macOS    | Every 5 minutes (recommended) |
| ArchiveBox           | Web page archiving tool, manual or auto archive | Syncthing sync          | Every 30 minutes       |
| Obsidian             | Markdown-based personal knowledge base       | Syncthing sync          | Manual or scheduled    |
| Email Exports        | Exported emails (e.g., via IMAP/Export tool) | Syncthing sync          | Scheduled (e.g., hourly) |
| Financial Data       | Quicken, Quickbooks, or bank CSV exports     | Syncthing sync          | Manual or scheduled    |
| Calendar             | Apple Calendar exports or other ICS files    | Syncthing sync          | Scheduled              |

---

## File Exclusion Rules

By default, the ingestion script excludes common system and temporary files such as:

- `.DS_Store`, `Thumbs.db`, `desktop.ini`
- Temporary and partial download files like `.tmp`, `.part`, `.crdownload`
- Backup and lock files like `.bak`, `.swp`, `.lock`
- Logs (`.log`) and databases (`.sqlite`, `.db`) are excluded unless explicitly included with flags.

This prevents unnecessary or redundant data from being ingested.

---

## Getting Started

### Prerequisites

- A Debian-based or similar Linux system with Docker and Docker Compose installed.
- Syncthing client installed on your macOS or other devices to sync files securely.
- Export mechanisms set up on Apple Notes, ArchiveBox, etc. to place files into Syncthing-shared folders.

### Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/yourusername/privategpt-ingestion-stack.git
   cd privategpt-ingestion-stack
