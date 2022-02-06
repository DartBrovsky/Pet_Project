from main_page import MainPage
from log_in_page import LogInPage
from special_info import *


def test_log_in(browser):

    main_page = MainPage(browser)
    main_page.get_start_page()
    main_page.go_to_log_in_page()

    log_in_to_site = LogInPage(browser)
    log_in_to_site.log_in(local_login, password)

    assert "Log out" in browser.page_source

