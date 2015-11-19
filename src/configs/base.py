
import os
import logging
from logging.handlers import WatchedFileHandler

CURRENT_FOLDER = os.path.dirname(os.path.abspath(__file__))
PROJECT_PATH = os.path.dirname(os.path.dirname(CURRENT_FOLDER))
LOG_PATH = os.path.join(PROJECT_PATH, "log")

if not os.path.exists(LOG_PATH):
    os.makedirs(LOG_PATH)

LOG_FORMAT = '%(asctime)s - %(filename)s - %(lineno)d - %(levelname)s - %(message)s'
formatter = logging.Formatter(LOG_FORMAT)

debug_log_handler = logging.StreamHandler()
debug_log_handler.setLevel(logging.DEBUG)
debug_log_handler.setFormatter(formatter)

info_log_handler = WatchedFileHandler(os.path.join(LOG_PATH, "info.log"))
info_log_handler.setLevel(logging.INFO)
info_log_handler.setFormatter(formatter)

error_log_handler = WatchedFileHandler(os.path.join(LOG_PATH, "error.log"))
error_log_handler.setLevel(logging.ERROR)
error_log_handler.setFormatter(formatter)

LOGGER = logging.getLogger("project_name")
LOGGER.setLevel(logging.DEBUG)
LOGGER.addHandler(debug_log_handler)
LOGGER.addHandler(info_log_handler)
LOGGER.addHandler(error_log_handler)

