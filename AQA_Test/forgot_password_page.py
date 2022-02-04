from base_app import base_page
from selenium.webdriver.common.by import By

class forgot_password_page(base_page):

    locator_forgot_password_field = (By.CSS_SELECTOR, "input.email")
    locator_forgot_password_button = (By.CSS_SELECTOR, "input[name=send-email]")

    def forgot_my_password(self, login):

        search_field_1 = self.find_element(forgot_password_page.locator_forgot_password_field)
        search_field_1.send_keys(login)

        search_field_2 = self.find_element(forgot_password_page.locator_forgot_password_button)
        search_field_2.click()
        