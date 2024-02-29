```python
import fitz  # PyMuPDF
from logger import log_operation, log_error

class PDFProcessor:
    def __init__(self, pdf_path):
        self.pdf_path = pdf_path
        self.document = None

    def load_pdf(self):
        try:
            self.document = fitz.open(self.pdf_path)
            log_operation(f"PDF loaded: {self.pdf_path}")
        except Exception as e:
            log_error(f"Failed to load PDF: {e}")
            raise e

    def search_names(self, names):
        if not self.document:
            raise ValueError("PDF not loaded")

        results = []
        for page in self.document:
            text = page.get_text("text")
            for name in names:
                if name in text:
                    hyperlinks = self.extract_hyperlinks(page, name)
                    results.append({'name': name, 'hyperlinks': hyperlinks})
        return results

    def extract_hyperlinks(self, page, name):
        hyperlinks = []
        links = page.get_links()
        for link in links:
            if link['type'] == fitz.LINK_URI and name in link['uri']:
                hyperlinks.append(link['uri'])
        return hyperlinks

    def close_pdf(self):
        if self.document:
            self.document.close()
            log_operation("PDF closed")

def search_pdf(pdf_path, names):
    pdf_processor = PDFProcessor(pdf_path)
    try:
        pdf_processor.load_pdf()
        results = pdf_processor.search_names(names)
        pdf_processor.close_pdf()
        return results
    except Exception as e:
        log_error(f"Error processing PDF: {e}")
        return None
```