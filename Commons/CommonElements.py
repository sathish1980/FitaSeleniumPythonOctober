from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class CommonElements():


    def ElementToBeClickable(self,browser,path):
        WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, path)))