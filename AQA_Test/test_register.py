from main_page import main_page
from register_page import register_page


def test_register(browser):
    open_main_page = main_page(browser)
    open_main_page.get_start_page()
    open_main_page.go_to_register_page()

    do_register = register_page(browser)
    do_register.register()

    assert "The specified email already exists" in browser.page_source



