.PHONY: ingest ingest-logs ingest-db

ingest:
	./scripts/run_ingestion.sh

ingest-logs:
	./scripts/run_ingestion.sh --include-logs

ingest-db:
	./scripts/run_ingestion.sh --include-db
