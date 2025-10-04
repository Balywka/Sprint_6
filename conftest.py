import pytest
from selenium import webdriver
from Pages.main_page import MainPage
from Pages.order_page import OrderPage

@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()

@pytest.fixture
def main_page(driver):
    return MainPage(driver)

@pytest.fixture
def order_page(driver):
    return OrderPage(driver)