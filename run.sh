#!/usr/bin/env bash
python -m uvicorn app_main:app --reload --host 0.0.0.0 --port 8000
