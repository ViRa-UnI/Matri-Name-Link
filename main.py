```python
import tkinter as tk
from tkinter import filedialog, messagebox
from gui import setup_gui
from pdf_processor import search_pdf, extract_hyperlinks
from ocr import perform_ocr
from input_validator import validate_input_file
from logger import log_operation, log_error

# Constants
FILE_TYPES = [('Text Files', '*.txt'), ('All Files', '*.*')]
OCR_SUPPORTED_IMAGE_FORMATS = [('Image Files', '*.png;*.jpg;*.jpeg;*.bmp;*.tiff;*.tif'), ('All Files', '*.*')]
PDF_SUPPORTED_FORMAT = [('PDF Files', '*.pdf'), ('All Files', '*.*')]

# Main application class
class MainApplication:
    def __init__(self, root):
        self.root = root
        setup_gui(self.root, self)

    def upload_text_file(self):
        file_path = filedialog.askopenfilename(filetypes=FILE_TYPES)
        if validate_input_file(file_path, 'text'):
            self.text_file_path_entry.delete(0, tk.END)
            self.text_file_path_entry.insert(0, file_path)
            log_operation(f"Text file uploaded: {file_path}")
        else:
            show_error_dialog(ERROR_MSG_INVALID_FILE)

    def upload_image_file(self):
        file_path = filedialog.askopenfilename(filetypes=OCR_SUPPORTED_IMAGE_FORMATS)
        if validate_input_file(file_path, 'image'):
            self.image_file_path_entry.delete(0, tk.END)
            self.image_file_path_entry.insert(0, file_path)
            log_operation(f"Image file uploaded: {file_path}")
        else:
            show_error_dialog(ERROR_MSG_INVALID_FILE)

    def upload_pdf_file(self):
        file_path = filedialog.askopenfilename(filetypes=PDF_SUPPORTED_FORMAT)
        if validate_input_file(file_path, 'pdf'):
            self.pdf_file_path_entry.delete(0, tk.END)
            self.pdf_file_path_entry.insert(0, file_path)
            log_operation(f"PDF file uploaded: {file_path}")
        else:
            show_error_dialog(ERROR_MSG_INVALID_FILE)

    def process_files(self):
        try:
            names = []
            text_file_path = self.text_file_path_entry.get()
            image_file_path = self.image_file_path_entry.get()
            pdf_file_path = self.pdf_file_path_entry.get()

            if text_file_path:
                with open(text_file_path, 'r') as file:
                    names.extend(file.read().splitlines())

            if image_file_path:
                names.extend(perform_ocr(image_file_path))

            if not names:
                show_error_dialog("No names to process. Please upload a text file or an image.")
                return

            if not pdf_file_path:
                show_error_dialog("Please upload a PDF file to search.")
                return

            found_names, not_found_names, hyperlinks = search_pdf(pdf_file_path, names)
            extract_hyperlinks(pdf_file_path, found_names)

            self.display_results(found_names, not_found_names, hyperlinks)
            update_status(INFO_MSG_PROCESSING_COMPLETE)
        except Exception as e:
            log_error(str(e))
            show_error_dialog(ERROR_MSG_PDF_PROCESSING_FAILED)

    def display_results(self, found_names, not_found_names, hyperlinks):
        self.results_text_area.delete(1.0, tk.END)
        self.results_text_area.insert(tk.END, f"Total names provided: {len(found_names) + len(not_found_names)}\n")
        self.results_text_area.insert(tk.END, f"Names found in PDF: {len(found_names)}\n")
        self.results_text_area.insert(tk.END, f"Names not found: {len(not_found_names)}\n\n")
        for name, hyperlink in hyperlinks.items():
            self.results_text_area.insert(tk.END, f"{name}: {hyperlink}\n")

    def save_results(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            with open(file_path, 'w') as file:
                file.write(self.results_text_area.get(1.0, tk.END))
            log_operation(f"Results saved to {file_path}")

    def update_status(self, message):
        self.status_bar.config(text=message)

    def show_error_dialog(self, message):
        messagebox.showerror("Error", message)

    def show_info_dialog(self, message):
        messagebox.showinfo("Information", message)

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = MainApplication(root)
    root.mainloop()
```