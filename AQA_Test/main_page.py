from base_app import base_page
from selenium.webdriver.common.by import By

class main_page_locators():

    locator_log_in = (By.CSS_SELECTOR, "a.ico-login")
    locator_register = (By.CSS_SELECTOR, "a.ico-register")
    locator_shopping_cart = (By.CSS_SELECTOR, "a.ico-cart")
    locator_wishlist = (By.CSS_SELECTOR, "div.header-links>ul>li>a[href='/wishlist']")
    locator_search_field = (By.CSS_SELECTOR, "input.search-box-text")
    locator_search_button = (By.CSS_SELECTOR, "input[type=submit]")

class go_to_register(base_page):

    def go_to_register_page(self):
        search_field = self.find_element(main_page_locators.locator_register)
        search_field.click()

class go_to_log_in(base_page):

    def go_to_log_in_page(self):
        search_field = self.find_element(main_page_locators.locator_log_in)
        search_field.click()





