#!/bin/bash
# startup.sh
python -m pip install --upgrade pip
pip install -r requirements.txt
streamlit run gemni-read-dataset.py --server.port ${PORT:-8501} --server.enableCORS false
