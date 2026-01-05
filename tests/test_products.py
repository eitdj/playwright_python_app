from pages.cartpage import CartPage
from pages.loginpage import LoginPage
from pages.productpage import ProductPage


class TestProductPage:
    def test_add_items_to_cart(self, page):
        login_page = LoginPage(page)
        login_page.login("abc123@com","12345678")
        product_page = ProductPage(page)
        product_page.search_item_by_name("Blue Top")
        product_page.continue_shopping()
        cart_page = CartPage(page)
        assert cart_page.get_cart_items_count() == 1