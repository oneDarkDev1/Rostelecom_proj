import pytest
from pages.events_page import EventsPage
from pages.locators import RegistrationLocators, SecurityPageLocators, LkLocators, EventsLocators
from pages.login_page import *
from pages.registration_page import RegistartionPage
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture()
def get_reg_page(selenium):
    auth_page = LoginPage(driver=selenium)
    auth_page.registration_bttn.click()

    return selenium


@pytest.fixture()
def login(selenium):
    auth_page = LoginPage(driver=selenium)
    wait = WebDriverWait(selenium, 8)

    auth_page.input_phone_num("9035371054")
    auth_page.input_password("U92vDEXU3z")

    wait.until(
        EC.element_to_be_clickable(LoginLocators.log_in_button_locator)
    )

    auth_page.log_in_bttn.click()

    wait.until(EC.url_contains("account_b2c/page"))
    return selenium


@pytest.fixture()
def get_feed_page(selenium):
    wait = WebDriverWait(selenium, 10)

    wait.until(
        EC.visibility_of_element_located(SecurityPageLocators.lk_bttn_locator)
    )
    selenium.find_element(*SecurityPageLocators.lk_bttn_locator).click()

    wait.until(
        EC.visibility_of_element_located(LkLocators.events_bttn_locator)
    )
    selenium.find_element(*LkLocators.events_bttn_locator).click()

    wait.until(EC.visibility_of_element_located(EventsLocators.events_container_locator))
    return selenium


@pytest.mark.parametrize("input", ["pineappleplay906@gmail.com", "rtkid_1763067038911", "123456789012"])
def test_tab_auto_switch_phone(selenium, input):
    auth_page = LoginPage(driver=selenium)

    assert "active" in auth_page.phone_tab.get_attribute("class")
    auth_page.input_phone_num(input)

    auth_page.login_form.click()

    should_be_email = "@" in input
    should_be_login = input.startswith("rtkid_")
    should_be_ls = len(input) == 12 and "+" not in input

    email_active = "active" in auth_page.email_tab.get_attribute("class")
    login_active = "active" in auth_page.login_tab.get_attribute("class")
    licevoi_schet_active = "active" in auth_page.licevoi_schet_tab.get_attribute("class")
    phone_active = "active" in auth_page.phone_tab.get_attribute("class")

    if should_be_email:
        assert email_active and (not login_active and not licevoi_schet_active and not phone_active)

    elif should_be_login:
        assert login_active and (not email_active and not licevoi_schet_active and not phone_active)

    elif should_be_ls:
        assert licevoi_schet_active and (not email_active and not login_active and not phone_active)


@pytest.mark.parametrize("input", ["rtkid_1763067038911", "123456789012", "+79035371054", "9035371054"])
def test_tab_auto_switch_email(selenium, input):
    auth_page = LoginPage(driver=selenium)

    auth_page.email_tab.click()
    auth_page.input_phone_num(input)
    auth_page.login_form.click()

    should_be_login = input.startswith("rtkid_")
    should_be_ls = len(input) == 12 and "+" not in input
    should_be_phone = len(input) == 12 and "+7" in input or len(input) == 10 and input.startswith("9")

    login_active = "active" in auth_page.login_tab.get_attribute("class")
    licevoi_schet_active = "active" in auth_page.licevoi_schet_tab.get_attribute("class")
    phone_active = "active" in auth_page.phone_tab.get_attribute("class")
    email_active = "active" in auth_page.email_tab.get_attribute("class")

    if should_be_login:
        assert login_active and (not email_active and not licevoi_schet_active and not phone_active)

    elif should_be_ls:
        assert licevoi_schet_active and (not email_active and not login_active and not phone_active)

    elif should_be_phone:
        assert phone_active and (not email_active and not login_active and not licevoi_schet_active)


@pytest.mark.parametrize("input", ["pineappleplay906@gmail.com", "123456789012", "+79035371054", "9035371054"])
def test_tab_auto_switch_login(selenium, input):
    auth_page = LoginPage(driver=selenium)

    auth_page.login_tab.click()
    auth_page.input_phone_num(input)
    auth_page.login_form.click()

    should_be_email = "@" in input
    should_be_ls = len(input) == 12 and "+" not in input
    should_be_phone = len(input) == 12 and "+7" in input or len(input) == 10 and input.startswith("9")

    login_active = "active" in auth_page.login_tab.get_attribute("class")
    licevoi_schet_active = "active" in auth_page.licevoi_schet_tab.get_attribute("class")
    phone_active = "active" in auth_page.phone_tab.get_attribute("class")
    email_active = "active" in auth_page.email_tab.get_attribute("class")

    if should_be_email:
        assert email_active and (not login_active and not licevoi_schet_active and not phone_active)

    elif should_be_ls:
        assert licevoi_schet_active and (not email_active and not login_active and not phone_active)

    elif should_be_phone:
        assert phone_active and (not email_active and not login_active and not licevoi_schet_active)


