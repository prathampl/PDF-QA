import fitz  # PyMuPDF

def extract_text(pdf_path: str) -> str:
    """
    Extracts text from a PDF file using PyMuPDF.

    :param pdf_path: Path to the PDF file.
    :return: Extracted text content.
    """
    try:
        doc = fitz.open(pdf_path)
        text = ""
        for page in doc:
            text += page.get_text()
        return text
    except Exception as e:
        print(f"Error processing PDF: {e}")
        return ""
