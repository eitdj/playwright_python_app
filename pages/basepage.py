from utils.logger import SingletonClass


class BasePage:
    def __init__(self,page):
        self.page = page
        self.logger = SingletonClass().setup_logger()

    def get_title(self):
        try:
            self.logger.info("Getting page title")
            return self.page.title()
        except Exception as e:
            self.logger.error(f"Error getting page title: {e}")
            return None

    def find_elements(self,selectors):
        try:
            self.logger.info(f"Finding elements with selectors: {selectors}")
            locators = self.page.locator(selectors)
            return locators
        except Exception as e:
            self.logger.error(f"Error finding elements with selectors {selectors}: {e}")
            return None

    def click_element(self,locator):
        try:
            self.logger.info(f"Clicking element with locator: {locator}")
            locator.click()
        except Exception as e:
            self.logger.error(f"Error clicking element with locator {locator}: {e}")
            raise

    def fill_input(self,locator,text):
        try:
            self.logger.info(f"Filling input with text: {text}")
            locator.clear()
            locator.fill(text)
        except Exception as e:
            self.logger.error(f"Error filling input with text {text}: {e}")
            raise

    def get_text(self,locator):
        try:
            self.logger.info(f"Getting text from locator:{locator}")
            return locator.text_content()
        except Exception as e:
            self.logger.error(f"Error getting text from locator {locator}: {e}")
            raise
        
    def get_count_of_elements(self,locator):
        try:
            self.logger.info(f"Getting count of elements for locator: {locator}")
            return locator.count()
        except Exception as e:
            self.logger.error(f"Error getting count of elements for locator {locator}: {e}")
            raise