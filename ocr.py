```python
import pytesseract
from PIL import Image
from logger import log_operation, log_error
from input_validator import validate_input_file, OCR_SUPPORTED_IMAGE_FORMATS

# Define the OCRResult schema
class OCRResult:
    def __init__(self, success, extracted_text, error_message=None):
        self.success = success
        self.extracted_text = extracted_text
        self.error_message = error_message

def perform_ocr(image_path):
    """
    Perform OCR on the provided image and extract text.
    
    :param image_path: Path to the image file.
    :return: OCRResult object containing the success status, extracted text, and error message if any.
    """
    try:
        # Validate the image file
        if not validate_input_file(image_path, OCR_SUPPORTED_IMAGE_FORMATS):
            error_msg = f"Unsupported image format. Supported formats are: {OCR_SUPPORTED_IMAGE_FORMATS}"
            log_error(error_msg)
            return OCRResult(False, None, error_msg)
        
        # Open the image file
        with Image.open(image_path) as img:
            # Use pytesseract to do OCR on the image
            extracted_text = pytesseract.image_to_string(img)
            
            # Log the operation
            log_operation(f"OCR performed successfully on {image_path}")
            
            # Return the extracted text
            return OCRResult(True, extracted_text)
    
    except Exception as e:
        # Log the error
        error_msg = f"OCR failed on {image_path}: {str(e)}"
        log_error(error_msg)
        return OCRResult(False, None, error_msg)
```