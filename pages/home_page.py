import allure

from locators.home_page_locators import (HomePageHeaderLocators,
                                         HomePageLocators)
from pages.base_page import BasePage


class HomePageHeader(BasePage):
    @allure.step('Клик по логотипу Яндекса')
    def yandex_logo_click(self):
        self.click_button(HomePageHeaderLocators.LOGO_YANDEX)

    @allure.step('Клик по логотипу Самоката')
    def scooter_logo_click(self):
        self.click_button(HomePageHeaderLocators.LOGO_SCOOTER)

    @allure.step('Клик по кнопке Заказать')
    def order_button_click(self):
        self.click_button(HomePageHeaderLocators.ORDER_BUTTON)

    @allure.step('Клик по кнопке Статус заказа')
    def status_order_click(self):
        self.click_button(HomePageHeaderLocators.ORDER_STATUS_BUTTON)

    @allure.step('Заполнение формы номера заказа')
    def send_number_order_to_track_field(self, number):
        self.status_order_click()
        self.send_keys_to_field(HomePageHeaderLocators.NUMBER_ORDER_FIELD, number)

    @allure.step('Нажатие на кнопку Go!')
    def go_button_click(self):
        self.click_button(HomePageHeaderLocators.GO_BUTTON)

    @allure.step('Заполнение формы номера заказа и клик на кнопку Go!')
    def check_order_status(self, number):
        self.status_order_click()
        self.send_number_order_to_track_field(number)
        self.go_button_click()

    @allure.step('Проверка отображения надписи - "Учебный проект"')
    def check_order_title(self):
        return self.find_and_wait_locator(HomePageHeaderLocators.HEADER_PAGE_TITLE).is_displayed()


class HomePage(BasePage):

    @allure.step('Принять куки')
    def accept_cookie_home_page(self):
        self.click_button(HomePageLocators.ACCEPT_COOKIES_BUTTON)

    @allure.step('Скролл и клик на кнопку Заказать')
    def scroll_and_click_on_the_order_button(self):
        self.scroll_to_locator(HomePageLocators.ORDER_BUTTON)
        self.click_button(HomePageLocators.ORDER_BUTTON)

    @allure.step('Переход к списку вопросов')
    def scroll_to_questions(self):
        self.scroll_to_locator(HomePageLocators.QUESTIONS_TITLE)

    @allure.step('Клик на вопрос')
    def click_question_button(self, question_button_locator):
        self.scroll_to_questions()
        self.click_button(question_button_locator)

    @allure.step('Получение текста вопроса')
    def get_text_question(self, question_button_locator, question_text_locator):
        self.click_question_button(question_button_locator)
        text_question = self.get_text_locator(question_text_locator)
        return text_question