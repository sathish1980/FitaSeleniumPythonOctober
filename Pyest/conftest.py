import pytest
from selenium.webdriver.chrome import webdriver

from Utils import ExcelRead
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

@pytest.fixture()
def url_Data1():
    #return "https://www.makemytrip.com/"
    print('begining')
    yield
    print("close")

@pytest.fixture()
def url_Data():
    return "https://www.makemytrip.com/"

@pytest.fixture()
def flightSearch():
    return["BLR","MAA","25"]

@pytest.fixture()
def hotelsearch():
    return["Chennai","10","19"]

@pytest.fixture(params=[("Mumbai","15","19"),("Goa","20","29")])
def hotelsearchwithmultiple(request):
    return request.param

credential_excel_dic = [ExcelRead.Excel_Read.retrundicvalue("ValidFlight")]

@pytest.fixture(params=credential_excel_dic)
def flightdataFromExecl(request):
    return request.param

@pytest.fixture
def driver():
    browser = webdriver.ChromiumDriver(service=ChromeService(executable_path=ChromeDriverManager().install()))
    yield browser
    browser.quit()

