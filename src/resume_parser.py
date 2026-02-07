import PyPDF2
from docx import Document


def extract_text(file_path):
    # Convert to lowercase to avoid extension issues
    file_path = file_path.lower()

    if file_path.endswith(".pdf"):
        text = ""
        with open(file_path, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                if page.extract_text():
                    text += page.extract_text()
        return text

    elif file_path.endswith(".docx"):
        doc = Document(file_path)
        return "\n".join([para.text for para in doc.paragraphs])

    else:
        raise ValueError("Unsupported file format")