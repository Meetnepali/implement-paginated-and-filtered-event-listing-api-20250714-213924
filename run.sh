#!/bin/bash
set -e
./install.sh
exec uvicorn app.main:app --host 0.0.0.0 --port 8000
