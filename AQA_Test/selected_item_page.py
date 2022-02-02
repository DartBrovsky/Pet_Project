from base_app import base_page
from selenium.webdriver.common.by import By

class selected_item_page_locators():

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
    locator_processor_select_radio = (By.CSS_SELECTOR, "input[value='96']")
    locator_add_to_cart_button = (By.CSS_SELECTOR, "input#add-to-cart-button-75")
    locator_email_friend_button = (By.CSS_SELECTOR, "input[value^=Email]")
    locator_add_to_compaire_list_button = (By.CSS_SELECTOR, "input[value$=list]")
    locator_another_item_page_button = (By.CSS_SELECTOR, "a[href='/141-inch-laptop']")

class adding_to_cart(base_page):

    def adding_to_cart(self):

        search_field_1 = self.find_element(selected_item_page_locators.locator_processor_select_radio)
        search_field_1.click()

        search_field_2 = self.find_element(selected_item_page_locators.locator_add_to_cart_button)
        search_field_2.click()

class go_to_shopping_cart_page(base_page):

    def go_to_shopping_cart_page(self):

        search_field = self.find_element(selected_item_page_locators.locator_shopping_cart)
        search_field.click()