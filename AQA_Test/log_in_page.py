from base_app import base_page
from selenium.webdriver.common.by import By

class log_in_page(base_page):

    locator_register_button = (By.CSS_SELECTOR, "input[value=Register]")
    locator_email_input_field = (By.CSS_SELECTOR, "input.email")
    locator_password_input_field = (By.CSS_SELECTOR, "input.password")
    locator_forgot_password_button = (By.CSS_SELECTOR, "a[href='/passwordrecovery']")
    locator_log_in_button = (By.CSS_SELECTOR, "input[class='button-1 login-button']")
    locator_remember_me_checkbox = (By.CSS_SELECTOR, "input#RememberMe")

    def log_in(self, login, password):

        search_field_1 = self.find_element(log_in_page.locator_email_input_field)
        search_field_1.send_keys(login)

        search_field_2 = self.find_element(log_in_page.locator_password_input_field)
        search_field_2.send_keys(password)

        search_field_3 = self.find_element(log_in_page.locator_log_in_button)
        search_field_3.click()

    def log_in_with_changed_password(self):

        search_field_1 = self.find_element(log_in_page.locator_email_input_field)
        search_field_1.send_keys("look070907@gmail.com")

        search_field_2 = self.find_element(log_in_page.locator_password_input_field)
        search_field_2.send_keys("dartdart")

        search_field_3 = self.find_element(log_in_page.locator_log_in_button)
        search_field_3.click()

    def go_to_forgot_password_page(self):

        search_field_1 = self.find_element(log_in_page.locator_forgot_password_button)
        search_field_1.click()