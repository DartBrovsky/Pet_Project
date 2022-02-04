from base_app import base_page
from selenium.webdriver.common.by import By

class register_page(base_page):

    locator_first_name_field = (By.CSS_SELECTOR, "input#FirstName")
    locator_last_name_field = (By.CSS_SELECTOR, "input#LastName")
    locator_email_field = (By.CSS_SELECTOR, "input#Email")
    locator_password_field = (By.CSS_SELECTOR, "input#Password")
    locator_confirm_password_field = (By.CSS_SELECTOR, "input#ConfirmPassword")
    locator_register_button = (By.CSS_SELECTOR, "input#register-button")

    def register(self, name, s_name, login, password):
        searh_field_1 = self.find_element(register_page.locator_first_name_field)
        searh_field_1.send_keys(name)

        searh_field_2 = self.find_element(register_page.locator_last_name_field)
        searh_field_2.send_keys(s_name)

        searh_field_3 = self.find_element(register_page.locator_email_field)
        searh_field_3.send_keys(login)

        searh_field_4 = self.find_element(register_page.locator_password_field)
        searh_field_4.send_keys(password)

        searh_field_5 = self.find_element(register_page.locator_confirm_password_field)
        searh_field_5.send_keys(password)

        searh_field_6 = self.find_element(register_page.locator_register_button)
        searh_field_6.click()
