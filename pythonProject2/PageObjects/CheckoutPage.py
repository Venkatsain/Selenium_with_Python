from selenium.webdriver.common.by import By

from PageObjects.ConfirmationPage import ConfirmationPage


class CheckOutPage:

    def __init__(self, driver):
        self.driver = driver

    # driver.find_elements_by_css_selector(".card-title a")
    # driver.find_element_by_xpath("//button[@class='btn btn-success']")
    cardTitle = (By.CSS_SELECTOR, ".card-title a")
    cardFooter = (By.CSS_SELECTOR, ".card-footer button")
    productadd = (By.CSS_SELECTOR, "a[class*='btn-primary']")
    checkOut = (By.XPATH, "//button[@class='btn btn-success']")

    def getCardTitles(self):
        return self.driver.find_elements(*CheckOutPage.cardTitle)

    def getCardFooter(self):
        return self.driver.find_elements(*CheckOutPage.cardFooter)

    def getproductadd(self):
        return self.driver.find_element(*CheckOutPage.productadd)

    def checkOutItems(self):
        self.driver.find_element(*CheckOutPage.checkOut).click()
        confirmpage = ConfirmationPage(self.driver)
        return confirmpage
