from main_page import main_page
from log_in_page import log_in_page
from search_result_page import search_result_page
from selected_item_page import selected_item_page
from shopping_cart_page import shopping_cart_page
from special_info import *

def test_remove_from_cart(browser):
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
    selected_item.go_to_shopping_cart_page()

    shopping_cart = shopping_cart_page(browser)
    shopping_cart.remove_item_from_shopping_cart()
    assert "Your Shopping Cart is empty!" in browser.page_source