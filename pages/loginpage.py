class LoginPage:
    def __init__(self, page):
        self.page = page
        self.login_link = page.get_by_text(" Signup / Login")
        self.email_input = page.get_by_placeholder("Email Address").first
        self.password_input = page.get_by_placeholder("Password")
        self.login_button = page.get_by_role("button", name = "Login")
    
    def login(self,email,password):
        self.login_link.click()
        self.email_input.fill(email)
        self.password_input.fill(password)
        self.login_button.click()