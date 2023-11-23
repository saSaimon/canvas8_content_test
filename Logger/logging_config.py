import logging
from logging.handlers import RotatingFileHandler
import os


def setup_logging():
    # Logger configuration - Only set up if not already configured
    if not logging.getLogger().hasHandlers():
        # Create the log directory if it doesn't exist
        if not os.path.exists('logs'):
            os.makedirs('logs')

        # Set up the logger
        log_file_path = os.path.join('logs', 'test_automation.log')

        logging.basicConfig(
            level=logging.DEBUG,
            format="%(asctime)s [%(levelname)s] %(module)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
            handlers=[
                logging.StreamHandler(),  # Console logging
                RotatingFileHandler(
                    filename=log_file_path,
                    maxBytes=5 * 1024 * 1024,  # 5 MB
                    backupCount=5            # Keep 5 backup files
                )
            ]
        )


def get_logger(name):
    # Setup logging if not already configured
    setup_logging()

    # Get the logger
    logger = logging.getLogger(name)
    return logger


# Usage
# logger = get_logger(__name__)
# logger.debug("This is a debug message.")
