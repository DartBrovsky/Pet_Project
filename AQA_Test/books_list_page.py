from base_app import BasePage
from selenium.webdriver.common.by import By

class BooksListPage(BasePage):

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
    locator_book_1 = (By.CSS_SELECTOR, "div.details>h2>a[href='/computing-and-internet']")
    locator_book_2 = (By.CSS_SELECTOR, "div.details>h2>a[href='/copy-of-computing-and-internet']")
    locator_book_3 = (By.CSS_SELECTOR, "div.details>h2>a[href='/fiction']")
    locator_book_4 = (By.CSS_SELECTOR, "div.details>h2>a[href='/fiction-ex']")
    locator_book_5 = (By.CSS_SELECTOR, "div.details>h2>a[href='/health']")
    locator_book_6 = (By.CSS_SELECTOR, "div.details>h2>a[href='/science']")

