import configparser
import logging

import logs.customlogger as cl
from baseUtilities.baseClass import BaseClass
from readdata.readfromExcel import ReadFromExcel


class LoginPage(BaseClass):

    # For initializing the driver
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Read the configuration file
    config = configparser.RawConfigParser()
    config.read(r"config/Properties.ini")

    # Locators of Login Page
    username = "email"
    password = "password"
    login_button = "//button[contains(@class,'previous-button')]"

    # Write logs in Logger file
    log = cl.customLogger(logging.DEBUG)

    # Create object of Read Data from CSV file
    # rd = ReadData()
    # value = rd.getCSVData()

    rd = ReadFromExcel("F:/Miestro_PythonProject/readdata/user_data.xlsx")

    # Check login functionality with valid username and password.
    def checkLoginWithValidCredentials(self):
        self.clickElement(self.getType("name"), self.username)

        # Enter values from csv file
        # self.send_keys_Element(self.getType("name"), self.username, username)

        self.send_keys_Element(self.getType("name"), self.username, self.rd.readData(0, i, 0))
        self.log.info("Username is entered")

        self.clickElement(self.getType("name"), self.password)

        # self.send_keys_Element(self.getType("name"), self.password, password)

        self.send_keys_Element(self.getType("name"), self.password, self.rd.readData(0, i, 0))
        self.log.info("password is entered")

        # Enter values from Properties file
        # self.send_keys_Element(self.getType("name"), self.password, self.config.get('Credentials', 'password'))

        self.driver.execute_script("window.scrollTo(0, 966)")

        self.clickElement(self.getType("xpath"), self.login_button)
        self.log.info("User is able to login.")
