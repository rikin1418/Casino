from selenium import webdriver
import pytest

@pytest.yield_fixture(scope='function')
def prePostMethod(request,browser):

    if browser == "chrome":
        # launch the browser
        driver = webdriver.Chrome()
        # max the browser
        driver.maximize_window()
        # implicit wait
        driver.implicitly_wait(10)
        # navigate to the app
        driver.get("https://www.gmail.com")
    else:
        # launch the browser
        driver = webdriver.Firefox()
        # max the browser
        driver.maximize_window()
        # implicit wait
        driver.implicitly_wait(10)
        # navigate to the app
        driver.get("https://www.gmail.com")

    if request.cls is not None:
        request.cls.driver=driver

    yield driver

    # close the browser
    driver.close()

def pytest_addoption(parser):
    parser.addoption('--browser')

@pytest.fixture(scope='session')
def browser(request):
    request.config.getoption('--browser')