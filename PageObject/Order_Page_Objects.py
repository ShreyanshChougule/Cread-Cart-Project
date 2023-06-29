import time

from selenium.common import NoSuchElementException
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Order_Objects:

    Apple = (By.XPATH, "//h3[normalize-space()='Apple Macbook Pro']")
    Add_Cart = (By.XPATH, "//input[@value='Add to Cart']")
    # Checkout = (By.XPATH, "//a[@class='btn btn-success btn-lg']")
    Proceed_Checkout = (By.XPATH, "//a[@class='btn btn-success btn-lg']")
    FN = (By.XPATH, "//input[@id='first_name']")
    LN = (By.XPATH, "//input[@id='last_name']")
    Phone = (By.XPATH, "//input[@id='phone']")
    Address = (By.XPATH, "//textarea[@id='address']")
    ZIP = (By.XPATH, "//input[@id='zip']")
    State = (By.XPATH, "//select[@id='state']")
    Owner = (By.XPATH, "//input[@id='owner']")
    CVV = (By.XPATH, "//input[@id='cvv']")
    Card_No = (By.XPATH, "//input[@id='cardNumber']")
    Exp_Year = (By.XPATH, "//select[@id='exp_year']")
    Month = (By.XPATH, "//select[@id='exp_month']")
    Continue_To_Checkout = (By.XPATH, "//button[@id='confirm-purchase']")
    Order_Placed = (By.XPATH, "//p[normalize-space()='Your order has been placed successfully.']")

    def __init__(self, driver):
        self.driver = driver

    def apple_macbook_pro(self):
        self.driver.find_element(*Order_Objects.Apple).click()
        # Click on product-->Apple Macbook Pro

    def add_cart(self):
        self.driver.find_element(*Order_Objects.Add_Cart).click()
        # Add To Cart

    # def checkout(self):
    #     self.driver.find_element(*Order_Objects.Checkout).click()
    #     # Clicking on Checkout

    def proceed_checkout(self):
        self.driver.find_element(*Order_Objects.Proceed_Checkout).click()
        # Clicking on Checkout page

    def first_name(self, First_Name):
        self.driver.find_element(*Order_Objects.FN).clear()
        self.driver.find_element(*Order_Objects.FN).send_keys(First_Name)
        # Entering First Name

    def last_name(self, Last_Name):
        self.driver.find_element(*Order_Objects.LN).clear()
        self.driver.find_element(*Order_Objects.LN).send_keys(Last_Name)
        # Entering Last Name

    def phone(self, Phone_No):
        self.driver.find_element(*Order_Objects.Phone).clear()
        self.driver.find_element(*Order_Objects.Phone).send_keys(Phone_No)
        # Entering Phone Number

    def address(self, Add):
        self.driver.find_element(*Order_Objects.Address).clear()
        self.driver.find_element(*Order_Objects.Address).send_keys(Add)
        # Entering address

    def zip(self, ZIP):
        self.driver.find_element(*Order_Objects.ZIP).clear()
        self.driver.find_element(*Order_Objects.ZIP).send_keys(ZIP)
        # Entering zip code

    def state(self, Indx):
        Select(self.driver.find_element(*Order_Objects.State)).select_by_index(Indx)
        # Selecting state

    def owner(self, Owner):
        self.driver.find_element(*Order_Objects.Owner).clear()
        self.driver.find_element(*Order_Objects.Owner).send_keys(Owner)
        # Entering Owner Name

    def cvv(self, CVV):
        self.driver.find_element(*Order_Objects.CVV).clear()
        self.driver.find_element(*Order_Objects.CVV).send_keys(CVV)
        # Entering Card CVV

    def card_no(self, Card_Number):
        self.driver.find_element(*Order_Objects.Card_No).clear()
        SPACE = ''
        for i in range(len(Card_Number)):
            if i > 0 and i % 4 == 0:
                SPACE += ' '  # Add a space after every 4 digits
            SPACE += Card_Number[i]
        New_List = SPACE.split(' ')
        self.driver.find_element(*Order_Objects.Card_No).send_keys(New_List[0])
        self.driver.find_element(*Order_Objects.Card_No).send_keys(New_List[1])
        self.driver.find_element(*Order_Objects.Card_No).send_keys(New_List[2])
        self.driver.find_element(*Order_Objects.Card_No).send_keys(New_List[3])
        # Entering Card Number : 4716 1089 9971 6531

    def year_and_month(self, Card_Exp, Month):
        Select(self.driver.find_element(*Order_Objects.Exp_Year)).select_by_visible_text(Card_Exp)
        # Select Card Exp Year
        Select(self.driver.find_element(*Order_Objects.Month)).select_by_index(Month)
        # Select Month

    def submit(self):
        self.driver.find_element(*Order_Objects.Continue_To_Checkout).click()
        # Click on Submit Button
        time.sleep(2)
        try:
            alrt = Alert(self.driver)  # get the text of the confirmation alert
            time.sleep(2)
            # handling the confirmation alert
            if alrt.text == "Wrong card number":
                alrt.accept()   # click OK button
                self.driver.get_screenshot_as_file("C:\\Users\\Tejas\\Class Project\\Screenshots\\Order\\Order_Unsuccessful.png")
            else:
                alrt.dismiss()  # click Cancel button
        except NoSuchElementException:
            self.driver.find_element(*Order_Objects.Order_Placed)
            self.driver.get_screenshot_as_file("C:\\Users\\Tejas\\Class Project\\Screenshots\\Order\\Order_Successful.png")
