from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from .base_page import BasePage
from .locators import RegistrationLocators


class RegistartionPage(BasePage):
    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    REGION_INPUT = (By.XPATH, "//input[contains(@class,'rt-select__input')]")

    def input_name(self, name):
        self.driver.find_element(*RegistrationLocators.name_field_locator).send_keys(name)

    def input_last_name(self, last_name):
        self.driver.find_element(*RegistrationLocators.last_name_field_locator).send_keys(last_name)

    def input_region(self, region):
        self.driver.find_element(*RegistrationLocators.region_downdrop_locator).send_keys(region)

    def choose_region(self, region_name):
        wait = WebDriverWait(self.driver, 10)

        # Click the dropdown input field
        dropdown = wait.until(
            EC.element_to_be_clickable(RegistrationLocators.region_downdrop_locator)
        )
        dropdown.click()

        # Click the desired option
        option = self.driver.find_element(
            By.XPATH,
            "//section[@id='page-right']/div/div/div/form/div[2]/div[2]/div[2]/div/div"
        )
        option.click()

    def input_adress(self, adress):
        self.driver.find_element(*RegistrationLocators.email_or_phone_field_locator).send_keys(adress)

    def input_password(self, password):
        self.driver.find_element(*RegistrationLocators.password_field_locator).send_keys(password)

    def input_password_repeat(self, password):
        self.driver.find_element(*RegistrationLocators.password_repeat_field_locator).send_keys(password)

    def reg_bttn_click(self):
        self.driver.find_element(*RegistrationLocators.register_bttn_locator).click()
