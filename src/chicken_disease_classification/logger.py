import os
import sys
import logging
from datetime import datetime
logging_str="[%(asctime)s: %(lineno)d %(name)s: %(levelname)s: %(module)s: %(message)s]"  

LOG_FOLDER_NAME = f'{datetime.now().strftime("%m_%d_%Y_%H_%M_%S")}' 
logs_file_name = f'{LOG_FOLDER_NAME}.log'

log_dir="C://Users//anush//OneDrive//Desktop//git_al//chicken_disease_classification//logs"

log_filepath=os.path.join(log_dir,logs_file_name)

os.makedirs(log_dir,exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

loggerr=logging.getLogger("chicken_disease_classificationLogger") #object

# if __name__ == '__main__':
#      loggerr.info('Logging has started.')