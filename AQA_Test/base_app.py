from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class base_page:

    def __init__(self, driver):
        self.driver = driver
        self.start_page_url =  "http://demowebshop.tricentis.com/"

    def find_element(self, locator, time=5):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can`t find element {locator}!")

    def find_elements(self, locator, time=5):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can`t find elements {locator}!")

    def get_start_page(self):
        return self.driver.get(self.start_page_url)