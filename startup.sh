python -m pip install --upgrade pip
pip install -r requirements.txt

# Use the PORT environment variable, default to 8000 if not set
PORT=${PORT:-8000}

streamlit run app.py --server.port $PORT --server.enableCORS false