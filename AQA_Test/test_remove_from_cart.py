from main_page import go_to_log_in
from log_in_page import log_in
from main_page import go_to_search_result_page
from search_result_page import go_to_selected_item_page
from selected_item_page import adding_to_cart
from selected_item_page import go_to_shopping_cart_page
from shopping_cart_page import remove_item_from_shopping_cart

def test_remove_from_cart(browser):

    go_log_in = go_to_log_in(browser)
    log_in_to_site = log_in(browser)
    doing_search = go_to_search_result_page(browser)
    selected_item = go_to_selected_item_page(browser)
    adding_cart = adding_to_cart(browser)
    checking_cart = go_to_shopping_cart_page(browser)
    remove_from_cart = remove_item_from_shopping_cart(browser)

    go_log_in.get_start_page()
    go_log_in.go_to_log_in_page()
    log_in_to_site.log_in()
    doing_search.go_to_search_result_page()
    selected_item.go_to_selected_item_page()
    adding_cart.adding_to_cart()
    checking_cart.go_to_shopping_cart_page()
    remove_from_cart.remove_item_from_shopping_cart()

    assert  "Your Shopping Cart is empty!" in browser.page_source