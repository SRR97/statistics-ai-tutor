from pypdf import PdfReader
from pathlib import Path

pdf_path = "data/Clase_2_Análisis_de_regresión.pdf"

def load_pdf(pdf_path):

    reader = PdfReader(pdf_path)
    document_name = Path(pdf_path).name

    pages = []

    print(f"Número de páginas: {len(reader.pages)}")

    for page_number, page in enumerate(reader.pages, start=1):
        page_text = page.extract_text()

        page_data = {
            "document": document_name,
            "page_number": page_number,
            "text": page_text
        }

        pages.append(page_data)

    print(f"Páginas almacenadas: {len(pages)}")

    return pages

def load_pdfs_from_directory(directory_path):
    directory = Path(directory_path)
    pdf_files = sorted(directory.glob("*.pdf"))
    all_pages = []

    for pdf_file in pdf_files:
        document_pages = load_pdf(pdf_file)
        all_pages.extend(document_pages)

    return all_pages


if __name__ == "__main__":
    document_pages = load_pdf(pdf_path) 

    print(document_pages[1]["document"])
