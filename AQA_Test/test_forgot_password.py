from main_page import MainPage
from log_in_page import LogInPage
from forgot_Password_page import ForgotPasswordPage
from special_info import *
from checking_email import EmailBox

def test_forgot_password(browser):
    open_main_page = MainPage(browser)
    open_main_page.get_start_page()
    open_main_page.go_to_log_in_page()

    log_in_to_site = LogInPage(browser)
    log_in_to_site.go_to_forgot_password_page()

    open_forgot_pass_page = ForgotPasswordPage(browser)
    open_forgot_pass_page.forgot_my_password(local_login)
    assert "Email with instructions has been sent to you." in browser.page_source

    checking_an_email = EmailBox()
    checking_an_email.check_an_email()