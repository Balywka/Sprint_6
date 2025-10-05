import allure
import pytest
from itertools import product
from Pages.main_page import MainPage
from Pages.order_page import OrderPage
from Locators.main_page_locators import MainPageLocators
from data import ORDER_TEST_DATA
from urls import BASE_URL

class TestOrder:
    @allure.title('Успешное оформление заказа')
    @pytest.mark.parametrize('order_button_locator', [
        MainPageLocators.ORDER_BUTTON_HEADER,
        MainPageLocators.ORDER_BUTTON_BODY,
    ], ids=['header', 'body'])
    def test_order_success(self, driver, order_button_locator):
        name, last_name, address, metro, phone, date, comment = ORDER_TEST_DATA[0]
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        main_page.open(BASE_URL)
        main_page.accept_cookies()
        main_page.click_order_button_by_locator(order_button_locator)
        order_page.fill_order_form(name, last_name, address, metro, phone, date, comment)
        assert order_page.is_order_success_displayed()