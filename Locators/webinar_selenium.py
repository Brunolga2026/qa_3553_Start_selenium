import time

from selenium import webdriver
from selenium.webdriver.common.by import By

def create_driver():
    driver = webdriver.Chrome()
    driver.set_window_size(1920, 1000)
    driver.implicitly_wait(10)
    driver.set_page_load_timeout(10)
    driver.maximize_window()
    return driver

def pause(seconds):
    time.sleep(seconds)

def hide_footer(driver):
    driver.execute_script("document.querySelector('footer').style.display='none'")

def selectors_home_page_demo():
    driver = create_driver()
    try:
        driver.get("https://demoqa.com/")
        pause(5)

        footer = driver.find_element(By.TAG_NAME, "footer")
        print(footer.tag_name)

        link_elements = driver.find_element(By.CSS_SELECTOR, "a[href='/elements']")
        link_elements.click()

        pause(5)

        forms = driver.find_element(By.CSS_SELECTOR, )
    finally:
        driver.quit()

selectors_home_page_demo()