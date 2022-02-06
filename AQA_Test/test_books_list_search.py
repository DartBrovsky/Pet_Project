from main_page import MainPage
from log_in_page import LogInPage
from special_info import *

def test_books_list_search(browser):

    open_main_page = MainPage(browser)
    open_main_page.get_start_page()
    open_main_page.go_to_log_in_page()

    log_in_to_site = LogInPage(browser)
    log_in_to_site.log_in(local_login, password)

    click_books_list = MainPage(browser)
    click_books_list.go_to_book_list_page()
    assert "Computing and Internet" in browser.page_source

