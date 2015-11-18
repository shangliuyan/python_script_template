
import os
import logging

CURRENT_FOLDER = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(os.path.dirname(CURRENT_FOLDER))
LOG_ROOT = os.path.join(PROJECT_ROOT, "log")

if not os.path.exists(LOG_ROOT):
    os.makedirs(LOG_ROOT)

LOG_FORMAT = '%(asctime)s - %(filename)s - %(lineno)d - %(levelname)s - %(message)s'
formatter = logging.Formatter(LOG_FORMAT)

debug_log_handler = logging.StreamHandler()
debug_log_handler.setLevel(logging.DEBUG)
debug_log_handler.setFormatter(formatter)

info_log_handler = logging.FileHandler(os.path.join(LOG_ROOT, "info.log"))
info_log_handler.setLevel(logging.INFO)
info_log_handler.setFormatter(formatter)

error_log_handler = logging.FileHandler(os.path.join(LOG_ROOT, "error.log"))
error_log_handler.setLevel(logging.ERROR)
error_log_handler.setFormatter(formatter)

LOGGER = logging.getLogger("project_name")
LOGGER.setLevel(logging.Debug)
LOGGER.addHandler(debug_log_handler)
LOGGER.addHandler(info_log_handler)
LOGGER.addHandler(error_log_handler)

