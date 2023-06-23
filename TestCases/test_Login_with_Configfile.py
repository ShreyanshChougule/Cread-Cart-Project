import time

from PageObject.Login_Page_Objects import Login_Objects
from Utilities.Logger import LogGenerator
from Utilities.Read_Config_File import Read_Config


class Test_Login:
    log = LogGenerator.getLog()
    r = Read_Config()

    def test_login_with_Config_File(self, setup):
        self.log.info("Test Login is started")
        self.driver = setup
        self.log.info("Invoking Browser And Opening URL")
        l = Login_Objects(self.driver)
        time.sleep(2)
        l.Click_login()
        self.log.info("Clicking on Register link")
        l.Enter_Email(self.r.getname())
        self.log.info("Entering Email Addsress as: " + self.r.getname())
        l.Enter_Password(self.r.getpass())
        self.log.info("Entering Password Addsress as: " + self.r.getpass())
        l.Click_Login_Button()
        self.log.info("Clicking on Login Button")
        time.sleep(2)
        l.Status("login_with_Config_File")
        self.log.info("Status of the page is Captured")
        self.driver.close()
        self.log.info("Test Login is Completed")
