#!/bin/bash

# Install system dependencies for OCR
apt-get update
apt-get install -y tesseract-ocr tesseract-ocr-eng

# Start Streamlit app
streamlit run app.py --server.port $PORT --server.address 0.0.0.0 --server.headless true --server.enableCORS false
