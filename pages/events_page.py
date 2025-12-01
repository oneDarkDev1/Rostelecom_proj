import time
import traceback

from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from .base_page import BasePage
from .locators import EventsLocators


class EventsPage(BasePage):
    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def get_settings_button(self):
        """Return settings button WebElement or None."""
        locator = EventsLocators.filter_settings_locator

        try:
            return self.wait.until(EC.element_to_be_clickable(locator))
        except TimeoutException:
            try:
                return self.wait.until(EC.presence_of_element_located(locator))
            except TimeoutException:
                return None

    def try_open_settings(
            self,
            panel_selector,
            btn_selector=".feed_open-settings-button",
            timeout=6
    ):
        driver = self.driver
        wait = WebDriverWait(driver, timeout)
        start = time.time()

        def panel_present():
            try:
                els = driver.find_elements(By.CSS_SELECTOR, panel_selector)
                return any(e.is_displayed() for e in els)
            except Exception:
                return False

        if panel_present():
            print("[try_open_settings] panel already open")
            return True

        try:
            btn = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, btn_selector))
            )
        except Exception as e:
            print("[try_open_settings] settings button not found:", e)
            return False

        def normal_click():
            try:
                btn.click()
                return True
            except:
                return False

        def js_click():
            try:
                driver.execute_script("arguments[0].click();", btn)
                return True
            except:
                return False

        strategies = [
            ("Normal click", normal_click),
            ("JS click", js_click)
        ]

        for name, action in strategies:
            try:
                print(f"[try_open_settings] trying: {name}")

                btn = driver.find_element(By.CSS_SELECTOR, btn_selector)
                driver.execute_script(
                    "arguments[0].scrollIntoView({block:'center'});",
                    btn
                )

                action()
                time.sleep(0.4)

                if panel_present():
                    print(f"[try_open_settings] success via {name}")
                    return True

                print(f"[try_open_settings] {name} did nothing")

            except Exception:
                print(f"[try_open_settings] exception in {name}:")
                traceback.print_exc()

        print("[try_open_settings] failed to open panel")
        return False

    def unclick_filters(self, section_num):
        i = 1

        while True:
            checkbox_xpath = (
                f"//*[@id='fade-screen']/div/div[2]/div/div[{section_num}]/div[{i}]"
                f"/div/input[@type='checkbox']"
            )

            try:
                checkbox = self.driver.find_element(By.XPATH, checkbox_xpath)
            except NoSuchElementException:
                break

            if checkbox.is_selected():
                checkbox.click()

            i += 1
    def click_filters(self, section_num):
        i = 1

        while True:
            checkbox_xpath = (
                f"//*[@id='fade-screen']/div/div[2]/div/div[{section_num}]/div[{i}]"
                f"/div/input[@type='checkbox']"
            )

            try:
                checkbox = self.driver.find_element(By.XPATH, checkbox_xpath)
            except NoSuchElementException:
                break

            if not checkbox.is_selected():
                checkbox.click()

            i += 1

    @property
    def count_filter_sections(self):
        return len(
            self.driver.find_elements(*EventsLocators.filter_sections)
        )

    @property
    def no_events_message(self):
        return self.driver.find_element(*EventsLocators.message_locator).text

    @property
    def X_button(self):
        while True:
            try:
                close_bttn = self.driver.find_element(*EventsLocators.X_button_locator)
                break
            except NoSuchElementException:
                continue
        return close_bttn

    @property
    def date_widget(self):
        self.wait.until(
            EC.visibility_of_element_located(EventsLocators.date_widget_locator)
        )
        widget = self.driver.find_element(*EventsLocators.date_widget_locator)
        return widget

    @property
    def date_field(self):
        return self.driver.find_element(*EventsLocators.date_field_locator)
