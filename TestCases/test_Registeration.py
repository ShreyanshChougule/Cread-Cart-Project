import time

import pytest
from PageObject.Registration_Page_Objects import Registration_Objects
from Utilities.Read_Excel_File import Read_Excel_File


# @pytest.mark.skip
class Test_Registration:

    @pytest.mark.Registration
    def test_registration(self, setup):
        self.driver = setup
        r = Registration_Objects(self.driver)
        D = Read_Excel_File()
        r.Click_Register()
        time.sleep(3)
        for i in range(2, 4):
            r.Enter_Username(D.read_excel(i, 2))
            r.Enter_Email(D.read_excel(i, 3))
            r.Enter_Password(D.read_excel(i, 4))
            r.Enter_Confirm_Password(D.read_excel(i, 5))
            r.Click_Register_Button()
            r.Status(i)
