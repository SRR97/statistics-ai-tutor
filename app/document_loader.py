from pypdf import PdfReader

pdf_path = "data/Clase_2_Análisis_de_regresión.pdf"

def load_pdf(pdf_path):

    reader = PdfReader(pdf_path)

    pages = []

    print(f"Número de páginas: {len(reader.pages)}")

    for page_number, page in enumerate(reader.pages, start=1):
        page_text = page.extract_text()

        page_data = {
            "page_number": page_number,
            "text": page_text
        }

        pages.append(page_data)

    print(f"Páginas almacenadas: {len(pages)}")

    return pages

document_pages = load_pdf(pdf_path) 

print(document_pages[1]["page_number"])