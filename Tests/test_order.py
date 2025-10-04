import allure
import pytest
from data import BASE_URL, ORDER_TEST_DATA

class TestOrder:

    @allure.title('Успешное оформление заказа через верхнюю кнопку')
    @pytest.mark.parametrize('name, last_name, address, metro, phone, date, comment', [ORDER_TEST_DATA[0]])
    def test_order_from_header(self, driver, main_page, order_page, name, last_name, address, metro, phone, date, comment):
        driver.get(BASE_URL)
        main_page.accept_cookies()
        main_page.click_order_button_header()
        order_page.fill_order_form(name, last_name, address, metro, phone, date, comment)
        assert order_page.is_order_success_displayed()

    @allure.title('Успешное оформление заказа через нижнюю кнопку')
    @pytest.mark.parametrize('name, last_name, address, metro, phone, date, comment', ORDER_TEST_DATA)
    def test_order_from_body(self, driver, main_page, order_page, name, last_name, address, metro, phone, date, comment):
        driver.get(BASE_URL)
        main_page.accept_cookies()
        main_page.click_order_button_body()
        order_page.fill_order_form(name, last_name, address, metro, phone, date, comment)
        assert order_page.is_order_success_displayed()