import time

from selenium import webdriver

from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class sync():

    def implict(self):
        self.browser = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))
        self.browser.maximize_window()
        #self.browser.implicitly_wait(60)
        self.browser.get("https://www.facebook.com/")
        self.browser.find_element(by=By.CSS_SELECTOR,value="[data-testid='open-registration-form-button']").click()
        WebDriverWait(self.browser, 20).until(EC.presence_of_element_located((By.NAME, "firstname")))

        self.browser.find_element(by=By.NAME,value="firstname").send_keys("sathishs")
        WebDriverWait(self.browser, 20).until(EC.presence_of_element_located((By.NAME, "lastname")))
        self.browser.find_element(by=By.NAME, value="lastname").send_keys("sathishs")
        WebDriverWait(self.browser, 20).until(EC.element_to_be_clickable((By.NAME, "websubmit")))
        self.browser.find_element(by=By.NAME, value="websubmit").click()
        time.sleep(5)

obj= sync()
obj.implict()
