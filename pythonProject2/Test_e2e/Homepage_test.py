import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from PageObjects.HomePage import HomePage
from TestData.Testdata_Homepage import HomepageData
from Utilities.BaseClass import Baseclass

class TestHomePage(Baseclass):
    def test_formsubmission(self,getdata):

        log = self.getlogger()
        homepage = HomePage(self.driver)
        homepage.getname().send_keys(getdata["FirstName"])
        homepage.getemail().send_keys(getdata["Email"])
        homepage.getpassword().send_keys(getdata["Password"])
        self.selectbyindex(homepage.getgender(),0)

        homepage.getradio().click()

        homepage.getsubmit().click()
        ActualMessage = homepage.getverify().text
        assert "Success!" in ActualMessage


    @pytest.fixture(params=HomepageData.test_datahomepage)
    def getdata(self,request):
        return request.param