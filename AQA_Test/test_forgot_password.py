from main_page import main_page
from log_in_page import log_in_page
from forgot_password_page import forgot_password_page
from special_info import *

def test_forgot_password(browser):
    open_main_page = main_page(browser)
    open_main_page.get_start_page()
    open_main_page.go_to_log_in_page()

    log_in_to_site = log_in_page(browser)
    log_in_to_site.go_to_forgot_password_page()

    open_forgot_pass_page = forgot_password_page(browser)
    open_forgot_pass_page.forgot_my_password(local_login)
    assert "Email with instructions has been sent to you." in browser.page_source
