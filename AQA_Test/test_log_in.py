from main_page import go_to_log_in
from log_in_page import log_in


def test_log_in(browser):
    log_in_page = go_to_log_in(browser)
    log_in_to_site = log_in(browser)
    log_in_page.get_start_page()
    log_in_page.go_to_log_in_page()
    log_in_to_site.log_in()

    assert "look070907@gmail.com" in browser.page_source

