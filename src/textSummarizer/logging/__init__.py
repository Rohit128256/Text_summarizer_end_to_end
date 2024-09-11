import logging
import os 
import sys
from datetime import datetime

# Define the log file with the current timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Create the logs directory if it doesn't exist
logs_path = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_path, exist_ok=True)

# Define the full log file path
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Create handlers: FileHandler for logging to a file and StreamHandler for console output
file_handler = logging.FileHandler(LOG_FILE_PATH)
stream_handler = logging.StreamHandler(sys.stdout)

# Configure logging
logging.basicConfig(
    format='[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    handlers=[file_handler, stream_handler]  # Use the custom handlers instead of filename
)