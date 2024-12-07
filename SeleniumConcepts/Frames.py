import time

from selenium import webdriver

from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


class FrameConcept():

    def Alertimpl(self):
        self.browser = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))
        self.browser.maximize_window()
        # self.browser.implicitly_wait(60)
        self.browser.get("https://leafground.com/frame.xhtml")
        allFrames = self.browser.find_elements(by=By.TAG_NAME,value="iframe")
        for eachframe in range(0,len(allFrames)):
            self.browser.switch_to.frame(eachframe)
            elementExist = self.browser.find_elements(by=By.XPATH, value="//*[@id='Click' and contains(@style,'ff7295')]")
            if len(elementExist) >0:
                self.browser.find_element(by=By.XPATH, value="//*[@id='Click' and contains(@style,'ff7295')]").click()
                break
            self.browser.switch_to.default_content()

        time.sleep(10)
        #WebDriverWait(self.browser, 20).until(EC.presence_of_element_located((By.XPATH, "//*[@id='Click' and contains(@style,'ff7295')]")))


obj = FrameConcept()
obj.Alertimpl()
