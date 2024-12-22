import time

import pytest

from selenium import webdriver


from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

from Pages.HotelSearchPage import HotelSearchPage
from Pages.SearchPage import SearchPage
from Pages.SearchResultPage import SearchResultPage


@pytest.mark.usefixtures("url_Data")
class Test_MakeMytripHotel(SearchPage, HotelSearchPage):


    def test_validhotesearch(self,url_Data, hotelsearch):
        self.browser = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))
        self.browser.maximize_window()
        print("log in")
        # self.browser.implicitly_wait(60)
        self.browser.get(url_Data)
        self.ClickOnAddPopup(self.browser)
        self.ClickOnHotelMenu(self.browser)
        self.ClickOnCityDropdown(self.browser)
        self.SelectCity(self.browser,hotelsearch[0])
        self.SelectHotelDate(self.browser, hotelsearch[1])
        self.SelectHotelDate(self.browser, hotelsearch[2])
        self.ClickOnRoomAndGuest(self.browser)
        self.ClickOnSearchButton(self.browser)
        time.sleep(10)





