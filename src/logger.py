import logging
import os
from datetime import datetime

LOG_File = f"{datetime.now().strftime('%m_%d_%y_%H_%M_%S')}.log"
LOG_DIR = os.path.join(os.getcwd(),"logs")

os.makedirs(LOG_DIR,exist_ok=True)

LOG_FILE_PATH = os.path.join(LOG_DIR,LOG_File)
LOG_FORMAT = "[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s"

logging.basicConfig(
    format=LOG_FORMAT,
    level=logging.INFO,
    handlers=[
        logging.FileHandler(LOG_FILE_PATH),
        logging.StreamHandler() 
    ]
)

logger = logging.getLogger("mlproject_logger")

## for test loogger
# if __name__== "__main__":    
#     logging.info("logging started")
