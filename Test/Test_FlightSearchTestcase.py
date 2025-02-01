import time

import pytest
from pytest_bdd import scenarios, given, when, then
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

# Define the feature file
scenarios('C:\\Users\\DELL\\PycharmProjects\\FitaSeleniumPythonOctober\\FeatureFile\\test_feature.feature')

@pytest.fixture
def driver():
    browser = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))
    yield browser
    browser.quit()

@given('the user is on the login page')
def navigate_to_login(driver):
    driver.get("https://bstackdemo.com/signin")
    driver.maximize_window()

@when('the user enters valid credentials')
def enter_credentials(driver):
#select username

    driver.find_element(by=By.ID, value="username").click()

    driver.find_element(by=By.CSS_SELECTOR,value="#react-select-2-option-0-0").click()

    #select password

    driver.find_element(by=By.ID,value="password").click()

    driver.find_element(by=By.CSS_SELECTOR, value="#react-select-3-option-0-0").click()

    #click submit

    driver.find_element(By.ID,"login-btn").click()

@then('the user should be logged in')
def verify_login(driver):

    assert driver.title=="StackDemo"
    time.sleep(2)

@when('the user enters invalid credentials')
def invalid_login(driver):
    driver.find_element(by=By.ID, value="username").click()

    driver.find_element(by=By.CSS_SELECTOR, value="#react-select-2-option-0-0").click()
    #driver.find_element(by=By.ID, value="password").click()
    time.sleep(2)
    #driver.find_element(by=By.XPATH, value="(//*[@id='password']//div[1]//div//div)[1]").click()
    #time.sleep(2)
    mouse = ActionChains(driver)
    mouse.move_to_element(driver.find_element(by=By.XPATH,
                                                    value="(//*[@id='password']//div[1]//div//div)[1]")).click().send_keys("werererrewr").key_down(Keys.TAB).key_up(Keys.TAB).perform()

    #driver.find_element(by=By.XPATH,value="(//*[@id='password']//div[1]//div//div)[1]").send_keys("asdhvsdhvjhwfet")
    # click submit
    #driver.find_element(by=By.CSS_SELECTOR, value="#react-select-1-option-0-0").click()
    time.sleep(2)
    driver.find_element(By.ID, "login-btn").click()


@then('the user should not be logged in')
def invalid_login_assertion(driver):
    time.sleep(2)
    assert driver.find_element(by=By.XPATH,value="//h3[@class='api-error']").text == "Invalid Password"
    time.sleep(5)

