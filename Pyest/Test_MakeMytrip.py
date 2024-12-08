import time

from selenium import webdriver

from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
class Test_MakeMytrip():

    def test_OpenAndClose1(self):
        self.browser = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))
        self.browser.maximize_window()
        print("log in")
        # self.browser.implicitly_wait(60)
        self.browser.get("https://www.leafground.com/alert.xhtml")
        self.browser.quit()

    def test_OpenAndClose2(self):
        self.browser = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))
        self.browser.maximize_window()
        # self.browser.implicitly_wait(60)
        self.browser.get("https://www.leafground.com/alert.xhtml")
        self.browser.quit()