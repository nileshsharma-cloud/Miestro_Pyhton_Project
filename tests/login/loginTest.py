import unittest

from baseUtilities.baseClass import BaseClass
from baseUtilities.openbrowser import openBrowser
from page.login.loginPage import LoginPage
from readdata.readdatafromCSV import ReadData


class LoginTests(unittest.TestCase):
    rd = ReadData()
    value = rd.getCSVData()

    @classmethod
    def setUpClass(cls):
        cls.driver = openBrowser()
        return cls.driver

    # @pytest.mark.run()
    def test_validateLoginWithValidCredentials(self):
        lp = LoginPage(self.driver)
      #  lp.checkLoginWithValidCredentials(self.value['username'][0], self.value['password'][0])
        lp.checkLoginWithValidCredentials()
    # @pytest.mark.run()
    def test_validateLoginWithInvalidCredentials(self):
        lp = LoginPage(self.driver)
        lp.checkLoginWithValidCredentials()

    # Call at the end of program execution
    @classmethod
    def tearDownClass(cls):
        bc = BaseClass(cls.driver)
        bc.screenshot_on_failure()

        # Closing the driver instance.
        cls.driver.quit()
