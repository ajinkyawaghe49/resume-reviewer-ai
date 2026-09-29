from pypdf import PdfReader
import io


def extract_text_from_pdf(contents):
    pdf = PdfReader(io.BytesIO(contents))

    text = ""

    for page in pdf.pages:
        text += page.extract_text() or ""

    pages = len(pdf.pages)

    return text, pages