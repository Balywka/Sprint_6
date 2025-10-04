from selenium.webdriver.common.by import By


class OrderPageLocators:
    # Шаг 1: личные данные
    NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
    LASTNAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_INPUT = (By.XPATH, "//input[@placeholder='* Станция метро']")
    METRO_OPTIONS_LIST = (By.XPATH, "//li[@class='select-search__row']")
    PHONE_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")

    # Шаг 2: детали аренды
    DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENTAL_PERIOD = (By.XPATH, "//div[text()='* Срок аренды']")
    RENTAL_OPTIONS = (By.XPATH, "//div[@class='Dropdown-option']")
    CHECKBOX_COLOR_BLACK = (By.ID, "black")
    COMMENT_FIELD = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")

    # Подтверждение
    ORDER_BUTTON = (By.XPATH, '//button[@class="Button_Button__ra12g Button_Middle__1CSJM" and text()="Заказать"]')
    CONFIRM_BUTTON = (By.XPATH, "//button[contains(text(), 'Да')]")

    # Успех
    SUCCESS_MODAL = (By.XPATH, "//div[text()='Заказ оформлен']")