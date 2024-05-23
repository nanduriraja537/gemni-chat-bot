python -m pip install --upgrade pip
pip install -r requirements.txt
pip install google-generative-ai
# Use the PORT environment variable, default to 8000 if not set
PORT=${PORT:-8000}

streamlit run gemni-read-dataset.py --server.port $PORT --server.enableCORS false