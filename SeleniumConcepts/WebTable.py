import time

from selenium import webdriver

from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


class WebTableConcepts():

    def tableimpl(self,actualcountry):
        self.browser = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))
        self.browser.maximize_window()
        # self.browser.implicitly_wait(60)
        self.browser.get("https://leafground.com/table.xhtml")
        allpages = self.browser.find_elements(by=By.XPATH,value="//*[@class='ui-paginator-pages']//a") # get all the pages
        for eachPage in range(1, len(allpages) + 1): # navigate in to each page
            self.browser.find_element(by=By.XPATH, value="//*[@class='ui-paginator-pages']//a["+str(eachPage)+"]").click()
            time.sleep(2)
            allRows = self.browser.find_elements(by=By.XPATH,value="//table//tbody[@id='form:j_idt89_data']//tr") # get all the rows in the page
            for eachRows in range(1,len(allRows)+1): # navigate in to each row
                eachCountry = self.browser.find_element(by=By.XPATH, value="//table//tbody[@id='form:j_idt89_data']//tr["+str(eachRows)+"]//td[2]//span[contains(@style,'vertical-align')]").text # get country from each row
                if eachCountry ==actualcountry: # compare the actual country from application with the expected country
                    resp = self.browser.find_element(by=By.XPATH,
                                                            value="//table//tbody[@id='form:j_idt89_data']//tr[" + str(
                                                                eachRows) + "]//td[3]//span[contains(@style,'vertical-align')]").text
                    print(resp)

        time.sleep(10)

obj = WebTableConcepts()
obj.tableimpl("India")
