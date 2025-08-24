import os
import fitz  # PyMuPDF
import docx

def extract_text_from_pdf(path):
    text = ""
    try:
        doc = fitz.open(path)
        for page in doc:
            text += page.get_text()
    except Exception as e:
        print(f"Error reading PDF {path}: {e}")
    return text

def extract_text_from_docx(path):
    text = ""
    try:
        doc = docx.Document(path)
        for para in doc.paragraphs:
            text += para.text + "\n"
    except Exception as e:
        print(f"Error reading DOCX {path}: {e}")
    return text

def extract_text_from_files(file_paths):
    combined_text = ""
    for file_path in file_paths:
        if file_path.endswith(".pdf"):
            text = extract_text_from_pdf(file_path)
        elif file_path.endswith(".docx"):
            text = extract_text_from_docx(file_path)
        else:
            continue

        print(f"\n---[Preview: {os.path.basename(file_path)}]---")
        print(text[:500])  # Preview the first 500 characters of each file
        print(f"[Length: {len(text)} characters]\n")

        combined_text += text + "\n"
    return combined_text


