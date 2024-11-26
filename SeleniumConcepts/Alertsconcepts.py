import time

from selenium import webdriver

from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

class AlertConcept():

    def Alertimpl(self):
        self.browser = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))
        self.browser.maximize_window()
        #self.browser.implicitly_wait(60)
        self.browser.get("https://www.leafground.com/alert.xhtml")
        self.browser.find_element(by=By.ID,value="j_idt88:j_idt91").click()
        time.sleep(2)
        self.browser.switch_to.alert.accept()
        time.sleep(2)
        print(self.browser.find_element(by=By.ID,value="simple_result").text)
        time.sleep(1)
        self.browser.find_element(by=By.ID, value="j_idt88:j_idt93").click()
        time.sleep(2)
        self.browser.switch_to.alert.dismiss()
        time.sleep(2)
        print(self.browser.find_element(by=By.ID, value="result").text)
        time.sleep(1)
        self.browser.find_element(by=By.ID, value="j_idt88:j_idt104").click()
        time.sleep(2)
        self.browser.switch_to.alert.send_keys("FITA")
        self.browser.switch_to.alert.accept()
        time.sleep(2)
        print(self.browser.find_element(by=By.ID, value="confirm_result").text)
        time.sleep(2)
        self.browser.find_element(by=By.ID, value="j_idt88:j_idt95").click()
        time.sleep(2)
        WebDriverWait(self.browser, 20).until(EC.element_to_be_clickable((By.ID, "j_idt88:j_idt98")))
        self.browser.find_element(by=By.ID,value="j_idt88:j_idt98").click()
        time.sleep(10)

obj = AlertConcept()
obj.Alertimpl()