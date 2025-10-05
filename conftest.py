import pytest
from selenium import webdriver
from Pages.main_page import MainPage
from Pages.order_page import OrderPage

@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()