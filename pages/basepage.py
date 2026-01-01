from utils.logger import SingletonClass


class BasePage:
    def __init__(self,page):
        self.page = page
        self.logger = SingletonClass().setup_logger()

    def get_title(self):
        self.logger.info("Getting page title")
        return self.page.title()