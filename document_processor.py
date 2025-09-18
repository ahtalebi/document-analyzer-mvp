import PyPDF2
from PIL import Image
import pytesseract
from typing import Optional

def extract_text_from_pdf(uploaded_file) -> str:
    """Extract text from PDF file"""
    try:
        pdf_reader = PyPDF2.PdfReader(uploaded_file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text() + "\n"
        return text.strip()
    except Exception as e:
        return f"Error reading PDF: {str(e)}"

def extract_text_from_image(uploaded_file) -> str:
    """Extract text from image using OCR"""
    try:
        image = Image.open(uploaded_file)
        text = pytesseract.image_to_string(image)
        return text.strip()
    except Exception as e:
        return f"Error reading image: {str(e)}"

def extract_text_from_txt(uploaded_file) -> str:
    """Extract text from text file"""
    try:
        return str(uploaded_file.read(), "utf-8")
    except Exception as e:
        return f"Error reading text file: {str(e)}"

def process_uploaded_file(uploaded_file) -> Optional[str]:
    """Process uploaded file and extract text"""
    if uploaded_file is None:
        return None
    
    file_type = uploaded_file.type
    
    if file_type == "application/pdf":
        return extract_text_from_pdf(uploaded_file)
    elif file_type.startswith('image/'):
        return extract_text_from_image(uploaded_file)
    elif file_type == "text/plain":
        return extract_text_from_txt(uploaded_file)
    else:
        return f"Unsupported file type: {file_type}"
