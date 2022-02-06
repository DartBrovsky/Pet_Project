from main_page import MainPage
from log_in_page import LogInPage
from special_info import *


def test_ivalid_log_in(browser):
    open_main_page = MainPage(browser)
    open_main_page.get_start_page()
    open_main_page.go_to_log_in_page()

    log_in_to_site = LogInPage(browser)
    log_in_to_site.log_in(local_login, invalid_password)

    assert "Login was unsuccessful. Please correct the errors and try again." in browser.page_source
