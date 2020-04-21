import logging
import traceback
from _datetime import datetime

from selenium.webdriver.common.by import By

import logs.customlogger as cl


class BaseClass():
    # Writing logs in Logger file
    log = cl.customLogger(logging.DEBUG)

    # For initializing the driver
    def __init__(self, driver):
        self.driver = driver

    # Get the type of locator
    def getType(self, locator_type):
        try:
            if locator_type == "xpath":
                self.log.info("locator type :", locator_type)
                return By.XPATH
            if locator_type == "id":
                return By.ID
            if locator_type == "name":
                self.log.info("locator type :", locator_type)
                return By.NAME
        except:
            print("Unable to find locator type.")

    # Click the element
    def clickElement(self, locator_type, locator_value):
        try:
            element = self.getType(locator_type)
            self.driver.find_element(element, locator_value).click()
            print("Element is clicked.")

        except Exception:
            print("Element is not displayed so unable to perform operations on it.")
            traceback.print_exception()

    # Sending keys to the field
    def send_keys_Element(self, locator_type, locator_value, pass_value):
        try:
            element = self.getType(locator_type)
            self.driver.find_element(element, locator_value).clear()
            self.driver.find_element(element, locator_value).send_keys(pass_value)
            print("Value is inserted in the textfield..")

        except Exception:
            print("Element is not displayed so unable to send keys to it.")
            traceback.print_exception()

    # Taking screenshot on failure
    def screenshot_on_failure(self):
        now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        self.driver.get_screenshot_as_file("screenshot\screenshot - %s.png" % now)
