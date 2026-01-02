import pytest

@pytest.fixture(scope="session")
def browser(playwright,pytestconfig):
    browser_name = pytestconfig.getoption("browser")
    headed = pytestconfig.getoption("headed")
    if isinstance(browser_name, list):
        browser_name = browser_name[0]
    browsers = getattr(playwright,browser_name).launch(headless = not headed)
    yield browsers
    browsers.close()

@pytest.fixture
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://automationexercise.com",wait_until="domcontentloaded")
    yield page 
    page.close()



