# Smart Document Analyzer

AI-powered document analysis tool built with Pydantic AI and Streamlit.

## Features

- 📄 Upload PDF, image, or text files
- 🤖 AI-powered document analysis
- 📊 Structured insights and metrics
- 🎯 Action items and risk assessment
- 💻 Clean, modern web interface

## Local Setup

### Prerequisites
- Python 3.8+
- OpenAI API key
- Linux system with tesseract-ocr installed

### Installation

1. **Clone the repository:**
```bash
git clone https://github.com/yourusername/document-analyzer-mvp.git
cd document-analyzer-mvp
```

2. **Install tesseract (for OCR):**
```bash
sudo apt update
sudo apt install tesseract-ocr
```

3. **Create virtual environment:**
```bash
python3 -m venv venv
source venv/bin/activate
```

4. **Install dependencies:**
```bash
pip install -r requirements.txt
```

5. **Set up environment variables:**
```bash
cp .env.example .env
# Edit .env and add your OpenAI API key
```

6. **Run the application:**
```bash
streamlit run app.py
```

## Deployment on Streamlit Cloud (Free)

1. Push your code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub repository
4. Your app will be live at: `https://yourusername-document-analyzer-mvp.streamlit.app`

## Usage

1. Enter your OpenAI API key in the sidebar
2. Upload a document or paste text directly
3. Click "Analyze Document"
4. View AI-generated insights, metrics, and recommendations

## Project Structure

```
document-analyzer-mvp/
├── app.py                 # Main Streamlit app
├── models.py             # Pydantic models
├── agents.py             # AI agents
├── document_processor.py # File processing
├── requirements.txt      # Dependencies
└── README.md            # This file
```

## Technologies Used

- **Pydantic AI**: AI agent framework
- **Streamlit**: Web interface
- **OpenAI GPT-4**: Language model
- **PyPDF2**: PDF processing
- **Pytesseract**: OCR for images
