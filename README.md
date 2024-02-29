# NameLink Extractor

## Overview
NameLink Extractor is a desktop GUI application that allows users to input a list of names from a text file or extract them from an image using OCR. The application then searches a specified PDF for these names and extracts any associated hyperlinks.

## Features
- Upload or input a list of names through a text file.
- Upload an image to perform OCR and extract names.
- Upload a PDF document to search for names.
- Extract hyperlinks associated with the found names in the PDF.
- Display results with the option to save to a file.
- Logging of operations and errors for troubleshooting.

## Requirements
- Python 3.x
- Tkinter, PyQt, or another Python GUI framework
- pytesseract for OCR
- PyPDF2, pdfminer.six, or PyMuPDF for PDF parsing

## Installation

To set up the application, follow these steps:

1. Ensure you have Python 3.x installed on your system.
2. Clone the repository or download the source code.
3. Navigate to the application directory.
4. Install the required dependencies by running:
   ```
   pip install -r requirements.txt
   ```
5. Run the application:
   ```
   python main.py
   ```

## Usage

1. Start the application using the instructions above.
2. Use the menu to open a text file with names, an image file for OCR, or a PDF file.
3. Click the 'Process' button to start the operation.
4. View the results in the text area provided.
5. Use the 'Save' option to save the results to a file.

## File Operations

- **Open Text File**: Select a text file containing a list of names.
- **Open Image File**: Select an image file for OCR processing.
- **Open PDF**: Select a PDF file to search for names and hyperlinks.
- **Exit**: Close the application.

## Error Handling

The application includes robust error handling. If an error occurs, a message box will display the error details.

## Logging

Operations and errors are logged for troubleshooting purposes. Check the log files for more information if you encounter any issues.

## Contributing

Contributions to the application are welcome. Please follow the coding standards and write unit tests for any new functionality.

## License

This project is licensed under the MIT License - see the LICENSE file for details.