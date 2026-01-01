import logging
import datetime
import os

class SingletonClass:
    _logger = None

    def __new__(cls):
        if cls._logger is None:
            cls._logger = super().__new__(cls)
        return cls._logger

    def setup_logger(self):
        logger = logging.getLogger("playwright_logger")
        logger.setLevel(logging.DEBUG)

        if not logger.handlers:
            log_dir = os.path.join("Summary", "logs")
            os.makedirs(log_dir, exist_ok=True)

            log_file = os.path.join(
                log_dir,
                f"log_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
            )

            formatter = logging.Formatter(
                "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
            )

            file_handler = logging.FileHandler(log_file)
            file_handler.setFormatter(formatter)

            stream_handler = logging.StreamHandler()
            stream_handler.setFormatter(formatter)

            logger.addHandler(file_handler)
            logger.addHandler(stream_handler)

        return logger

        
        