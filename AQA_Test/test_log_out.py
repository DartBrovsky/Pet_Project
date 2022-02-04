from main_page import main_page
from log_in_page import log_in_page
from  special_info import *

def test_log_out(browser):
    open_main_page = main_page(browser)
    open_main_page.get_start_page()
    open_main_page.go_to_log_in_page()

    log_in_to_site = log_in_page(browser)
    log_in_to_site.log_in(local_login, password)

    log_out_from_site = main_page(browser)
    log_out_from_site.log_out()
    assert "Log in" in browser.page_source