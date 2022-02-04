import pytest
from selenium import webdriver

@pytest.fixture()
def browser():
    driver = webdriver.Chrome("/Users/dart_brovsky/PycharmProjects/Pet_Project/chromedriver")
    yield driver
    driver.quit()
