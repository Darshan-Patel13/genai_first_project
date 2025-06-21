import logging
import os
from datetime import datetime


LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
#getcwd to access current working directory
log_path=os.path.join(os.getcwd(),"logs")
if not os.path.exists(log_path):
    os.mkdir(log_path)  # only create if it doesn't exist
#path of file
LOG_FILEPATH=os.path.join(log_path,LOG_FILE)

logging.basicConfig(level=logging.INFO,filename=LOG_FILEPATH,format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s -%(message)s")