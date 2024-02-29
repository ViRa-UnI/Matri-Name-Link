```python
import os
from tkinter import messagebox

# Shared dependencies
FILE_TYPES = {
    'text': ('.txt',),
    'image': ('.png', '.jpg', '.jpeg', '.bmp', '.tiff', '.tif'),
    'pdf': ('.pdf',)
}

ERROR_MSG_INVALID_FILE = "Invalid file type selected. Please select a valid {} file."

def validate_input_file(file_path, file_type):
    """
    Validates if the provided file path is of the correct file type.
    
    :param file_path: str, the path to the file to be validated
    :param file_type: str, the type of file to validate ('text', 'image', 'pdf')
    :return: bool, True if file is valid, False otherwise
    """
    if not file_path:
        return False

    if file_type not in FILE_TYPES:
        raise ValueError(f"Unknown file type: {file_type}")

    file_extension = os.path.splitext(file_path)[1].lower()
    if file_extension in FILE_TYPES[file_type]:
        return True
    else:
        messagebox.showerror("Error", ERROR_MSG_INVALID_FILE.format(file_type))
        return False
```