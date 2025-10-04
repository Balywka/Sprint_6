import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Locators.order_page_locator import OrderPageLocators  # ← исправлено имя!


class OrderPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    @allure.step('Заполнить поле "Имя"')
    def set_first_name(self, name):
        self.wait.until(EC.visibility_of_element_located(OrderPageLocators.NAME_INPUT)).send_keys(name)
        return self

    @allure.step('Заполнить поле "Фамилия"')
    def set_last_name(self, last_name):
        self.driver.find_element(*OrderPageLocators.LASTNAME_INPUT).send_keys(last_name)
        return self

    @allure.step('Заполнить поле "Адрес"')
    def set_address(self, address):
        self.driver.find_element(*OrderPageLocators.ADDRESS_INPUT).send_keys(address)
        return self

    @allure.step('Выбрать станцию метро: "{station}"')
    def set_metro(self, station):
        clean_station = station.strip()
        self.driver.find_element(*OrderPageLocators.METRO_INPUT).send_keys(clean_station)
        station_xpath = f"//li[@class='select-search__row' and normalize-space()='{clean_station}']"
        station_element = self.wait.until(EC.element_to_be_clickable((By.XPATH, station_xpath)))
        station_element.click()
        return self

    @allure.step('Заполнить поле "Телефон"')
    def set_phone(self, phone):
        self.driver.find_element(*OrderPageLocators.PHONE_INPUT).send_keys(phone)
        return self

    @allure.step('Нажать кнопку "Далее"')
    def click_next_button(self):
        self.driver.find_element(*OrderPageLocators.NEXT_BUTTON).click()
        return self

    @allure.step('Заполнить дату аренды: "{date}"')
    def set_rental_date(self, date):
        self.wait.until(EC.visibility_of_element_located(OrderPageLocators.DATE_INPUT)).send_keys(date)
        self.driver.find_element(By.TAG_NAME, "body").click()
        return self

    @allure.step('Выбрать срок аренды')
    def set_rental_duration(self):
        self.driver.find_element(By.TAG_NAME, "body").click()
        self.driver.find_element(*OrderPageLocators.RENTAL_PERIOD).click()
        options = self.driver.find_elements(*OrderPageLocators.RENTAL_OPTIONS)
        if options:
            options[0].click()
        return self

    @allure.step('Выбрать цвет самоката: чёрный')
    def set_color_black(self):
        self.driver.find_element(*OrderPageLocators.CHECKBOX_COLOR_BLACK).click()
        return self

    @allure.step('Добавить комментарий для курьера: "{comment}"')
    def set_comment(self, comment):
        if comment:
            self.driver.find_element(*OrderPageLocators.COMMENT_FIELD).send_keys(comment)
        return self

    @allure.step('Нажать кнопку "Заказать"')
    def click_order_button(self):
        self.driver.find_element(*OrderPageLocators.ORDER_BUTTON).click()
        return self

    @allure.step('Подтвердить заказ (нажать "Да")')
    def confirm_order(self):
        self.wait.until(EC.element_to_be_clickable(OrderPageLocators.CONFIRM_BUTTON)).click()
        return self

    @allure.step('Проверить, что появилось модальное окно "Заказ оформлен"')
    def is_order_success_displayed(self):
        success_element = self.wait.until(EC.visibility_of_element_located(OrderPageLocators.SUCCESS_MODAL))
        return success_element.is_displayed()

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