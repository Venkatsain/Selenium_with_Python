from selenium.webdriver.common.by import By

from PageObjects.CheckoutPage import CheckOutPage


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    Name = (By.XPATH,"(//input[@name='name'])[1]")
    Email = (By.XPATH,"//input[@name='email']")
    Password = (By.XPATH,"//input[@type='password']")
    Gender = (By.XPATH,"//select[@id='exampleFormControlSelect1']")
    Radio =(By.XPATH,"//input[@value='option1']")
    Submit = (By.XPATH,"//input[@value='Submit']")
    Verfication = (By.XPATH,"//div[@class='alert alert-success alert-dismissible']")


    def shopitems(self):
        self.driver.find_element(*HomePage.shop).click()
        checkoutpage = CheckOutPage(self.driver)
        return checkoutpage

        # driver.find_element(By.CSS_SELECTOR, "a[href*='shop']")

    def getname(self):
        return self.driver.find_element(*HomePage.Name)

    def getemail(self):
        return self.driver.find_element(*HomePage.Email)

    def getpassword(self):
        return self.driver.find_element(*HomePage.Password)

    def getgender(self):
        return self.driver.find_element(*HomePage.Gender)

    def getradio(self):
        return self.driver.find_element(*HomePage.Radio)

    def getsubmit(self):
        return self.driver.find_element(*HomePage.Submit)

    def getverify(self):
        return self.driver.find_element(*HomePage.Verfication)
