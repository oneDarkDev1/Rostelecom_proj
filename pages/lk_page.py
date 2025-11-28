import os

from .base_page import BasePage
from .locators import LkLocators


class LoginPage(BasePage):
    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)
        self.driver = driver
        url = os.getenv("LOGIN_URL") or "https://lk.rt.ru/#"
        driver.get(url)

    @property
    def events_bttn(self):
        return self.driver.find_element(*LkLocators.events_bttn_locator)
