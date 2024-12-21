import time

import pytest

from selenium import webdriver

from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

from Pages.SearchPage import SearchPage
from Pages.SearchResultPage import SearchResultPage


@pytest.mark.usefixtures("url_Data")
class Test_MakeMytrip(SearchPage,SearchResultPage):

    def test_OpenAndClose1(self,url_Data,flightSearch):
        self.browser = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))
        self.browser.maximize_window()
        print("log in")
        # self.browser.implicitly_wait(60)
        self.browser.get(url_Data)
        self.ClickOnAddPopup(self.browser)
        self.ClickOnFromCityDropdown(self.browser)
        self.SelectValueFromList(self.browser,flightSearch[0])
        self.ClickOnToCityDropdown(self.browser)
        self.SelectValueFromList(self.browser,flightSearch[1])
        self.SelectDate(self.browser,flightSearch[2])
        self.ClickOnSearchButton(self.browser)
        print(self.GetValidationText(self.browser))
        assert self.GetValidationText(self.browser) == "NETWORK PROBLEM"


        #self.browser.quit()

    def sartest12_OpenAndClose2(self,url_Data):
        self.browser = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))
        self.browser.maximize_window()
        # self.browser.implicitly_wait(60)
        self.browser.get(url_Data)
        #self.browser.get("https://www.leafground.com/alert.xhtml")
        self.browser.quit()


