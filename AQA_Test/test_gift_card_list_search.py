from main_page import main_page
from log_in_page import log_in_page
from special_info import *

def test_gift_card_list_search(browser):

    open_main_page = main_page(browser)
    open_main_page.get_start_page()
    open_main_page.go_to_log_in_page()

    log_in_to_site = log_in_page(browser)
    log_in_to_site.log_in(local_login, password)

    click_gift_card_list = main_page(browser)
    click_gift_card_list.go_to_gift_list_page()
    assert "$100 Physical Gift Card" in browser.page_source