from selenium.webdriver.common.by import By


class LoginLocators:
    phone_num_field_locator = (By.XPATH, "//input[@id = 'username']")
    password_field_locator = (By.XPATH, "//input[@id = 'password']")
    log_in_button_locator = (By.XPATH, "//button[@id= 'kc-login']")
    register_bbtn_locator = (By.XPATH, "//*[@id='kc-register']")

    phone_num_tab_locator = (By.XPATH, "//*[@id='t-btn-tab-phone']")
    login_tab_locator = (By.XPATH, "//*[@id='t-btn-tab-login']")
    email_tab_locator = (By.XPATH, "//*[@id='t-btn-tab-mail']")
    ls_tab_locator = (By.XPATH, "//*[@id='t-btn-tab-ls']")

    login_form_locator = (By.XPATH, "//*[@id='page-right']/div")


class RegistrationLocators:
    name_field_locator = (By.XPATH, "//*[@id='page-right']/div/div[1]/div/form/div[1]/div[1]/div/input")
    last_name_field_locator = (By.XPATH, "//*[@id='page-right']/div/div[1]/div/form/div[1]/div[2]/div/input")
    region_downdrop_locator = (By.XPATH, "//*[@id='page-right']/div/div[1]/div/form/div[2]/div/div/input")
    email_or_phone_field_locator = (By.XPATH, "//*[@id='address']")
    password_field_locator = (By.XPATH, "//*[@id='password']")
    password_repeat_field_locator = (By.XPATH, "//*[@id='password-confirm']")
    register_bttn_locator = (By.XPATH, "//*[@id='page-right']/div/div[1]/div/form/button[1]")

    alaram_locator = (By.XPATH, "//*[@id='page-right']/div/div[1]/div/form/div[1]/div/div")
    alarm_text_locator = (By.XPATH, "//*[@id='page-right']/div/div[1]/div/form/div[1]/div/div/h2")


class SecurityPageLocators:
    lk_bttn_locator = (By.XPATH, "//*[@id='lk-btn']/span")


class LkLocators:
    events_bttn_locator = (By.XPATH, "//*[@href = '#feed']")


class EventsLocators:
    events_container_locator = (By.XPATH, "//*[@id='root']/div[7]/div[2]")

    filter_settings_locator = (By.CSS_SELECTOR, ".feed_open-settings-button")
    filter_settings_container_locator = (By.XPATH, "//*[@id='fade-screen']/div")
    filter_sections = (By.XPATH, "//*[@id='fade-screen']/div/div[2]/div/div")

    X_button_locator = (By.CSS_SELECTOR, "#fade-screen > div > div.sidebar-impl_header > svg")

    feed_card_container = (By.XPATH, "//*[@id='root']/div[7]/div[2]/div/div/div[2]")
    message_locator = (By.XPATH, "//*[@id='root']/div[7]/div[2]/div/div/div[2]/header")

    date_widget_locator = (By.XPATH, "//*[@id='root']/div[7]/div[2]/div/div/div[1]/div[2]/div[2]/div[2]")
    date_field_locator = (By.XPATH, "//div[contains(@class, 'date-picker_input')]/input")
