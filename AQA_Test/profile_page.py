from base_app import base_page
from selenium.webdriver.common.by import By

class profile_page_locators():

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
    locator_customer_info_button = (By.CSS_SELECTOR, "div.listbox>ul>li>a[href='/customer/info']")
    locator_addresses_button = (By.CSS_SELECTOR, "div.listbox>ul>li>a[href='/customer/addresses']")
    locator_orders_button = (By.CSS_SELECTOR, "div.listbox>ul>li>a[href='/customer/orders']")
    locator_downloadable_products_button = (By.CSS_SELECTOR,
            "div.listbox>ul>li>a[href='/customer/downloadableproducts']")
    locator_back_in_stock_button = (By.CSS_SELECTOR,
            "div.listbox>ul>li>a[href='/customer/backinstocksubscriptions']")
    locator_reward_points_button = (By.CSS_SELECTOR, "div.listbox>ul>li>a[href='/customer/rewardpoints']")
    locator_change_password_button = (By.CSS_SELECTOR, "div.listbox>ul>li>a[href='/customer/changepassword']")
    # After click on locator_change_password_button
    locator_old_password_entry = (By.CSS_SELECTOR, "input[name^=Old]")
    locator_new_password_entry = (By.CSS_SELECTOR, "input[name^=New]")
    locator_confirm_password_entry = (By.CSS_SELECTOR, "input[name^=Confirm]")
    locator_change_password_confirm_button = (By.CSS_SELECTOR, "input[value^=Change]")

class click_on_changing_password(base_page):

    def click_on_changing_password(self):

        search_field = self.find_element(profile_page_locators.locator_change_password_button)
        search_field.click()

class change_password(base_page):

    def change_password(self):

        search_field_1 = self.find_element(profile_page_locators.locator_old_password_entry)
        search_field_1.send_keys("Dart_brovsky")

        search_field_2 = self.find_element(profile_page_locators.locator_new_password_entry)
        search_field_2.send_keys("dartdart")

        search_field_3 = self.find_element(profile_page_locators.locator_confirm_password_entry)
        search_field_3.send_keys("dartdart")

        search_field_4 = self.find_element(profile_page_locators.locator_change_password_confirm_button)
        search_field_4.click()

    # func for returning old password

    def return_old_password(self):
        search_field_1 = self.find_element(profile_page_locators.locator_old_password_entry)
        search_field_1.send_keys("dartdart")

        search_field_2 = self.find_element(profile_page_locators.locator_new_password_entry)
        search_field_2.send_keys("Dart_brovsky")

        search_field_3 = self.find_element(profile_page_locators.locator_confirm_password_entry)
        search_field_3.send_keys("Dart_brovsky")

        search_field_4 = self.find_element(profile_page_locators.locator_change_password_confirm_button)
        search_field_4.click()
