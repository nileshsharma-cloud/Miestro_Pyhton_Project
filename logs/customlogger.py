import inspect
import logging


def customLogger(loglevel):
    # Gets the name of the class/method from where it is called
    loggerName = inspect.stack()[1][3]
    logger = logging.getLogger(loggerName)

    # by default log all messages
    logger.setLevel(logging.DEBUG)

    # Generating the logs in different folder
    fileHandler = logging.FileHandler(filename=r"F:/Miestro_PythonProject/logs/automation.log", mode='a')
    fileHandler.setLevel(loglevel)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s',
                                  datefmt='%m/%d/%y %I:%M:%S %p')
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)

    return logger
