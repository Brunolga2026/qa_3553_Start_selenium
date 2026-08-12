import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "https://telranedu.web.app/login"

# заготовка под тесты, типа шаблон
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get(URL)

    yield driver #что сделать после теста, даже если failed

    driver.quit()

def test_login_page(driver):
    element = driver.find_element(By.NAME, "email")
    assert element.is_displayed()


def test_login_button_is_displayed(driver):
    button = driver.find_element(By.XPATH, "//button[text()='Login']")
    assert button.is_displayed()


def test_registration_button_is_displayed(driver):
    button_reg = driver.find_element(By.XPATH, "//button[text()='Registration']")
    assert button_reg.is_displayed()


def test_login_button_is_enabled(driver):
    button = driver.find_element(By.XPATH, "//button[text()='Login']")
    assert button.is_enabled()
