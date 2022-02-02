from main_page import go_to_log_in
from log_in_page import log_in
from main_page import go_to_search_result_page

def test_search_item(browser):

    log_in_page = go_to_log_in(browser)
    log_in_to_site = log_in(browser)
    search_result_page = go_to_search_result_page(browser)

    log_in_page.get_start_page()
    log_in_page.go_to_log_in_page()
    log_in_to_site.log_in()
    search_result_page.go_to_search_result_page()

    assert "800" in browser.page_source