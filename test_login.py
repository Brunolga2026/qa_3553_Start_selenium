from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "https://telranedu.web.app/login"

def test_login_page():
    driver = webdriver.Chrome()

    try:
        driver.get(URL)

        element = driver.find_element(By.NAME, "email")
        assert element.is_displayed()

    finally:
        driver.quit()

def test_login_button_is_displayed():
    driver = webdriver.Chrome()

    try:
        driver.get(URL)

        button = driver.find_element(By.XPATH, "//button[text()='Login']")
        assert button.is_displayed()

    finally:
        driver.quit()


def test_registration_button_is_displayed():
    driver = webdriver.Chrome()

    try:
        driver.get(URL)

        button_reg = driver.find_element(By.XPATH, "//button[text()='Registration']")
        assert button_reg.is_displayed()

    finally:
        driver.quit()

# проверка, что кнопка кликабельная
def test_login_button_is_enabled():
    driver = webdriver.Chrome()

    try:
        driver.get(URL)

        button = driver.find_element(By.XPATH, "//button[text()='Login']")
        assert button.is_enabled()

    finally:
        driver.quit()