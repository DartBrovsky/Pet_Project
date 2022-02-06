from main_page import MainPage
from log_in_page import LogInPage
from special_info import *

def test_gift_card_list_search(browser):

    open_main_page = MainPage(browser)
    open_main_page.get_start_page()
    open_main_page.go_to_log_in_page()

    log_in_to_site = LogInPage(browser)
    log_in_to_site.log_in(local_login, password)

    click_gift_card_list = MainPage(browser)
    click_gift_card_list.go_to_gift_list_page()
    assert "$100 Physical Gift Card" in browser.page_source