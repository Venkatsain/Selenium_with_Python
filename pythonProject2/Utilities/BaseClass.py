import inspect

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures('setup')
class Baseclass:

    def getlogger(self):
        loggername = inspect.stack()[1][3]
        logger = logging.getLogger(loggername)
        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        logger.setLevel(logging.CRITICAL)
        logger.debug("A debug statement is executed")
        logger.info("Information statement")
        logger.debug("A debug statement is executed")
        logger.warning("Something is in warning mode")
        logger.error("A Major error has happend")
        logger.critical("Critical issue")

    def verficationforlink(self,text):
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.XPATH,text)))

    def selectbyindex(self,locator,index):
        GenderDropdown = Select(locator)
        GenderDropdown.select_by_index(index)

