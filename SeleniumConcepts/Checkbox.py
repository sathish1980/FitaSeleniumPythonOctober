import time

from selenium import webdriver

from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

class checkbox():

    def checkboximpl(self):
        self.browser = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))
        self.browser.maximize_window()
        #self.browser.implicitly_wait(60)
        self.browser.get("https://www.leafground.com/checkbox.xhtml")
        self.browser.find_element(by=By.XPATH,value="//*[@id='j_idt87:j_idt89']//*[starts-with(@class,'ui-chkbox-box')]").click()
        self.browser.find_element(by=By.CLASS_NAME,value="ui-toggleswitch-slider").click()
        time.sleep(2)
        print(self.browser.find_element(by=By.CLASS_NAME,value="ui-growl-title").text)
        time.sleep(10)

obj = checkbox()
obj.checkboximpl()