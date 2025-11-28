import os

from .base_page import BasePage
from .locators import LoginLocators


class LoginPage(BasePage):
    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)
        self.driver = driver
        url = os.getenv("LOGIN_URL") or "https://b2c.passport.rt.ru/auth"
        driver.get(url)

    def input_phone_num(self, phone):
        self.driver.find_element(*LoginLocators.phone_num_field_locator).send_keys(phone)

    def input_password(self, password):
        self.driver.find_element(*LoginLocators.password_field_locator).send_keys(password)

    @property
    def log_in_bttn(self):
        return self.driver.find_element(*LoginLocators.log_in_button_locator)

    @property
    def registration_bttn(self):
        return self.driver.find_element(*LoginLocators.register_bbtn_locator)

    @property
    def phone_tab(self):
        return self.driver.find_element(*LoginLocators.phone_num_tab_locator)

    @property
    def login_tab(self):
        return self.driver.find_element(*LoginLocators.login_tab_locator)

    @property
    def email_tab(self):
        return self.driver.find_element(*LoginLocators.email_tab_locator)

    @property
    def licevoi_schet_tab(self):
        return self.driver.find_element(*LoginLocators.ls_tab_locator)

    @property
    def login_form(self):
        return self.driver.find_element(*LoginLocators.login_form_locator)
