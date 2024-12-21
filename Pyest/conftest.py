import pytest


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

