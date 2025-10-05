import allure
import pytest
from Pages.main_page import MainPage
from Pages.order_page import OrderPage
from data import ORDER_TEST_DATA
from urls import BASE_URL

class TestOrder:
    @allure.title('Успешное оформление заказа')
    @pytest.mark.parametrize('source', ['header', 'body'])
    @pytest.mark.parametrize('name, last_name, address, metro, phone, date, comment', ORDER_TEST_DATA)
    def test_order_success(self, driver, source, name, last_name, address, metro, phone, date, comment):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        driver.get(BASE_URL)
        main_page.accept_cookies()
        if source == 'header':
             main_page.click_order_button_header()
        else:
            main_page.click_order_button_body()
        order_page.fill_order_form(name, last_name, address, metro, phone, date, comment)
        assert order_page.is_order_success_displayed()