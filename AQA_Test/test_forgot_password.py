from main_page import go_to_log_in
from log_in_page import go_to_forgot_password_page
from forgot_password_page import forgot_my_password


def test_forgot_password(browser):
    log_in_page = go_to_log_in(browser)
    go_to_f_password_page = go_to_forgot_password_page(browser)
    forgot_password = forgot_my_password(browser)
    log_in_page.get_start_page()
    log_in_page.go_to_log_in_page()
    go_to_f_password_page.go_to_forgot_password_page()
    forgot_password.forgot_my_password()

    assert "Email with instructions has been sent to you." in browser.page_source
