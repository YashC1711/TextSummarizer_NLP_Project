#mention the Custom log
# we can use this custom log in every project


import os
import sys
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"
log_dir = "logs"
log_filepath = os.path.join(log_dir,"running_logs.log")
os.makedirs(log_dir, exist_ok=True)



logging.basicConfig(
    level= logging.INFO,
    format= logging_str,

    handlers=[
        logging.FileHandler(log_filepath), #create the file 
        logging.StreamHandler(sys.stdout) # show logs in the terminal also
    ]
)

logger = logging.getLogger("textSummarizerLogger")