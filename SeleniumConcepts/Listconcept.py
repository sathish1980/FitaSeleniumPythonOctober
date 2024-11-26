import time

from selenium import webdriver

from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

class ListConcept():

    def listimpl(self,expectedCountry):
        self.browser = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))
        self.browser.maximize_window()
        #self.browser.implicitly_wait(60)
        self.browser.get("https://www.leafground.com/select.xhtml")
        self.browser.find_element(by=By.XPATH,value="//*[@id='j_idt87:country']//*[starts-with(@class,'ui-selectonemenu-trigger')]").click()
        WebDriverWait(self.browser, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='j_idt87:country_items']//li[1]")))
        allElements  = self.browser.find_elements(by=By.XPATH,value="//*[@id='j_idt87:country_items']//li")
        for eachelement in allElements:
            actualCountry = eachelement.text
            print(actualCountry)
            if expectedCountry == actualCountry:
                eachelement.click()
                break
        time.sleep(10)

obj = ListConcept()
obj.listimpl("India")