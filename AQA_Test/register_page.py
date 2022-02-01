from base_app import base_page
from selenium.webdriver.common.by import By

class register_page_locators():

    locator_first_name_field = (By.CSS_SELECTOR, "input#FirstName")
    locator_last_name_field = (By.CSS_SELECTOR, "input#LastName")
    locator_email_field = (By.CSS_SELECTOR, "input#Email")
    locator_password_field = (By.CSS_SELECTOR, "input#Password")
    locator_confirm_password_field = (By.CSS_SELECTOR, "input#ConfirmPassword")
    locator_register_button = (By.CSS_SELECTOR, "input#register-button")

class register(base_page):

    def register(self):
        searh_field_1 = self.find_element(register_page_locators.locator_first_name_field)
        searh_field_1.send_keys("Dart")

        searh_field_2 = self.find_element(register_page_locators.locator_last_name_field)
        searh_field_2.send_keys("Brovsky")

        searh_field_3 = self.find_element(register_page_locators.locator_email_field)
        searh_field_3.send_keys("look070907@gmail.com")

        searh_field_4 = self.find_element(register_page_locators.locator_password_field)
        searh_field_4.send_keys("Dart_brovsky")

        searh_field_5 = self.find_element(register_page_locators.locator_confirm_password_field)
        searh_field_5.send_keys("Dart_brovsky")

        searh_field_6 = self.find_element(register_page_locators.locator_register_button)
        searh_field_6.click()