from base_app import base_page
from selenium.webdriver.common.by import By

class forgot_password_locators():

    locator_forgot_password_field = (By.CSS_SELECTOR, "input.email")
    locator_forgot_password_button = (By.CSS_SELECTOR, "input[name=send-email]")

class forgot_my_password(base_page):

    def forgot_my_password(self):

        search_field_1 = self.find_element(forgot_password_locators.locator_forgot_password_field)
        search_field_1.send_keys("look070907@gmail.com")

        search_field_2 = self.find_element(forgot_password_locators.locator_forgot_password_button)
        search_field_2.click()
        