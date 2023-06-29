import time

import pytest
from PageObject.Registration_Page_Objects import Registration_Objects
from Utilities.Logger import LogGenerator
from Utilities.Read_Excel_File import Read_Excel_File


# @pytest.mark.skip
class Test_Registration:
    log = LogGenerator.getLog()
    R = Read_Excel_File()

    @pytest.mark.Registration
    def test_registration(self, setup):
        self.log.info("Test Registration is Started")
        self.driver = setup
        self.log.info("Invoking Browser and Opening URL")
        RO = Registration_Objects(self.driver)
        RO.Click_Register()
        self.log.info("Clicking on Register Button")
        time.sleep(3)
        for r in range(2, 4):
            RO.Enter_Username(self.R.read_excel(r, 2))
            self.log.info(f"Entering User Name as: {self.R.read_excel(r, 2)}")
            RO.Enter_Email(self.R.read_excel(r, 3))
            self.log.info(f"Entering Email as: {self.R.read_excel(r, 3)}")
            RO.Enter_Password(self.R.read_excel(r, 4))
            self.log.info(f"Entering Password as: {self.R.read_excel(r, 4)}")
            RO.Enter_Confirm_Password(self.R.read_excel(r, 5))
            self.log.info(f"Entering Confirm Password as: {self.R.read_excel(r, 5)}")
            RO.Click_Register_Button()
            self.log.info("Clicking on Register Button")
            RO.Status(r)
            self.log.info("Status of The Page is Captured")
        self.log.info("Test Registration is Completed..!")
