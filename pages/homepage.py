from pages.basepage import BasePage
from utils.logger import SingletonClass


class HomePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.logger = SingletonClass().setup_logger()
        self.home_page_link = page.locator("//a[normalize-space()='Home']")
        self.subscription_input = page.get_by_placeholder("Your email address")
        self.subscription_submit_button = page.locator("#subscribe")
        self.subscription_success_message = page.locator("div[class='alert-success alert']").text_content()

    def goto_home_page(self):
        self.logger.info("navigating to home page")
        self.click_element(self.home_page_link)

    def verify_subscription(self):
        self.scroll_to_the_element(self.subscription_input)
        self.fill_input(self.subscription_input,"abc123@com")
        self.click_element(self.subscription_submit_button)
        self.logger.info("verifying subscription input is visible")
        return self.subscription_success_message
    



