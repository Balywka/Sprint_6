import allure
from Locators.main_page_locators import MainPageLocators
from selenium.webdriver.support import expected_conditions as EC
from Pages.base_page import BasePage

class MainPage(BasePage):
    @allure.step('Принять cookies')
    def accept_cookies(self):
        self.click(MainPageLocators.ACCEPT_COOKIE_BUTTON)

    @allure.step('Нажать кнопку "Заказать" в шапке')
    def click_order_button_header(self):
        self.click(MainPageLocators.ORDER_BUTTON_HEADER)

    @allure.step('Нажать кнопку "Заказать" в теле страницы')
    def click_order_button_body(self):
        self.click(MainPageLocators.ORDER_BUTTON_BODY)

    @allure.step('Прокрутить страницу к разделу "Вопросы о важном"')
    def scroll_to_faq(self):
        self.scroll_to_element(MainPageLocators.FAQ_SECTION)

    @allure.step('Нажать на вопрос FAQ')
    def click_the_question(self, question_locator):
        self.click(question_locator)

    @allure.step('Получить текст ответа')
    def get_the_answer_text(self, answer_locator):
        return self.get_text(answer_locator)

    @allure.step('Нажать на логотип "Самокат"')
    def click_logo_open_home_page(self):
        self.click(MainPageLocators.LOGO_SCOOTER)

    @allure.step('Нажатие на логотип "Яндекс"')
    def click_logo_yandex_open_dzen_page(self):
        self.click(MainPageLocators.LOGO_YANDEX)
        self.switch_to_new_window()
        self.wait.until(EC.url_contains('dzen.ru'))