from main_page import MainPage
from log_in_page import LogInPage
from search_result_page import SearchResultPage
from selected_item_page import SelectedItemPage
from special_info import *

def test_add_to_cart(browser):
    open_main_page = MainPage(browser)
    open_main_page.get_start_page()
    open_main_page.go_to_log_in_page()

    log_in_to_site = LogInPage(browser)
    log_in_to_site.log_in(local_login, password)

    search_item_result_page = MainPage(browser)
    search_item_result_page.go_to_search_result_page()

    go_to_item_page = SearchResultPage(browser)
    go_to_item_page.go_to_selected_item_page()

    selected_item = SelectedItemPage(browser)
    selected_item.adding_to_cart()
    assert "Simple Computer" in browser.page_source
