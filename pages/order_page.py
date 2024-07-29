import allure

from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):

    @allure.step('Заполнение поля Имя')
    def send_name_to_name_field(self, text):
        self.send_keys_to_field(OrderPageLocators.NAME_FIELD, text)

    @allure.step('Заполнение поля Фамилия')
    def send_last_name_to_last_name_field(self, text):
        self.send_keys_to_field(OrderPageLocators.LAST_NAME_FIELD, text)

    @allure.step('Заполнение поля Адрес')
    def send_address_to_address_field(self, text):
        self.send_keys_to_field(OrderPageLocators.ADDRESS_FIELD, text)

    @allure.step('Заполнение поля Станция метро')
    def send_metro_station_to_metro_station_field(self, text):
        self.click_button(OrderPageLocators.METRO_STATION_FIELD)
        self.send_keys_to_field(OrderPageLocators.METRO_STATION_FIELD, text)
        self.click_button(OrderPageLocators.METRO)

    @allure.step('Заполнение поля Номер телефона')
    def send_telephone_number_to_telephone_number_field(self, text):
        self.send_keys_to_field(OrderPageLocators.TELEPHONE_FIELD, text)

    @allure.step('Клик на кнопку Далее')
    def click_on_the_next_button(self):
        self.click_button(OrderPageLocators.NEXT_BUTTON)

    @allure.step('''Заполнение данных на странице "Для кого самокат"
                                 и переход на сл.страницу "Про аренду"''')
    def complete_filling_of_the_who_is_scooter_form(self, user):
        self.send_name_to_name_field(user[1])
        self.send_last_name_to_last_name_field(user[2])
        self.send_address_to_address_field(user[3])
        self.send_metro_station_to_metro_station_field(user[4])
        self.send_telephone_number_to_telephone_number_field(user[5])
        self.click_on_the_next_button()

    @allure.step('Заполнение поля Когда привезти заказ')
    def send_deliver_to_deliver_order_field(self, text):
        self.click_button(OrderPageLocators.DELIVER_ORDER_FIELD)
        self.send_keys_to_field(OrderPageLocators.DELIVER_ORDER_FIELD, text)

    @allure.step('Заполнение поля Срок аренды')
    def period_time(self):
        self.click_button(OrderPageLocators.RENT_PERIOD_FIELD)
        self.click_button(OrderPageLocators.RENT_PERIOD_THREE_DAYS)

    @allure.step('Заполнение поля Цвет самоката')
    def select_color_scooter(self):
        self.click_button(OrderPageLocators.BLACK_COLOR_SCOOTER_CHECK)

    @allure.step('Заполнение поля Комментарии для курьера')
    def send_comment_to_comment_field(self, text):
        self.send_keys_to_field(OrderPageLocators.COMMENT_FIELD, text)

    @allure.step('Клик на кнопку Заказать')
    def click_order_button(self):
        self.click_button(OrderPageLocators.ORDER_BUTTON)

    @allure.step('''Заполнение данных на странице "Про аренду"
                 и переход к подтверждению заказа''')
    def complete_filling_of_the_about_rent_form(self, text):
        self.send_deliver_to_deliver_order_field(text[6])
        self.period_time()
        self.select_color_scooter()
        self.send_comment_to_comment_field(text[7])
        self.click_order_button()

    @allure.step('Клик на кнопку Нет')
    def cancel_order_scooter(self):
        self.click_button(OrderPageLocators.NO_BUTTON)

    @allure.step('Клик на кнопку Да')
    def confirm_order_scooter(self):
        self.click_button(OrderPageLocators.YES_BUTTON)

    @allure.step('''Заполнение формы "Для кого самокат", "Про аренду" и подтверждение заказа''')
    def order_scooter_full_path(self, user):
        self.complete_filling_of_the_who_is_scooter_form(user)
        self.complete_filling_of_the_about_rent_form(user)
        self.confirm_order_scooter()

    @allure.step('Проверка отображения окна с текстом подтверждения заказа')
    def check_order_title(self):
        return self.find_and_wait_locator(OrderPageLocators.ORDER_PLACED_TEXT).is_displayed()