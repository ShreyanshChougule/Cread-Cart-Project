from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from Utilities.Read_Excel_File import Read_Excel_File


class Registration_Objects:
    Registration = (By.LINK_TEXT, "Register")
    Name = (By.ID, "name")
    Email_ID = (By.NAME, "email")
    Password_ID = (By.ID, "password")
    Confirm_Password_ID = (By.ID, "password-confirm")
    Register = (By.CLASS_NAME, "btn")
    Status_Text = (By.XPATH, "/html/body/div/div[1]/p[1]")
    Tx = "A Online Shopping Site for Fashion & Lifestyle in India. India's Fashion Expert brings you a variety of footwear, Clothing, Accessories and lifestyle products."

    def __init__(self, driver):
        self.driver = driver

    def Click_Register(self):
        self.driver.find_element(*Registration_Objects.Registration).click()

    def Enter_Username(self, username):
        self.driver.find_element(*Registration_Objects.Name).send_keys(username)

    def Enter_Email(self, email):
        self.driver.find_element(*Registration_Objects.Email_ID).send_keys(email)

    def Enter_Password(self, password):
        self.driver.find_element(*Registration_Objects.Password_ID).send_keys(password)

    def Enter_Confirm_Password(self, confirm_password):
        self.driver.find_element(*Registration_Objects.Confirm_Password_ID).send_keys(confirm_password)

    def Click_Register_Button(self):
        self.driver.find_element(*Registration_Objects.Register).click()

    def Status(self, r):
        D = Read_Excel_File()
        try:
            s = self.driver.find_element(*Registration_Objects.Status_Text).text
            if s == Registration_Objects.Tx:
                self.driver.get_screenshot_as_file("C:\\Users\\Tejas\\Class Project\\Screenshots\\Registeration\\Test_Registration_Pass.png")
                D.write_excel(r, 7, "Pass")
        except NoSuchElementException:
            self.driver.get_screenshot_as_file("C:\\Users\\Tejas\\Class Project\\Screenshots\\Registeration\\Test_Registration_Fail.png")
            D.write_excel(r, 7, "Fail")