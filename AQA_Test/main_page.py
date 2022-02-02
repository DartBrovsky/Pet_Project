from base_app import base_page
from selenium.webdriver.common.by import By

class main_page_locators():

    locator_log_in = (By.CSS_SELECTOR, "a.ico-login")
    locator_register = (By.CSS_SELECTOR, "a.ico-register")
    locator_shopping_cart = (By.CSS_SELECTOR, "a.ico-cart")
    locator_wishlist = (By.CSS_SELECTOR, "div.header-links>ul>li>a[href='/wishlist']")
    locator_search_field = (By.CSS_SELECTOR, "input.search-box-text")
    locator_search_button = (By.CSS_SELECTOR, "input[type=submit]")
    locator_log_out = (By.CSS_SELECTOR, "a[href='/logout']")
    locator_profile_button = (By.CSS_SELECTOR, "div.header-links>ul>li>a.account")
    locator_books_ref_button = (By.CSS_SELECTOR, "ul.top-menu>li:nth-child(1)>a")
    locator_computers_ref_button = (By.CSS_SELECTOR, "ul.top-menu>li:nth-child(2)>a")
    locator_electronics_ref_button = (By.CSS_SELECTOR, "ul.top-menu>li:nth-child(3)>a")
    locator_apparelshoes_ref_button = (By.CSS_SELECTOR, "ul.top-menu>li:nth-child(4)>a")
    locator_digitaldown_ref_button = (By.CSS_SELECTOR, "ul.top-menu>li:nth-child(5)>a")
    locator_jewelery_ref_button = (By.CSS_SELECTOR, "ul.top-menu>li:nth-child(6)>a")
    locator_giftcard_ref_button = (By.CSS_SELECTOR, "ul.top-menu>li:nth-child(7)>a")

class go_to_register(base_page):

    def go_to_register_page(self):
        search_field = self.find_element(main_page_locators.locator_register)
        search_field.click()

class go_to_log_in(base_page):

    def go_to_log_in_page(self):
        search_field = self.find_element(main_page_locators.locator_log_in)
        search_field.click()

class go_to_profile_page(base_page):

    def go_to_profile_page(self):

        search_field = self.find_element(main_page_locators.locator_profile_button)
        search_field.click()

class go_to_search_result_page(base_page):

    def go_to_search_result_page(self):

        search_field_1 = self.find_element(main_page_locators.locator_search_field)
        search_field_1.send_keys("Simple Computer")

        search_field_2 = self.find_element(main_page_locators.locator_search_button)
        search_field_2.click()





