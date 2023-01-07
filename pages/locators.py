from selenium.webdriver.common.by import By

class AuthLocators:
    email_selector = (By.ID, "t-btn-tab-mail")
    phone_selector = (By.ID, "t-btn-tab-phone")
    login_selector = (By.ID, "t-btn-tab-login")
    submit_button = (By.ID, "kc-login")
    username_input = (By.ID, "username")
    password_input = (By.ID, "password")
    error_phone_message = (By.CSS_SELECTOR, "rt-input-container__meta rt-input-container__meta--error")
    error_form_message = (By.ID, "form-error-message")