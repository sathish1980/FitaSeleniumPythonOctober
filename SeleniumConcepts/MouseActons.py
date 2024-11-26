import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys

from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

class MouseActions():

    def MouseActionsimpl(self):
        self.browser = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))
        self.browser.maximize_window()
        #self.browser.implicitly_wait(60)
        self.browser.get("https://www.ebay.com/")
        mouse = ActionChains(self.browser)
        mouse.move_to_element(self.browser.find_element(by=By.XPATH,value="//*[@class='vl-flyout-nav__js-tab']//*[text()='Electronics']")).perform()
        time.sleep(2)
        mouse.move_to_element(self.browser.find_element(by=By.XPATH,value="//*[text()='Computers and tablets']")).click().perform()
        time.sleep(5)

    def MouseActionsimpl2(self):
        self.browser = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))
        self.browser.maximize_window()
        # self.browser.implicitly_wait(60)
        self.browser.get("https://www.facebook.com/")
        mouse = ActionChains(self.browser)
        mouse.move_to_element(self.browser.find_element(by=By.ID,
                                                        value="email")).send_keys("sathish").double_click().context_click().perform()

        time.sleep(5)

    def MouseActionsimpl3(self):
        self.browser = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))
        self.browser.maximize_window()
        # self.browser.implicitly_wait(60)
        self.browser.get("https://www.leafground.com/drag.xhtml")
        mouse = ActionChains(self.browser)
        mouse.move_to_element(self.browser.find_element(by=By.ID,
                                                        value="form:drag")).drag_and_drop(self.browser.find_element(by=By.ID,
                                                        value="form:drag"),self.browser.find_element(by=By.ID,
                                                        value="form:drop_content")).perform()
        time.sleep(5)

    def MouseActionsimpl4(self):
        self.browser = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))
        self.browser.maximize_window()
        # self.browser.implicitly_wait(60)
        self.browser.get("https://www.leafground.com/drag.xhtml")
        mouse = ActionChains(self.browser)
        mouse.move_to_element(self.browser.find_element(by=By.ID,
                                                        value="form:conpnl")).drag_and_drop_by_offset(self.browser.find_element(by=By.ID,
                                                        value="form:conpnl"),50,0).perform()
        mouse.move_to_element(self.browser.find_element(by=By.ID,
                                                       value="form:conpnl")).drag_and_drop_by_offset(self.browser.find_element(by=By.ID,
                                      value="form:conpnl"), -50, 0).perform()
        time.sleep(5)

obj = MouseActions()
obj.MouseActionsimpl4()