from .base_page import BasePage
from .locators import AuthLocators
from configs import auth_page_link
from selenium.common.exceptions import NoSuchElementException


class AuthPage(BasePage):
    def __init__(self, driver, url):
        super().__init__(driver, url)
        driver.get(auth_page_link)
        self.email_selector = driver.find_element(*AuthLocators.email_selector)
        self.phone_selector = driver.find_element(*AuthLocators.phone_selector)
        self.login_selector = driver.find_element(*AuthLocators.login_selector)
        self.login_input = driver.find_element(*AuthLocators.username_input)
        self.password_input = driver.find_element(*AuthLocators.password_input)
        self.submit_button = driver.find_element(*AuthLocators.submit_button)


    def choose_email(self):
        self.email_selector.click()

    def choose_phone(self):
        self.phone_selector.click()

    def choose_login(self):
        self.login_selector.click()

    def enter_login(self, login):
        self.login_input.send_keys(login)

    def enter_password(self, password):
        self.password_input.send_keys(password)

    def submit(self):
        self.submit_button.click()

    def check_error_message(self):
        try:
            self.driver.find_element(*AuthLocators.error_form_message)
        except NoSuchElementException:
            return False
        return True

    def check_error_phone(self):
        try:
            self.driver.find_element(*AuthLocators.error_phone_message)
        except NoSuchElementException:
            return False
        return True