@pytest.mark.parametrize("input", ["pineappleplay906@gmail.com", "rtkid_1763067038911", "+79035371054", "9035371054"])
def test_tab_auto_switch_ls(selenium, input):
    auth_page = LoginPage(driver=selenium)

    auth_page.licevoi_schet_tab.click()
    auth_page.input_phone_num(input)
    auth_page.login_form.click()

    should_be_email = "@" in input
    should_be_phone = len(input) == 12 and "+7" in input or len(input) == 10 and input.startswith("9")
    should_be_login = input.startswith("rtkid_")

    login_active = "active" in auth_page.login_tab.get_attribute("class")
    licevoi_schet_active = "active" in auth_page.licevoi_schet_tab.get_attribute("class")
    phone_active = "active" in auth_page.phone_tab.get_attribute("class")
    email_active = "active" in auth_page.email_tab.get_attribute("class")

    if should_be_email:
        assert email_active and (not login_active and not licevoi_schet_active and not phone_active)

    elif should_be_phone:
        assert phone_active and (not email_active and not login_active and not licevoi_schet_active)

    elif should_be_login:
        assert login_active and (not email_active and not licevoi_schet_active and not phone_active)


@pytest.mark.parametrize("input", ["pineappleplay906@gmail.com", "rtkid_1763067038911", "+79035371054"])
def test_auth(selenium, input):
    auth_page = LoginPage(driver=selenium)
    wait = WebDriverWait(selenium, 8)

    auth_page.input_phone_num(input)
    auth_page.input_password("U92vDEXU3z")

    wait.until(
        EC.element_to_be_clickable(LoginLocators.log_in_button_locator)
    )

    auth_page.log_in_bttn.click()

    wait.until(EC.url_contains("account_b2c/page"))
    assert "account_b2c/page" in selenium.current_url


@pytest.mark.parametrize("input", ["pineappleplay906@gmail.com", "+79035371054"])
def test_registration_alarm(input, get_reg_page):
    driver = get_reg_page
    wait = WebDriverWait(driver, 8)
    wait.until(
        EC.url_contains("registration")
    )

    reg_page = RegistartionPage(driver=driver)
    reg_page.input_name("Иван")
    reg_page.input_last_name("Иванов")
    reg_page.choose_region("Москва")
    reg_page.input_adress(input)
    reg_page.input_password("U92vDEXu3z")
    reg_page.input_password_repeat("U92vDEXu3z")
    reg_page.reg_bttn_click()

    wait.until(
        EC.visibility_of_element_located(RegistrationLocators.alaram_locator)
    )
    assert driver.find_element(*RegistrationLocators.alarm_text_locator).text == "Учётная запись уже существует"


def test_filters_in_feed(login, get_feed_page):
    login
    driver = get_feed_page
    wait = WebDriverWait(driver, 8)

    events_page = EventsPage(driver)

    panel_selector = (
        ".feed_settings-container, "
        ".feed_settings-card, "
        "#fade-screen"
    )
    driver.execute_script("""
           return new Promise(resolve => setTimeout(resolve, 400));
       """)

    success = events_page.try_open_settings(panel_selector)

    assert success, "Settings panel did not open"

    num_of_sections = events_page.count_filter_sections
    for section_num in range(1, num_of_sections + 1):
        print(events_page.unclick_filters(section_num))
    events_page.X_button.click()

    wait.until(
        EC.visibility_of_element_located(EventsLocators.feed_card_container)
    )

    wait.until(
        EC.text_to_be_present_in_element(
            EventsLocators.message_locator,
            "События не найдены"
        )
    )
    assert events_page.no_events_message == "События не найдены"


def test_inexistent_date(login, get_feed_page):
    login
    driver = get_feed_page
    wait = WebDriverWait(driver, 8)

    events_page = EventsPage(driver)
    date_widget = events_page.date_widget
    date_widget.click()

    date = "12.06.2001-13.06.2001"
    date_field = events_page.date_field

    for ch in date:
        date_field.send_keys(ch)

    date_field.send_keys(Keys.ENTER)

    wait.until(
        EC.text_to_be_present_in_element(
            EventsLocators.message_locator,
            "События не найдены"
        )
    )
    assert events_page.no_events_message == "События не найдены"
