import time

import pytest
from PageObject.Login_Page_Objects import Login_Objects
from Utilities.Logger import LogGenerator
from Utilities.Read_Config_File import Read_Config


# class Test_Login:
#     r = Read_Config()

    # @pytest.mark.skip
    # @pytest.mark.Config_File
    # def test_login_with_Config_File(self, setup):
    #     log = LogGenerator.getLog()
    #     log.info("Test Login is started")
    #     self.driver = setup
    #     log.info("Invoking Browser And Opening URL")
    #     l = Login_Objects(self.driver)
    #     time.sleep(2)
    #     l.Click_login()
    #     log.info("Clicking on Register link")
    #     l.Enter_Email(self.r.getname())
    #     log.info("Entering Email Addsress as: " + self.r.getname())
    #     l.Enter_Password(self.r.getpass())
    #     log.info("Entering Password Addsress as: " + self.r.getpass())
    #     l.Click_Login_Button()
    #     log.info("Clicking on Login Button")
    #     time.sleep(2)
    #     l.Status("login_with_Config_File")
    #     log.info("Status of the page is Captured")
    #     self.driver.close()
    #     log.info("Test Login is Completed")
