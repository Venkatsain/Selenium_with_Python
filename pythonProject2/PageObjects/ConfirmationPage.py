from selenium.webdriver.common.by import By


class ConfirmationPage:

    def __init__(self, driver):
        self.driver = driver

    Countryfield = (By.CSS_SELECTOR,"#country")
    Countryselect = (By.XPATH,"//a[text()='India']")
    Countrycheckbox = (By.XPATH,"//div[@class='checkbox checkbox-primary']")
    Purchase = (By.XPATH,"//input[@class='btn btn-success btn-lg']")
    Successmessage = (By.XPATH,"//div[@class='alert alert-success alert-dismissible']")

    def getcountryfiled(self):
        return self.driver.find_element(*ConfirmationPage.Countryfield)


    def getcountryselect(self):
        return self.driver.find_element(*ConfirmationPage.Countryselect)

    def getcountrycheckbox(self):
        return self.driver.find_element(*ConfirmationPage.Countrycheckbox)

    def getcountrypurchase(self):
        return self.driver.find_element(*ConfirmationPage.Purchase)

    def getcountrymessage(self):
        return self.driver.find_element(*ConfirmationPage.Successmessage)

