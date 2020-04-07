import unittest

import pytest

from page.login.loginPage import LoginPage
from baseUtilities.openbrowser import openBrowser
from baseUtilities.baseClass import BaseClass


class LoginTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = openBrowser()
        return cls.driver


    @pytest.mark.run(order=1)
    def test_validateLogin(self):
        lp = LoginPage(self.driver)
        lp.checkLoginWithValidCredentials()

    # Call at the end of program execution
    @classmethod
    def tearDownClass(cls):
        bc = BaseClass(cls.driver)
        bc.screenshot_on_failure()

        # Closing the driver instance.
        cls.driver.quit()
