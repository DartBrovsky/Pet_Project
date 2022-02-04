from main_page import main_page
from log_in_page import log_in_page
from profile_page import profile_page
from special_info import *


def test_change_password(browser):
    open_main_page = main_page(browser)
    open_main_page.get_start_page()
    open_main_page.go_to_log_in_page()

    log_in_to_site = log_in_page(browser)
    log_in_to_site.log_in(local_login, password)

    go_to_profile = main_page(browser)
    go_to_profile.go_to_profile_page()

    changing_password = profile_page(browser)
    changing_password.click_on_changing_password()
    changing_password.change_password(password, new_pass)
    assert "Password was changed" in browser.page_source

    # control that the password was changed
    log_out = main_page(browser)
    log_out.log_out()

    open_main_page.go_to_log_in_page()
    log_in_to_site.log_in(local_login, new_pass)
    assert "look070907@gmail.com" in browser.page_source

    # return old password
    go_to_profile.go_to_profile_page()
    changing_password.click_on_changing_password()
    changing_password.change_password(new_pass, password)
    assert "Password was changed" in browser.page_source
















