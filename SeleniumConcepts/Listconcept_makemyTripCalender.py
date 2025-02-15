import time

from selenium import webdriver

from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

class ListConceptmakemytrip():


    browser= "";

    def browserlaunch(self):
        self.browser = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))
        self.browser.maximize_window()
        # self.browser.implicitly_wait(60)
        self.browser.get("https://www.makemytrip.com/")
        WebDriverWait(self.browser, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@data-cy='closeModal']")))
        self.browser.find_element(by=By.XPATH, value="//*[@data-cy='closeModal']").click()

    def fromdropdonw(self):
        WebDriverWait(self.browser, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@for='fromCity']")))
        self.browser.find_element(by=By.XPATH, value="//*[@for='fromCity']").click()

    def toDropdown(self):
        WebDriverWait(self.browser, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@for='toCity']")))
        self.browser.find_element(by=By.XPATH, value="//*[@for='toCity']").click()

    def listimpl1(self,expectedCountry):




        WebDriverWait(self.browser, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='react-autowhatever-1']//ul//li[last()]")))
        allElements  = self.browser.find_elements(by=By.XPATH,value="//*[@id='react-autowhatever-1']//ul//li")
        for eachelement in range(1,len(allElements)+1):
            actualCountry = self.browser.find_element(by=By.XPATH,value="//*[@id='react-autowhatever-1']//ul//li["+str(eachelement)+"]//div[starts-with(@class,'font14')]").text
            print(actualCountry)
            if expectedCountry == actualCountry:
                self.browser.find_element(by=By.XPATH,value="//*[@id='react-autowhatever-1']//ul//li[" + str(eachelement) + "]").click()
                break
        time.sleep(10)

    def CalenderSlection(self, expectedDate):
        allWeeks= self.browser.find_elements(by=By.XPATH,value="(//*[@class='DayPicker-wrapper']//div[@class='DayPicker-Month'])[last()]//div[@class='DayPicker-Body']//div[@class='DayPicker-Week']")
        for eachWeek in range(1, len(allWeeks) + 1):
            alldays =self.browser.find_elements(by=By.XPATH,
                                      value="((//*[@class='DayPicker-wrapper']//div[@class='DayPicker-Month'])[last()]//div[@class='DayPicker-Body']//div[@class='DayPicker-Week'])["+str(eachWeek)+"]//div[@class='DayPicker-Day']")
            for eachday in range(1, len(alldays) + 1):
                actualDate = self.browser.find_element(by=By.XPATH, value="(((//*[@class='DayPicker-wrapper']//div[@class='DayPicker-Month'])[last()]//div[@class='DayPicker-Body']//div[@class='DayPicker-Week'])[" + str(eachWeek) + "]//div[@class='DayPicker-Day'])["+str(eachday)+"]//p[1]").text
                if actualDate==expectedDate:
                    self.browser.find_element(by=By.XPATH,value="(((//*[@class='DayPicker-wrapper']//div[@class='DayPicker-Month'])[last()]//div[@class='DayPicker-Body']//div[@class='DayPicker-Week'])[" + str(eachWeek) + "]//div[@class='DayPicker-Day'])[" + str(eachday) + "]").click()
                    time.sleep(10)
                    return


obj = ListConceptmakemytrip()
obj.browserlaunch()
obj.fromdropdonw()
obj.listimpl1("PNQ")
obj.toDropdown()
obj.listimpl1("MAA")
obj.CalenderSlection("20")