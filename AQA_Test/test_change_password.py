from main_page import go_to_log_in
from log_in_page import log_in
from main_page import go_to_profile_page
from main_page import log_out
from profile_page import click_on_changing_password
from profile_page import change_password
from log_in_page import log_in_with_changed_password


def test_change_password(browser):

    log_in_page = go_to_log_in(browser)
    log_in_to_site = log_in(browser)
    go_to_profile = go_to_profile_page(browser)
    click_on_changing_of_password = click_on_changing_password(browser)
    change_my_password = change_password(browser)

    log_in_page.get_start_page()
    log_in_page.go_to_log_in_page()
    log_in_to_site.log_in()
    go_to_profile.go_to_profile_page()
    click_on_changing_of_password.click_on_changing_password()
    change_my_password.change_password()

    assert "Password was changed" in browser.page_source

    # control that the password was changed

    loging_out = log_out(browser)

    loging_out.log_out()
    log_in_page.go_to_log_in_page()

    log_in_with_new_password = log_in_with_changed_password(browser)
    log_in_with_new_password.log_in_with_changed_password()

    assert "look070907@gmail.com" in browser.page_source

    # return old password

    go_to_profile.go_to_profile_page()
    click_on_changing_of_password.click_on_changing_password()

    return_old_password = change_password(browser)
    return_old_password.return_old_password()

    assert "Password was changed" in browser.page_source
















