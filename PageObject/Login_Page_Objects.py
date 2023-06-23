from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


class Login_Objects:
    Login = (By.LINK_TEXT, "Login")
    Email = (By.XPATH, "//input[@type='email']")
    Password = (By.XPATH, "//input[@id='password']")
    Login_Button = (By.XPATH, "//button[@class='btn btn-primary']")
    Status_Text = (By.XPATH, "/html/body/div/div[1]/p[1]")
    Tx = "A Online Shopping Site for Fashion & Lifestyle in India. India's Fashion Expert brings you a variety of footwear, Clothing, Accessories and lifestyle products."

    def __init__(self, driver):
        self.driver = driver

    def Click_login(self):
        self.driver.find_element(*Login_Objects.Login).click()

    def Enter_Email(self, email):
        self.driver.find_element(*Login_Objects.Email).send_keys(email)

    def Enter_Password(self, password):
        self.driver.find_element(*Login_Objects.Password).send_keys(password)

    def Click_Login_Button(self):
        self.driver.find_element(*Login_Objects.Login_Button).click()

    def Status(self):
        try:
            s = self.driver.find_element(*Login_Objects.Status_Text).text
            if s == Login_Objects.Tx:
                self.driver.get_screenshot_as_file("C:\\Users\\Tejas\\Class Project\\Screenshots\\Login\\Test_Login_Pass.png")
        except NoSuchElementException:
            self.driver.get_screenshot_as_file("C:\\Users\\Tejas\\Class Project\\Screenshots\\Login\\Test_Login_Fail.png")
