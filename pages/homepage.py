from pages.basepage import BasePage
from utils.logger import SingletonClass


class HomePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.logger = SingletonClass().setup_logger()


