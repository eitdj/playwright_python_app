from pages.basepage import BasePage


class ProductPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.product_link_text = page.get_by_role("link", name=" Products")
        self.add_to_cart_buttons = page.get_by_text("Add to cart")
        self.continue_shopping_button = page.get_by_role("button", name="Continue Shopping")
        self.product_price = page.locator('.price')
        self.search_tab = page.locator("input[name='search']")
        self.search_button = page.locator("#submit_search")

    def search_item_by_name(self, item_name):
        self.click_element(self.product_link_text)
        self.logger.info(f"Searching for item: {item_name}")
        self.fill_input(self.search_tab, item_name)
        self.click_element(self.search_button)
        self.click_element(self.add_to_cart_buttons.nth(1))
    
    def continue_shopping(self):
        self.click_element(self.continue_shopping_button)