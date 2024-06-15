import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from PageObjects.CheckoutPage import CheckOutPage
from PageObjects.ConfirmationPage import ConfirmationPage
from PageObjects.HomePage import HomePage
from Utilities.BaseClass import Baseclass


#@pytest.mark.usefixtures("setup")
class Testone(Baseclass):
    def test_e2e(self):
        homepage = HomePage(self.driver)
        checkoutpage= homepage.shopitems()
        #checkoutpage = CheckOutPage(self.driver)

        cards = checkoutpage.getCardTitles()
        i = -1
        for card in cards:
            i = i + 1
            cardText = card.text
            if cardText == "Blackberry":
                checkoutpage.getCardFooter()[i].click()

        checkoutpage.getproductadd().click()
        confirmpage = checkoutpage.checkOutItems()
        #confirmpage = ConfirmationPage(self.driver)

        confirmpage.getcountryfiled().send_keys("Ind")
        try:
            self.verficationforlink("India")
            confirmpage.getcountryselect().click()
        except:
            confirmpage.getcountryselect().click()
        confirmpage.getcountrycheckbox().click()
        confirmpage.getcountrypurchase().click()
        Alertmessage = confirmpage.getcountrymessage().text
        assert "Success! Thank you!" in Alertmessage
