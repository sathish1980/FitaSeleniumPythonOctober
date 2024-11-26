import time

from selenium import webdriver

from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class forstclass():
    browser = "null"

    def launch(self):
        self.browser = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))
        self.browser.maximize_window()


    def secondfunction(self):
        self.browser.get("https://www.facebook.com/")
        time.sleep(2)
        #self.browser.refresh()
        #self.browser.back()
        #self.browser.forward()
        # browser.quit()
        self.browser.find_element(by=By.ID,value="email").send_keys("sathish")
        self.browser.find_element(by=By.NAME, value="email").clear()
        #self.browser.find_element(by=By.CLASS_NAME, value="inputtext _55r1 _6luy").click()
        #self.browser.find_element(by=By.LINK_TEXT,value="Forgotten password?").click()
        #self.browser.find_element(by=By.PARTIAL_LINK_TEXT, value="ten p").click()
        self.browser.find_element(by=By.CSS_SELECTOR,value="input[class^=inputtext]").send_keys("FITA")

        self.browser.find_element(by=By.XPATH,value="//input[@name='email']").clear()
        self.browser.find_element(by=By.XPATH,value="//button[text()='Log in']").click()

        #Startswith --^
        #Endswith --$
        #contians -- *
        time.sleep(5)

obj = forstclass()
obj.launch()
obj.secondfunction()
