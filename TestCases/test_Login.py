import time

from PageObject.Login_Page_Objects import Login_Objects
from Utilities.Logger import LogGenerator


class Test_Login:
    log = LogGenerator.getLog()

    def test_login(self, setup, Data_for_login):
        self.log.info("Test Login is started")
        self.driver = setup
        self.log.info("Invoking Browser And Opening URL")
        l = Login_Objects(self.driver)
        time.sleep(2)
        l.Click_login()
        self.log.info("Clicking on Register link")
        l.Enter_Email(Data_for_login[0])
        self.log.info("Entering Email Addsress as: " + Data_for_login[0])
        l.Enter_Password(Data_for_login[1])
        self.log.info("Entering Password Addsress as: " + Data_for_login[1])
        l.Click_Login_Button()
        self.log.info("Clicking on Login Button")
        time.sleep(2)
        l.Status()
        self.log.info("Status of the page is Captured")
        self.driver.close()
        self.log.info("Test Login is Completed")
