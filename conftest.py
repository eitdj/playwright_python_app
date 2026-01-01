import pytest

@pytest.fixture(scope="session")
def browser(playwright,pytestconfig):
    browser_name = pytestconfig.getoption("browser")
    headed = pytestconfig.getoption("headed")
    browser = getattr(playwright,browser_name[0]).launch(headless = not headed)
    yield browser
    browser.close()

@pytest.fixture
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://automationexercise.com",wait_until="domcontentloaded")
    yield page 
    page.close()



