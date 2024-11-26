import time

from selenium import webdriver

from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

class Dropdown():

    def dropdownimpl(self):
        self.browser = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))
        self.browser.maximize_window()
        #self.browser.implicitly_wait(60)
        self.browser.get("https://www.leafground.com/select.xhtml")
        automation_Tool = Select(self.browser.find_element(by=By.CLASS_NAME,value="ui-selectonemenu"))
        automation_Tool.select_by_index(2)
        time.sleep(2)
        automation_Tool.select_by_visible_text("Cypress")
        time.sleep(2)
        #automation_Tool.select_by_value()
        print(automation_Tool.is_multiple)

obj = Dropdown()
obj.dropdownimpl()