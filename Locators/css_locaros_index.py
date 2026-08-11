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


# by tag_name
    button = driver.find_element(By.TAG_NAME, "button")
    button_1 = driver.find_element(By.CSS_SELECTOR, "button")

    print(button.tag_name)
    print(button.text)

    print(button_1.tag_name)
    print(button_1.text)

    links = driver.find_elements(By.TAG_NAME, "a")
    links_1 = driver.find_elements(By.CSS_SELECTOR,"a") # by tag name и by css selector почти одно и то же
    print(len(links))
    for link in links:
        print(link.text)

    print(len(links_1))
    for link in links_1:
        print(link.text)

# by class
    container = driver.find_element(By.CLASS_NAME,"container") # БЕЗ ТОЧКИ ЭТО
    container_1 = driver.find_element(By.CSS_SELECTOR,".container") # ТОЧКА ПЕРЕД СЛОВОМ ТОЧКА ЭТО ЭЛЕМЕНТ КЛАССА

# by id

    nav = driver.find_element(By.ID,"nav")
    nav_1 = driver.find_element(By.CSS_SELECTOR, "#nav")

    print("NAV id: ", nav.tag_name)
    print("NAV id: ", nav_1.tag_name)

#by attribute

    name_input = driver.find_element(By.CSS_SELECTOR, "[placeholder='Type your name']")
    item_2 = driver.find_element(By.CSS_SELECTOR, "[href='#item2']")
    nav_2 = driver.find_element(By.CSS_SELECTOR, "[id = 'nav']")

    input_name = driver.find_element(By.CSS_SELECTOR, "[name = 'name']")
    input_name_1 = driver.find_element(By.NAME, "name")

    input = driver.find_element(By.CSS_SELECTOR, "[placeholder = 'Type your name']")
    # поиск элемента по атрибуту по началу значения атрибута (placeholder) ставим ^=
    starts_input = driver.find_element(By.CSS_SELECTOR, "[placeholder ^= 'Type']")
    # поиск элемента по атрибуту по окончанию значения атрибута (placeholder) ставим $=
    ends_input = driver.find_element(By.CSS_SELECTOR, "[placeholder $= 'name']")
    # поиск элемента по атрибуту по любому содержимому значения атрибута (placeholder) ставим *=
    contains_input = driver.find_element(By.CSS_SELECTOR, "[placeholder *= 'your']")

# устаревший поиск linkText & partialLinkText

    item1 = driver.find_element(By.LINK_TEXT, "Item 1")
    all_items = driver.find_elements(By.PARTIAL_LINK_TEXT, "Item")

    first_child = driver.find_element(By.CSS_SELECTOR, "li:first-child")
    last_child = driver.find_element(By.CSS_SELECTOR, "li:last-child")
    nth_child = driver.find_element(By.CSS_SELECTOR, "li:nth-child(2)")

# Canada
    canada = driver.find_element(By.CSS_SELECTOR, "tr:nth-child(3)>td:last-child")
    assert canada.text == "Canada"

finally:
    driver.quit()