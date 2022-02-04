from base_app import base_page
from selenium.webdriver.common.by import By

class shopping_cart_page(base_page):

    # Empty cart locators
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
    # Cart with computer item locators
    locator_simple_computer_item_button = (By.CSS_SELECTOR, "td.product>a[href='/simple-computer']")
    locator_edit_button = (By.CSS_SELECTOR, "a[href='/simple-computer?updatecartitemid=2213015']")
    locator_remove_checkbox = (By.CSS_SELECTOR, "input[name^=remove]")
    locator_update_cart_button = (By.CSS_SELECTOR, "input[name^=update]")
    locator_continue_shopping_button = (By.CSS_SELECTOR, "input[name^=continue]")
    locator_dicount_entry_field = (By.CSS_SELECTOR, "input[name^=discount]")
    locator_dicount_entry_button = (By.CSS_SELECTOR, "input[name^=applydiscount]")
    locator_giftcard_entry_field = (By.CSS_SELECTOR, "input[name^=gift]")
    locator_giftcard_entry_button = (By.CSS_SELECTOR, "input[name^=applygift]")

    def remove_item_from_shopping_cart(self):

        search_field_1 = self.find_element(shopping_cart_page.locator_remove_checkbox)
        search_field_1.click()

        search_field_2 = self.find_element(shopping_cart_page.locator_update_cart_button)
        search_field_2.click()