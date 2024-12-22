import time

import pytest

from selenium import webdriver

from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

from Pages.HotelSearchPage import HotelSearchPage
from Pages.SearchPage import SearchPage
from Pages.SearchResultPage import SearchResultPage


@pytest.mark.usefixtures("url_Data")
class Test_MakeMytripHotel(SearchPage, HotelSearchPage):


    def test_ValidHoteSearch(self,url_Data):
        self.browser = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))
        self.browser.maximize_window()
        print("log in")
        # self.browser.implicitly_wait(60)
        self.browser.get(url_Data)
        self.ClickOnAddPopup(self.browser)
        self.ClickOnHotelMenu(self.browser)
        self.ClickOnCityDropdown(self.browser)
        self.SelectCity(self.browser,"Chennai")
        self.SelectHotelDate(self.browser, "12")
        self.SelectHotelDate(self.browser, "15")
        self.ClickOnRoomAndGuest(self.browser)
        self.ClickOnSearchButton(self.browser)
        time.sleep(10)





