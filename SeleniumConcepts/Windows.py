import time

from selenium import webdriver

from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


class WindowsConcept():

    def Windowimpl(self):
        self.browser = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))
        self.browser.maximize_window()
        # self.browser.implicitly_wait(60)
        self.browser.get("https://leafground.com/window.xhtml")
        parent_window =self.browser.current_window_handle # get current window name

        print(parent_window)
        self.browser.find_element(by=By.ID,value="j_idt88:new").click()
        allwindows = self.browser.window_handles # get all windows name
        for eachWindow in allwindows: # iterate in to all windows
            if parent_window!=eachWindow:
                self.browser.switch_to.window(eachWindow) # switching in to respective  window
                elementExist = self.browser.find_elements(by=By.ID,value="menuform:j_idt40")
                if len(elementExist) > 0 : # ensuring the element exist in the respective window
                    self.browser.find_element(by=By.ID, value="menuform:j_idt40").click()
                    self.browser.find_element(by=By.ID,value="menuform:m_input").click()
                    self.browser.find_element(by=By.ID,value="j_idt88:name").send_keys("FITA")
                    self.browser.close()
                    self.browser.switch_to.window(parent_window) # switch back to parent window
                    break;
                #self.browser.switch_to.window(parent_window)
        time.sleep(10)


obj = WindowsConcept()
obj.Windowimpl()
