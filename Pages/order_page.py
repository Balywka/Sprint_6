import allure
from selenium.webdriver.common.by import By
from Pages.base_page import BasePage
from Locators.order_page_locator import OrderPageLocators  # ← исправлено имя!


class OrderPage(BasePage):
    @allure.step('Заполнить поле "Имя"')
    def set_first_name(self, name):
        self.send_keys(OrderPageLocators.NAME_INPUT, name)
        return self

    @allure.step('Заполнить поле "Фамилия"')
    def set_last_name(self, last_name):
        self.send_keys(OrderPageLocators.LASTNAME_INPUT, last_name)
        return self

    @allure.step('Заполнить поле "Адрес"')
    def set_address(self, address):
        self.send_keys(OrderPageLocators.ADDRESS_INPUT, address)
        return self

    @allure.step('Выбрать станцию метро: "{station}"')
    def set_metro(self, station):
        clean_station = station.strip()
        self.send_keys(OrderPageLocators.METRO_INPUT, clean_station)
        station_xpath = f"//li[@class='select-search__row' and normalize-space()='{clean_station}']"
        self.click((By.XPATH, station_xpath))
        return self

    @allure.step('Заполнить поле "Телефон"')
    def set_phone(self, phone):
        self.send_keys(OrderPageLocators.PHONE_INPUT, phone)
        return self

    @allure.step('Нажать кнопку "Далее"')
    def click_next_button(self):
        self.click(OrderPageLocators.NEXT_BUTTON)
        return self

    @allure.step('Заполнить дату аренды: "{date}"')
    def set_rental_date(self, date):
        self.send_keys(OrderPageLocators.DATE_INPUT, date)
        self.driver.find_element(By.TAG_NAME, "body").click()
        return self

    @allure.step('Выбрать срок аренды')
    def set_rental_duration(self):
        self.click(OrderPageLocators.RENTAL_PERIOD)
        options = self.driver.find_elements(*OrderPageLocators.RENTAL_OPTIONS)
        if options:
            options[0].click()
        return self

    @allure.step('Выбрать цвет самоката: чёрный')
    def set_color_black(self):
        self.click(OrderPageLocators.CHECKBOX_COLOR_BLACK)
        return self

    @allure.step('Добавить комментарий для курьера: "{comment}"')
    def set_comment(self, comment):
        if comment:
            self.send_keys(OrderPageLocators.COMMENT_FIELD, comment)
        return self

    @allure.step('Нажать кнопку "Заказать"')
    def click_order_button(self):
        self.click(OrderPageLocators.ORDER_BUTTON)
        return self

    @allure.step('Подтвердить заказ (нажать "Да")')
    def confirm_order(self):
        self.click(OrderPageLocators.CONFIRM_BUTTON)
        return self

    @allure.step('Проверить, что появилось модальное окно "Заказ оформлен"')
    def is_order_success_displayed(self):
        return self.find_element(OrderPageLocators.SUCCESS_MODAL).is_displayed()

    @allure.step('Заполнить всю форму заказа')
    def fill_order_form(self, name, last_name, address, metro, phone, date, comment=""):
        (
            self.set_first_name(name)
                .set_last_name(last_name)
                .set_address(address)
                .set_metro(metro)
                .set_phone(phone)
                .click_next_button()
                .set_rental_date(date)
                .set_rental_duration()
                .set_color_black()
                .set_comment(comment)
                .click_order_button()
                .confirm_order()
        )
        return self