from main_page import go_to_register
from register_page import register


def test_register(browser):
    register_page = go_to_register(browser)
    do_register = register(browser)
    register_page.get_start_page()
    register_page.go_to_register_page()
    do_register.register()

    browser.implicitly_wait(5)

    assert "The specified email already exists" in browser.page_source



