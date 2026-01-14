from pages.cartpage import CartPage
from pages.homepage import HomePage
from pages.loginpage import LoginPage

class TestProductPage:
    def test_add_items_to_cart(self, page):
        login_page = LoginPage(page)
        login_page.login("abc123@com","12345678")
        home_page = HomePage(page)
        home_page.goto_home_page()
        actual_home_page = home_page.verify_subscription()
        assert actual_home_page == "You have been successfully subscribed!"