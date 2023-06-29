import pytest


# # Parametrized fixture
# @pytest.fixture(params=[1, 2, 3])
# def input_data(request):
#     return request.param
#
#
# # Parametrized test function
# @pytest.mark.parametrize("value", [4, 5, 6])
# def test_multiply(input_data, value):
#     # result = input_data + value
#     # print(result)
#     print(input_data, value)

# -----------------

# @pytest.fixture(params=[("A", "1"), ("B", "2"), ("C", "3"), ("D", "4")])
# def Data_for_login(request):
#     return request.param
#
#
# def test_mark(Data_for_login):
#     print("Me:", Data_for_login[0], "::: She:", Data_for_login[1])
# -----------------

#
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
#
driver = webdriver.Edge()
# driver.find_element(By.LINK_TEXT, "")
driver.find_element().clear()

a = Alert(driver)
a.text()
a.accept()
a.dismiss()
