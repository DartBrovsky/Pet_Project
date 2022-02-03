from main_page import main_page
from log_in_page import log_in_page


def test_ivalid_log_in(browser):
    open_main_page = main_page(browser)
    open_main_page.get_start_page()
    open_main_page.go_to_log_in_page()

    log_in_to_site = log_in_page(browser)
    local_login = "look070907@gmail.com"
    invalid_password = "dart"
    log_in_to_site.log_in(local_login, invalid_password)

    assert "Login was unsuccessful. Please correct the errors and try again." in browser.page_source
