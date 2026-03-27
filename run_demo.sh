#!/usr/bin/env bash
set -e
mkdir -p sample_data
echo "id,name,qty" > sample_data/demo.csv
echo "1,shipment-A,10" >> sample_data/demo.csv
echo "2,shipment-B,5" >> sample_data/demo.csv

python -m uvicorn app_main:app --reload --host 0.0.0.0 --port 8000
