from pages.basepage import BasePage


class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.page = page
        self.login_link = page.get_by_text(" Signup / Login")
        self.email_input = page.get_by_placeholder("Email Address").first
        self.password_input = page.get_by_placeholder("Password")
        self.login_button = page.get_by_role("button", name = "Login")

    def enter_email(self,email):
        self.fill_input(self.email_input, email)
        self.email_input.fill(email)
    def enter_password(self,password):
        self.fill_input(self.password_input, password)
    
    def login(self,email,password):
        self.click_element(self.login_link)
        self.enter_email(email)
        self.enter_password(password)
        self.click_element(self.login_button)