from main_page import MainPage
from log_in_page import LogInPage
from special_info import *

def test_search_item(browser):

    open_main_page = MainPage(browser)
    open_main_page.get_start_page()
    open_main_page.go_to_log_in_page()

    log_in_to_site = LogInPage(browser)
    log_in_to_site.log_in(local_login, password)

    search_result_page = MainPage(browser)
    search_result_page.go_to_search_result_page()

    assert "800" in browser.page_source