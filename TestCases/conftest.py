import pytest
from selenium import webdriver

from Utilities.Read_Config_File import Read_Config


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'edge':
        driver = webdriver.Edge()
    else:
        Edge_options = webdriver.EdgeOptions()
        Edge_options.add_argument("headless")
        driver = webdriver.Edge(options=Edge_options)

    r = Read_Config()
    # driver.get("https://automation.credence.in")
    driver.get(r.getURL())
    driver.maximize_window()
    return driver


@pytest.fixture(params=[("Unknown2023@gmail.com", "1234512345"), ("test@credence.in1", "test@123")])
def Data_for_login(request):
    return request.param


# ("test@credence.in", "test@1231"),
# ("test@credence.in1", "test@1231")
