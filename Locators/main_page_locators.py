from selenium.webdriver.common.by import By


class MainPageLocators:
    # Кнопки "Заказать"
    ORDER_BUTTON_HEADER = (By.CLASS_NAME, "Button_Button__ra12g") # В шапке
    ORDER_BUTTON_BODY = (By.CLASS_NAME, "Button_Middle__1CSJM")   # В теле

    # Логотипы
    LOGO_SCOOTER = (By.XPATH, "//img[@alt='Scooter']")
    LOGO_YANDEX = (By.XPATH, "//img[@alt='Yandex']")

    # Куки
    ACCEPT_COOKIE_BUTTON = (By.ID, "rcc-confirm-button")

    # FAQ — вопросы
    ACCORDION_BUTTON_FAQ_0 = (By.ID, "accordion__heading-0")
    ACCORDION_BUTTON_FAQ_1 = (By.ID, "accordion__heading-1")
    ACCORDION_BUTTON_FAQ_2 = (By.ID, "accordion__heading-2")
    ACCORDION_BUTTON_FAQ_3 = (By.ID, "accordion__heading-3")
    ACCORDION_BUTTON_FAQ_4 = (By.ID, "accordion__heading-4")
    ACCORDION_BUTTON_FAQ_5 = (By.ID, "accordion__heading-5")
    ACCORDION_BUTTON_FAQ_6 = (By.ID, "accordion__heading-6")
    ACCORDION_BUTTON_FAQ_7 = (By.ID, "accordion__heading-7")

    # FAQ — ответы
    ANSWER_FAQ_0 = (By.ID, "accordion__panel-0")
    ANSWER_FAQ_1 = (By.ID, "accordion__panel-1")
    ANSWER_FAQ_2 = (By.ID, "accordion__panel-2")
    ANSWER_FAQ_3 = (By.ID, "accordion__panel-3")
    ANSWER_FAQ_4 = (By.ID, "accordion__panel-4")
    ANSWER_FAQ_5 = (By.ID, "accordion__panel-5")
    ANSWER_FAQ_6 = (By.ID, "accordion__panel-6")
    ANSWER_FAQ_7 = (By.ID, "accordion__panel-7")

    # Элемент для скролла к FAQ
    FAQ_SECTION = (By.XPATH, "//div[text()='Вопросы о важном']")