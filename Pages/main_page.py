import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Locators.main_page_locators import MainPageLocators

class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step('Принять cookies')
    def accept_cookies(self):
        self.wait.until(EC.element_to_be_clickable(MainPageLocators.ACCEPT_COOKIE_BUTTON)).click()

    @allure.step('Нажать кнопку "Заказать" в шапке')
    def click_order_button_header(self):
        self.wait.until(EC.element_to_be_clickable(MainPageLocators.ORDER_BUTTON_HEADER)).click()

    @allure.step('Нажать кнопку "Заказать" в теле страницы')
    def click_order_button_body(self):
        self.wait.until(EC.element_to_be_clickable(MainPageLocators.ORDER_BUTTON_BODY)).click()

    @allure.step('Прокрутить страницу к разделу "Вопросы о важном"')
    def scroll_to_faq(self):
        faq_section = self.wait.until(EC.presence_of_element_located(MainPageLocators.FAQ_SECTION))
        self.driver.execute_script("arguments[0].scrollIntoView();", faq_section)

    @allure.step('Нажать на вопрос FAQ')
    def click_the_question(self, question_locator):
        self.wait.until(EC.element_to_be_clickable(question_locator)).click()

    @allure.step('Получить текст ответа')
    def get_the_answer_text(self, answer_locator):
        return self.wait.until(EC.visibility_of_element_located(answer_locator)).text

    @allure.step('Нажать на логотип "Самокат"')
    def click_logo_open_home_page(self):
        self.wait.until(EC.element_to_be_clickable(MainPageLocators.LOGO_SCOOTER)).click()

    @allure.step('Нажатие на логотип "Яндекс"')
    def click_logo_yandex_open_dzen_page(self):
        self.wait.until(EC.element_to_be_clickable(MainPageLocators.LOGO_YANDEX)).click()
        self.wait.until(EC.number_of_windows_to_be(2))
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[-1])
        self.wait.until(EC.url_contains('dzen.ru'))