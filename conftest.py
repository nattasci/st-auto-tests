import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help='Choose language')
    parser.addoption('--browser_name', action='store', default='chrome',
                     help='Choose browser: chrome or firefox')

@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    browser_name = request.config.getoption("browser_name")
    browser = None
    
    if language is None:
        raise pytest.UsageError("--language is missing")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages':language})

    if browser_name == "chrome":
        print("\nstart chrome for test")
        browser = webdriver.Chrome(options = options)

    elif browser_name == "firefox":
        print("\nstart firefox for test")
        browser = webdriver.Firefox(options = options)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
   
    yield browser
    print("\nquit browser")
    browser.quit()
