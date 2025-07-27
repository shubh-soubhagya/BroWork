import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path):
    text = ""
    with fitz.open(pdf_path) as doc:
        for page_num, page in enumerate(doc, start=1):
            page_text = page.get_text()
            text += f"\n--- Page {page_num} ---\n{page_text}"

    return text  # return the variable directly


