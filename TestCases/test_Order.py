import time

import pytest

from PageObject.Login_Page_Objects import Login_Objects
from PageObject.Order_Page_Objects import Order_Objects
from Utilities.Logger import LogGenerator
from Utilities.Read_Config_File import Read_Config
from Utilities.Read_Excel_File import Read_Excel_File


@pytest.mark.skip("Test Order is Completed..!")
class Test_Order:
    log = LogGenerator.getLog()
    r = Read_Config()

    @pytest.mark.Order
    def test_order(self, setup):
        self.log.info("Test Order is Started")
        self.driver = setup
        self.log.info("Invoking Browser and Opening URL")
        l = Login_Objects(self.driver)
        O = Order_Objects(self.driver)
        R = Read_Excel_File()
        time.sleep(2)
        l.Click_login()
        l.Enter_Email(self.r.getname())
        l.Enter_Password(self.r.getpass())
        l.Click_Login_Button()
        self.log.info("Login Througt Valid Inputs")
        time.sleep(2)
        # ----------------------------------
        # Working Page Opractions Starts:
        O.apple_macbook_pro()
        self.log.info("Select Apple Mackbook and Click")
        O.add_cart()
        self.log.info("Adding Product to Cart")
        O.proceed_checkout()
        self.log.info("Proceding For Checkout")
        O.first_name(R.read_excel(10, 2))
        self.log.info(f"Entering First Name: {R.read_excel(10, 2)}")
        O.last_name(R.read_excel(10, 3))
        self.log.info(f"Entering Last Name: {R.read_excel(10, 3)}")
        O.phone(R.read_excel(10, 4))
        self.log.info(f"Entering Phone Number: {R.read_excel(10, 4)}")
        O.address(R.read_excel(10, 5))
        self.log.info(f"Entering Address: {R.read_excel(10, 5)}")
        O.zip(R.read_excel(10, 6))
        self.log.info(f"Entering ZIP: {R.read_excel(10, 6)}")
        O.state(R.read_excel(10, 7))
        self.log.info(f"Select State Name: {R.read_excel(10, 7)}")
        O.owner(R.read_excel(10, 8))
        self.log.info(f"Entering Owner Name: {R.read_excel(10, 8)}")
        O.cvv(R.read_excel(10, 9))
        self.log.info(f"Entering CVV: {R.read_excel(10, 9)}")
        O.card_no(str(R.read_excel(10, 10)))
        self.log.info(f"Entering Card Details as: {R.read_excel(10, 10)}")
        O.year_and_month(str(R.read_excel(10, 11)), str(R.read_excel(10, 12)))
        self.log.info(f"Select Expirey Year and Month: {R.read_excel(10, 12)}")
        O.submit()
        self.log.info("Status of the page is Captured")
        self.driver.close()
        self.log.info("Test Order is Completed...!")
