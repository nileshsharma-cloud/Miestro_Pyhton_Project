from baseUtilities.baseClass import BaseClass
import logs.customlogger as cl
import logging
import configparser
from readdata.readdatafromCSV import ReadData


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
    login_button = "//button[@class='btnBasic btnBasic_theme_darkBlue btnBasic_size_full']"

    # Write logs in Logger file
    log = cl.customLogger(logging.DEBUG)

    # Create object of Read Data from CSV file
    rd = ReadData()
    value = rd.getCSVData()

    # Check login functionality with valid username and password.
    def checkLoginWithValidCredentials(self):
        self.clickElement(self.getType("name"), self.username)
        # Enter values from csv file
        self.send_keys_Element(self.getType("name"), self.username, self.value['username'][0])
        self.log.info("Username is entered")

        self.clickElement(self.getType("name"), self.password)
        self.send_keys_Element(self.getType("name"), self.password, self.value['password'][0])
        self.log.info("password is entered")

        # Enter values from Properties file
        # self.send_keys_Element(self.getType("name"), self.password, self.config.get('Credentials', 'password'))

        self.driver.execute_script("window.scrollTo(0, 966)")

        self.clickElement(self.getType("xpath"), self.login_button)
        self.log.info("User is able to login.")
