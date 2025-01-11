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


        self.browser.quit()

    def test12_OpenAndClose2(self,url_Data):
        self.browser = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))
        self.browser.maximize_window()
        # self.browser.implicitly_wait(60)
        self.browser.get(url_Data)
        #self.browser.get("https://www.leafground.com/alert.xhtml")
        self.browser.quit()


    def test_validFlightsearchwithMultidata(self,url_Data,flightdataFromExecl):
        self.browser = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))
        self.browser.maximize_window()
        print("log in")
        # self.browser.implicitly_wait(60)
        self.browser.get(url_Data)
        self.ClickOnAddPopup(self.browser)
        total_data =flightdataFromExecl
        print(total_data)
        size = len(total_data)
        print(size)
        totalcolumn = size / 3
        for i in range(1, int(totalcolumn) + 1):
            self.ClickOnFromCityDropdown(self.browser)
            self.SelectValueFromList(self.browser,flightdataFromExecl["From"+str(i)])
            self.ClickOnToCityDropdown(self.browser)
            print("to city",flightdataFromExecl["To"+str(i)])
            self.SelectValueFromList(self.browser,flightdataFromExecl["To"+str(i)])
            self.SelectDate(self.browser,flightdataFromExecl["Date"+str(i)])
            self.ClickOnSearchButton(self.browser)
            print(self.GetValidationText(self.browser))
            assert self.GetValidationText(self.browser) == "NETWORK PROBLEM"
            self.browser.back()
            time.sleep(5)

        self.browser.quit()


