import tkinter as tk
from tkinter import filedialog, messagebox
from ocr import perform_ocr
from pdf_processor import search_pdf, extract_hyperlinks
from input_validator import validate_input_file
from logger import log_operation, log_error

FILE_TYPES = [('Text Files', '*.txt'), ('All Files', '*.*')]
OCR_SUPPORTED_IMAGE_FORMATS = [('Image Files', '*.png;*.jpg;*.jpeg;*.bmp;*.tiff;*.tif'), ('All Files', '*.*')]
PDF_SUPPORTED_FORMAT = [('PDF Files', '*.pdf'), ('All Files', '*.*')]

class MainApplication(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Name Search and Hyperlink Extraction')
        self.create_widgets()
        self.setup_layout()

    def create_widgets(self):
        # Menu
        self.menu_bar = tk.Menu(self)
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label='Open Text File', command=self.upload_text_file)
        self.file_menu.add_command(label='Open Image File', command=self.upload_image_file)
        self.file_menu.add_command(label='Open PDF', command=self.upload_pdf_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label='Exit', command=self.quit)
        self.menu_bar.add_cascade(label='File', menu=self.file_menu)
        self.config(menu=self.menu_bar)

        # File path entries and browse buttons
        self.text_file_path_entry = tk.Entry(self)
        self.image_file_path_entry = tk.Entry(self)
        self.pdf_file_path_entry = tk.Entry(self)
        self.text_file_browse_button = tk.Button(self, text='Browse...', command=lambda: self.browse_file(self.text_file_path_entry, FILE_TYPES))
        self.image_file_browse_button = tk.Button(self, text='Browse...', command=lambda: self.browse_file(self.image_file_path_entry, OCR_SUPPORTED_IMAGE_FORMATS))
        self.pdf_file_browse_button = tk.Button(self, text='Browse...', command=lambda: self.browse_file(self.pdf_file_path_entry, PDF_SUPPORTED_FORMAT))

        # Process button
        self.process_button = tk.Button(self, text='Process', command=self.process_files)

        # Results text area
        self.results_text_area = tk.Text(self, height=15, width=50)

        # Status bar
        self.status_bar = tk.Label(self, text='Ready', bd=1, relief=tk.SUNKEN, anchor=tk.W)

    def setup_layout(self):
        # Layout configuration
        self.text_file_path_entry.grid(row=0, column=0, padx=5, pady=5, sticky='ew')
        self.text_file_browse_button.grid(row=0, column=1, padx=5, pady=5)
        self.image_file_path_entry.grid(row=1, column=0, padx=5, pady=5, sticky='ew')
        self.image_file_browse_button.grid(row=1, column=1, padx=5, pady=5)
        self.pdf_file_path_entry.grid(row=2, column=0, padx=5, pady=5, sticky='ew')
        self.pdf_file_browse_button.grid(row=2, column=1, padx=5, pady=5)
        self.process_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)
        self.results_text_area.grid(row=4, column=0, columnspan=2, padx=5, pady=5)
        self.status_bar.grid(row=5, column=0, columnspan=2, sticky='ew')

        self.grid_columnconfigure(0, weight=1)

    def browse_file(self, entry_widget, file_types):
        file_path = filedialog.askopenfilename(filetypes=file_types)
        if file_path:
            entry_widget.delete(0, tk.END)
            entry_widget.insert(0, file_path)

    def upload_text_file(self):
        # Implementation for uploading text file
        pass

    def upload_image_file(self):
        # Implementation for uploading image file and performing OCR
        pass

    def upload_pdf_file(self):
        # Implementation for uploading PDF file
        pass

    def process_files(self):
        # Implementation for processing the files and extracting data
        pass

    def update_status(self, message):
        self.status_bar.config(text=message)

    def show_error_dialog(self, message):
        messagebox.showerror('Error', message)

    def show_info_dialog(self, message):
        messagebox.showinfo('Info', message)

if __name__ == '__main__':
    app = MainApplication()
    app.mainloop()