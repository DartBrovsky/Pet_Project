from base_app import base_page
from selenium.webdriver.common.by import By

class search_result_page(base_page):

    locator_simple_computer_search_button = (By.CSS_SELECTOR, "h2.product-title>a[href='/simple-computer']")
    locator_computer_add_to_cart_button = (By.CSS_SELECTOR, "input[value^=Add]")
    locator_log_out = (By.CSS_SELECTOR, "a[href='/logout']")
    locator_profile_button = (By.CSS_SELECTOR, "div.header-links>ul>li>a.account")
    locator_shopping_cart = (By.CSS_SELECTOR, "a.ico-cart")
    locator_wishlist = (By.CSS_SELECTOR, "div.header-links>ul>li>a[href='/wishlist']")
    locator_search_field = (By.CSS_SELECTOR, "input.search-box-text")
    locator_search_button = (By.CSS_SELECTOR, "input[type=submit]")
    locator_books_ref_button = (By.CSS_SELECTOR, "ul.top-menu>li:nth-child(1)>a")
    locator_computers_ref_button = (By.CSS_SELECTOR, "ul.top-menu>li:nth-child(2)>a")
    locator_electronics_ref_button = (By.CSS_SELECTOR, "ul.top-menu>li:nth-child(3)>a")
    locator_apparelshoes_ref_button = (By.CSS_SELECTOR, "ul.top-menu>li:nth-child(4)>a")
    locator_digitaldown_ref_button = (By.CSS_SELECTOR, "ul.top-menu>li:nth-child(5)>a")
    locator_jewelery_ref_button = (By.CSS_SELECTOR, "ul.top-menu>li:nth-child(6)>a")
    locator_giftcard_ref_button = (By.CSS_SELECTOR, "ul.top-menu>li:nth-child(7)>a")

    def go_to_selected_item_page(self):

        search_field = self.find_element(search_result_page.locator_simple_computer_search_button)
        search_field.click()