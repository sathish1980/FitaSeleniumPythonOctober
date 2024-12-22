from selenium.webdriver.common.by import By

from Commons.CommonElements import CommonElements
from Pages.SearchPage import SearchPage


class HotelSearchPage(CommonElements):

    def ClickOnHotelMenu(self,browser):
        self.ElementToBeClickable(browser, "//*[@data-cy='menu_Hotels']//a")
        # WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@data-cy='closeModal']")))
        browser.find_element(by=By.XPATH, value="//*[@data-cy='menu_Hotels']//a").click()

    def ClickOnCityDropdown(self,browser):
        self.ElementToBeClickable(browser, "//*[@for='city']")
        # WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@data-cy='closeModal']")))
        browser.find_element(by=By.XPATH, value="//*[@for='city']").click()

    def ClickOnRoomAndGuest(self,browser):

        self.ElementToBeClickable(browser, "//*[starts-with(@data-cy,'RoomsGuestsNew')]")
        # WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@data-cy='closeModal']")))
        browser.find_element(by=By.XPATH, value="//*[starts-with(@data-cy,'RoomsGuestsNew')]").click()

    def SelectCity(self,browser,expectedCity):
        self.ElementToBeClickable(browser, "//*[@id='react-autowhatever-1']//li[last()]")
        allCities = browser.find_elements(by=By.XPATH,value="//*[@id='react-autowhatever-1']//li")
        for eachvalue in range(1,len(allCities)+1):
            actaulCity = browser.find_element(by=By.XPATH, value="//*[@id='react-autowhatever-1']//li["+str(eachvalue)+"]//p[@class='sr_city']//span").text
            print(actaulCity)
            if actaulCity == expectedCity:
                browser.find_element(by=By.XPATH, value="//*[@id='react-autowhatever-1']//li[" + str(
                    eachvalue) + "]").click()
                break
