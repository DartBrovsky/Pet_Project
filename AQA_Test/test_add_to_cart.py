from main_page import main_page
from log_in_page import log_in_page
from search_result_page import search_result_page
from selected_item_page import selected_item_page
from special_info import *

def test_add_to_cart(browser):
    open_main_page = main_page(browser)
    open_main_page.get_start_page()
    open_main_page.go_to_log_in_page()

    log_in_to_site = log_in_page(browser)
    log_in_to_site.log_in(local_login, password)

    search_item_result_page = main_page(browser)
    search_item_result_page.go_to_search_result_page()

    go_to_item_page = search_result_page(browser)
    go_to_item_page.go_to_selected_item_page()

    selected_item = selected_item_page(browser)
    selected_item.adding_to_cart()
    assert "Simple Computer" in browser.page_source
