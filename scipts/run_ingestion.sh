#!/bin/bash

# Parse options
INCLUDE_LOGS=0
INCLUDE_DB=0

for arg in "$@"
do
  case $arg in
    --include-logs)
      INCLUDE_LOGS=1
      shift
      ;;
    --include-db)
      INCLUDE_DB=1
      shift
      ;;
  esac
done

echo "Starting ingestion script..."
python3 scripts/ingest_all.py \
  $( [ $INCLUDE_LOGS -eq 1 ] && echo '--include-logs' ) \
  $( [ $INCLUDE_DB -eq 1 ] && echo '--include-db' )


