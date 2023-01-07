import pytest

import configs
from pages.auth_page import AuthPage
import time
from configs import auth_page_link, email, password, phone, login


def test_auth_with_valide_mail(web_browser):
    """Тест аутентификации с валидной почтой и паролем."""
    auth_page = AuthPage(web_browser, auth_page_link)

    auth_page.choose_email()
    auth_page.enter_login(email)
    auth_page.enter_password(password)
    auth_page.submit()
    assert auth_page.get_relative_link() == "/account_b2c/page"

def test_auth_with_valide_phone(web_browser):
    """ Тест аутентификации с валидным номером телефона и паролем."""
    auth_page = AuthPage(web_browser, auth_page_link)

    auth_page.choose_phone()
    auth_page.enter_login(phone)
    auth_page.enter_password(password)
    auth_page.submit()
    assert auth_page.get_relative_link() == "/account_b2c/page"

def test_auth_with_valide_login(web_browser):
    """Тест аутентификации с валидными логином и паролем."""
    auth_page = AuthPage(web_browser, auth_page_link)

    auth_page.choose_login()
    auth_page.enter_login(login)
    auth_page.enter_password(password)
    auth_page.submit()
    assert auth_page.get_relative_link() == "/account_b2c/page"

def test_auth_autotab_to_mail(web_browser):
    """Тест, что система автоматически проверяет, что вход осуществляется с помощью почты"""
    auth_page = AuthPage(web_browser, auth_page_link)

    auth_page.enter_login(email)
    auth_page.enter_password(password)
    auth_page.submit()
    assert auth_page.get_relative_link() == "/account_b2c/page"


def test_auth_autotab_to_phone(web_browser):
    """Тест, что система автоматически проверяет, что вход осуществляется с помощью номера телефона"""
    auth_page = AuthPage(web_browser, auth_page_link)
    # Изначально меняем выбор на почту, так как по дефолту выбор стоит на входе по телефону.
    auth_page.choose_email()
    auth_page.enter_login(phone)
    auth_page.enter_password(password)
    auth_page.submit()
    assert auth_page.get_relative_link() == "/account_b2c/page"


def test_auth_autotab_to_login(web_browser):
    """Тест, что система автоматически проверяет, что вход осуществляется с помощью логина"""
    auth_page = AuthPage(web_browser, auth_page_link)

    auth_page.enter_login(login)
    auth_page.enter_password(password)
    auth_page.submit()
    assert auth_page.get_relative_link() == "/account_b2c/page"


@pytest.mark.parametrize("test_input_mail, output", [("sol19@mail.ru", True), ("sol19mail.ru", True),
                                                     (configs.mail_255, True), (configs.mail_1000, True)])
def test_auth_invalid_mail(web_browser, test_input_mail, output):
    """Негативные проверки аутентификации с невалидной почтой"""
    auth_page = AuthPage(web_browser, auth_page_link)
    auth_page.choose_email()
    auth_page.enter_login(test_input_mail)
    auth_page.enter_password(password)
    auth_page.submit()
    assert auth_page.check_error_message() == output


@pytest.mark.parametrize("test_input_login, output", [("asdasadqwf123", True), ("аывпаыкрцукр", True),
                                                      (configs.mail_255, True), (configs.mail_1000, True)])
def test_invalid_login(web_browser, test_input_login, output):
    """Негативные проверки аутентификации с невалидным логином"""
    auth_page = AuthPage(web_browser, auth_page_link)
    auth_page.choose_login()
    auth_page.enter_login(test_input_login)
    auth_page.enter_password(password)
    auth_page.submit()
    assert auth_page.check_error_message() == output


@pytest.mark.parametrize("test_input_phone, output", [(configs.phone_invalid, True), (configs.phone_str, True),
                                                      (configs.phone_kirr, True), (configs.phone_10_char, True)])
def test_phone_invalid(web_browser, test_input_phone, output):
    """Негативные проверки аутентификации с невалидным номером телефона"""
    auth_page = AuthPage(web_browser, auth_page_link)
    auth_page.choose_phone()
    auth_page.enter_login(test_input_phone)
    auth_page.enter_password(password)
    auth_page.submit()
    assert auth_page.check_error_phone() == output





