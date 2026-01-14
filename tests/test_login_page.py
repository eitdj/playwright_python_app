
import pytest
from pages.basepage import BasePage
from pages.loginpage import LoginPage


class TestLoginPage:

    @pytest.mark.parametrize("username,password",[("abc123@com","12345678"),("abc123@","12345678"),("abc123@com","123458678")])
    def test_login_with_valid_credentials(self,page,username,password):
        login_page = LoginPage(page)
        login_page.login(username,password)
        base_page = BasePage(page)
        assert base_page.get_title() == 'Automation Exercise'
        