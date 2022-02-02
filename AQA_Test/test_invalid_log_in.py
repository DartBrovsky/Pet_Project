from main_page import go_to_log_in
from log_in_page import invalid_password_log_in


def test_ivalid_log_in(browser):
    log_in_page = go_to_log_in(browser)
    log_in_to_site = invalid_password_log_in(browser)
    log_in_page.get_start_page()
    log_in_page.go_to_log_in_page()
    log_in_to_site.invalid_password_log_in()

    assert "Login was unsuccessful. Please correct the errors and try again." in browser.page_source
