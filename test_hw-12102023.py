import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "https://anc.ua/"

@pytest.fixture(scope="class") # на весь клас
def browser():
    print("\nstart browser for test suite..")
    browser = webdriver.Chrome()
    return browser

@pytest.fixture(autouse=True) # в кінці кожного тесту в класі
def print_smiling_faces():
    yield
    print('\nbutton or element is OK')

@pytest.fixture(scope="class") # на весь клас
def teardown_class(self):
    yield
    print("\nquit browser for test suite..")
    self.browser.quit()

class TestAncheadermenu():
    def test_img_anc(self, browser):
        browser.get(link)
        browser.find_element(By.XPATH, "//img[@src='https://storage.googleapis.com/static-storage/logo.svg']")

    def test_catalog_menu_anc(self, browser):
        browser.get(link)
        browser.find_element(By.XPATH, "//button[@class='button button-yellow-light text-size-16 weight-600 padding-10']")

    def test_search_anc(self, browser):
        browser.get(link)
        browser.find_element(By.XPATH, "//input[@class='input-search']")

    def test_history_anc(self, browser):
        browser.get(link)
        browser.find_element(By.XPATH, "//a[@href='/profile/history']")

    def test_favorite_anc(self, browser):
        browser.get(link)
        browser.find_element(By.XPATH, "//a[@href='/profile/favorites']")

    def test_user_anc(self, browser):
        browser.get(link)
        browser.find_element(By.XPATH, "//div[@class='row column v-center gap-5']")

    def test_cart_anc(self, browser):
        browser.get(link)
        browser.find_element(By.XPATH, "//a[@title='Кошик']")


#pytest -s test_hw-12102023.py


