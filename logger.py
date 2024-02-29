import logging
import os

# Define the logging configuration
def setup_logging():
    log_directory = "logs"
    if not os.path.exists(log_directory):
        os.makedirs(log_directory)
    log_filename = os.path.join(log_directory, "app.log")

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        handlers=[
            logging.FileHandler(log_filename, 'a', 'utf-8'),
            logging.StreamHandler()
        ]
    )

# Function to log an operation
def log_operation(message):
    logging.info(message)

# Function to log an error
def log_error(message):
    logging.error(message)