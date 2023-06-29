import time

import pytest

from PageObject.Login_Page_Objects import Login_Objects
from Utilities.Logger import LogGenerator
from Utilities.Read_Config_File import Read_Config


# @pytest.mark.skip
class Test_Login:
    log = LogGenerator.getLog()
    r = Read_Config()

    @pytest.mark.Parameters
    def test_login_with_parameters(self, setup, Data_for_login):
        self.log.info("Test Login With Parameters is Started")
        self.driver = setup
        self.log.info("Invoking Browser and Opening URL")
        l = Login_Objects(self.driver)
        time.sleep(2)
        l.Click_login()
        self.log.info("Clicking on Login Button")
        l.Enter_Email(Data_for_login[0])
        self.log.info("Entering Email Addsress as: " + Data_for_login[0])
        l.Enter_Password(Data_for_login[1])
        self.log.info("Entering Password Addsress as: " + Data_for_login[1])
        l.Click_Login_Button()
        self.log.info("Clicking on Login Button")
        time.sleep(2)
        l.Status()
        self.log.info("Status of The Page is Captured")
        self.driver.close()
        self.log.info("Test Login With Parameters is Completed")

    @pytest.mark.Config_File
    def test_login_with_Config_File(self, setup):
        self.log.info("Test Login With Configuration File is started")
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
        l.Status("login_with_Config_File_is")
        self.log.info("Status of the page is Captured")
        self.driver.close()
        self.log.info("Test Login With Configuration File is Completed")
