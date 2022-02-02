from main_page import go_to_log_in
from log_in_page import log_in
from main_page import go_to_search_result_page
from search_result_page import go_to_selected_item_page
from selected_item_page import adding_to_cart
from selected_item_page import go_to_shopping_cart_page

def test_add_to_cart(browser):

    go_log_in =  go_to_log_in(browser)
    log_in_to_site = log_in(browser)
    doing_search = go_to_search_result_page(browser)
    selected_item = go_to_selected_item_page(browser)
    adding_cart = adding_to_cart(browser)
    checking_cart = go_to_shopping_cart_page(browser)

    go_log_in.get_start_page()
    go_log_in.go_to_log_in_page()
    log_in_to_site.log_in()
    doing_search.go_to_search_result_page()
    selected_item.go_to_selected_item_page()
    adding_cart.adding_to_cart()
    checking_cart.go_to_shopping_cart_page()

    assert "Simple Computer" in browser.page_source
