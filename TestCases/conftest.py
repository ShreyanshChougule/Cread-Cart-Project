import pytest
from selenium import webdriver


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
    driver.get("https://automation.credence.in")
    driver.maximize_window()
    return driver


@pytest.fixture(params=[("Unknown2023@gmail.com", "1234512345"), ("test@credence.in1", "test@123")])
def Data_for_login(request):
    return request.param


# ("test@credence.in", "test@1231"),
# ("test@credence.in1", "test@1231")
def test_new(Data_for_login):
    print("A = ", Data_for_login[0], "and B = ", Data_for_login[1])