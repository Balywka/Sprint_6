import allure
import pytest
from Pages.main_page import MainPage
from Locators.main_page_locators import MainPageLocators
from data import expected_texts, BASE_URL
from urls import BASE_URL


class TestHomePageSamokat:

    @allure.title('Проверка раздела "Вопросы о важном"')
    @allure.description('Проверка появления соответствующего текста ответа при нажатии на каждый вопрос')
    @pytest.mark.parametrize('question_locator, answer_locator, expected_text', [
        (MainPageLocators.ACCORDION_BUTTON_FAQ_0, MainPageLocators.ANSWER_FAQ_0, expected_texts['faq0']),
        (MainPageLocators.ACCORDION_BUTTON_FAQ_1, MainPageLocators.ANSWER_FAQ_1, expected_texts['faq1']),
        (MainPageLocators.ACCORDION_BUTTON_FAQ_2, MainPageLocators.ANSWER_FAQ_2, expected_texts['faq2']),
        (MainPageLocators.ACCORDION_BUTTON_FAQ_3, MainPageLocators.ANSWER_FAQ_3, expected_texts['faq3']),
        (MainPageLocators.ACCORDION_BUTTON_FAQ_4, MainPageLocators.ANSWER_FAQ_4, expected_texts['faq4']),
        (MainPageLocators.ACCORDION_BUTTON_FAQ_5, MainPageLocators.ANSWER_FAQ_5, expected_texts['faq5']),
        (MainPageLocators.ACCORDION_BUTTON_FAQ_6, MainPageLocators.ANSWER_FAQ_6, expected_texts['faq6']),
        (MainPageLocators.ACCORDION_BUTTON_FAQ_7, MainPageLocators.ANSWER_FAQ_7, expected_texts['faq7']),
    ])
    def test_click_question_shows_answer_faq(self, driver,question_locator, answer_locator, expected_text):
        main_page = MainPage(driver)
        driver.get(BASE_URL)
        main_page.accept_cookies()
        main_page.scroll_to_faq()
        main_page.click_the_question(question_locator)
        actual_text = main_page.get_the_answer_text(answer_locator)
        assert actual_text == expected_text

    @allure.title('Проверка нажатия на логотип "Яндекс"')
    @allure.description('Проверка открытия страницы Яндекс.Дзен в новой вкладке')
    def test_clicking_yandex_logo_opens_dzen_page(self, driver):
        main_page = MainPage(driver)
        driver.get(BASE_URL)
        main_page.accept_cookies()
        main_page.click_logo_yandex_open_dzen_page()
        assert 'dzen.ru' in driver.current_url

    @allure.title('Проверка нажатия на логотип "Самокат"')
    @allure.description('Проверка перехода на главную страницу после нажатия на логотип "Самокат"')
    def test_click_logo_samokat_open_home_page(self, driver):
        main_page = MainPage(driver)
        driver.get(BASE_URL)
        main_page.accept_cookies()
        main_page.click_logo_open_home_page()
        assert driver.current_url == BASE_URL