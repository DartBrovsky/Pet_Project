from main_page import MainPage
from register_page import RegisterPage
from special_info import *


def test_register(browser):
    open_main_page = MainPage(browser)
    open_main_page.get_start_page()
    open_main_page.go_to_register_page()

    do_register = RegisterPage(browser)
    do_register.register(first_name, second_name, local_login, password)

    assert "The specified email already exists" in browser.page_source



