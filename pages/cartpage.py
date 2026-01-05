from pages.basepage import BasePage


class CartPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.cart_items = page.get_by_role("link", name="Cart")
        self.cart_items_count = page.locator('.cart_quantity')
        self.product_name_in_cart = page.locator('.cart_description .product-name')
    
    def goto_cart(self):
        self.click_element(self.cart_items)
    
    def get_cart_items_count(self):
        self.goto_cart()
        count = self.get_count_of_elements(self.cart_items_count)
        return count
    
    def get_product_name_in_cart(self):
        return self.get_text(self.product_name_in_cart)


