from pathlib import Path

from selenium import webdriver
from selenium.webdriver.common.by import By

html_file = Path(__file__).parent / "21.index.html"
page_url = html_file.as_uri()

driver = webdriver.Chrome()
# driver.get("https://telranedu.web.app/login")
#
# input("Press Enter to close the browser...")
# # driver.close()
# finally:
#
try:
    driver.get(page_url)

    # input("Press Enter to close the browser...")

# by tag
    button = driver.find_element(By.TAG_NAME, "button")
    button_1 = driver.find_element(By.CSS_SELECTOR, "button")
    print(button.tag_name)
    print(button.text)

    links = driver.find_elements(By.TAG_NAME, "a")
    for link in links:
        print(link.text)

    links = driver.find_elements(By.TAG_NAME, "a")
    links_1 = driver.find_element(By.CSS_SELECTOR,"a") # by tag name и by css selector почти одно и то же
    print(len(links))
    for link in links:
        print(link.text)


# by class
    container = driver.find_element(By.CLASS_NAME,"container") # БЕЗ ТОЧКИ ЭТО
    container_1 = driver.find_element(By.CSS_SELECTOR,".container") # ТОЧКА ПЕРЕД СЛОВОМ ТОЧКА ЭТО ЭЛЕМЕНТ КЛАССА

# by id

    nav = driver.find_element(By.ID,"nav")
    nav_1 = driver.find_element(By.CSS_SELECTOR, "#nav")

    print("NAV id: ", nav.tag_name)
    print("NAV id: ", nav_1.tag_name)

finally:
    driver.quit()