import configparser
from selenium import webdriver


def openBrowser():

    # Read the configuration file
    config = configparser.RawConfigParser()
    config.read(r"config/Properties.ini")
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(config.get('Credentials', 'URL'))
    driver.implicitly_wait(10)
    return driver
