# Project Test Suite Documentation

This repository contains an automated test suite written in **Python** using **pytest** and **Selenium WebDriver**. The tests validate authentication workflows, registration form behavior, UI tab auto-switching logic, and event feed filtering for a web application.

## 📁 Project Structure
```
project/
├── tests/
│   └── test_auth_and_events.py
├── pages/
│   ├── login_page.py
│   ├── registration_page.py
│   ├── events_page.py
│   ├── locators.py
│   ├── base_page.py
│   
├── requirements.txt
└── README.md
```

## 🧪 Features Tested
### 🔐 Authentication
- Auto-switch between phone, email, login, and account-number tabs based on input format.
- Successful authentication for valid credentials.

### 📝 Registration
- Registration form validation and alarm message display for existing accounts.

### 🗂 Event Feed
- Opening and interacting with the filter settings panel.
- Clearing filters and validating that no events match the criteria.
- Entering a nonexistent date range and verifying the "No events found" message.

## ⚙️ Technologies Used
- **Python 3**
- **pytest**
- **Selenium WebDriver**
- **WebDriverWait** and `expected_conditions`

## 🔧 Configuration
This project uses pytest fixtures such as:
- `selenium` — provided by pytest-selenium for browser control
- `login` — logs into the account before running tests
- `get_reg_page` — navigates to the registration page
- `get_feed_page` — navigates to the events feed page

Ensure you have a valid WebDriver installed (ChromeDriver, GeckoDriver, etc.) and compatible browser version.

## 🧩 Test Logic Overview
### Intelligent Tab Switching
The tests validate that entering:
- an email (`@` present) activates the email tab
- a login (`rtkid_`) activates the login tab
- a personal account number (12 digits) activates the LS tab
- a phone number (10 digits or +7 format) activates the phone tab

### Registration Alert
The test checks that using an existing email or phone number triggers the message:
```
Учётная запись уже существует
```

### Event Filters
- Opens filter settings panel using JS and CSS selectors
- Unchecks all filters
- Confirms the UI displays "События не найдены"

### Invalid Date Search
- Inputs a date range in the date widget
- Confirms no matching events

## 🚀 Future Improvements
- Add CI/CD integration (GitHub Actions / GitLab)
- Add Allure reports
- Parameterize credentials via environment variables
- Add page object documentation

