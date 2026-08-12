#open browser
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

#open site
try:
    driver.get("https://telranedu.web.app/login")

#by tag_name
    div = driver.find_element(By.TAG_NAME, "div")
    div_1 = driver.find_element(By.CSS_SELECTOR, "div")
    div_2 = driver.find_element(By.XPATH, "//div")

    h1 = driver.find_element(By.TAG_NAME, "h1")
    h1_1 = driver.find_element(By.CSS_SELECTOR, "h1")
    h1_2 = driver.find_element(By.XPATH, "//h1")

    input = driver.find_element(By.TAG_NAME, "input")
    input_1 = driver.find_element(By.CSS_SELECTOR, "input")
    input_2 = driver.find_element(By.XPATH, "//input")

    a_list = driver.find_elements(By.TAG_NAME, "a")
    a_list_1 = driver.find_elements(By.CSS_SELECTOR, "a")
    print(len(a_list))
    a_list_2 = driver.find_elements(By.XPATH, "//a")

#by class
    container = driver.find_element(By.CLASS_NAME, "container")
    container_1 = driver.find_element(By.CSS_SELECTOR, ".container")
    container_2 = driver.find_element(By.XPATH, "//div[@class = 'container']")

    navbar = driver.find_element(By.CLASS_NAME, "navbar-component_nav__1X_4m")
    navbar_1 = driver.find_element(By.CSS_SELECTOR, ".navbar-component_nav__1X_4m")
    navbar_2 = driver.find_element(By.XPATH, "//*[@class = 'navbar-component_nav__1X_4m']")

    login_login = driver.find_element(By.CLASS_NAME, "login_login__3EHKB")
    login_login_1 = driver.find_element(By.CLASS_NAME, "login_login__3EHKB")
    login_login_2 = driver.find_element(By.XPATH, "//*[@class = 'login_login__3EHKB']")

#by id
    root = driver.find_element(By.ID, "root")
    root_1 = driver.find_element(By.CSS_SELECTOR, "#root")
    root_2 = driver.find_element(By.XPATH, "//*[@id = 'root']")

    root_3 = driver.find_element(By.ID, "root")
    root_4 = driver.find_element(By.CSS_SELECTOR, "#root")

#by text
    login_button = driver.find_element(By.XPATH, "//*[text()='Login']")
    login_button_1 = driver.find_element(By.XPATH, "//*[contains(text(),'Login')]")
# by attribute

    input_3 = driver.find_element(By.XPATH, "//input[@placeholder='Password']")
    #CSS
    input_4 = driver.find_element(By.CSS_SELECTOR, "[placeholder^='Pas']") #start CSS
    input_5 = driver.find_element(By.XPATH, "//*[starts-with(@placeholder, 'Pas')]") #start XPath

    input_6 = driver.find_element(By.CSS_SELECTOR, "[placeholder $='ord']")
    input_7 = driver.find_element(By.XPATH, "//*[contains(@placeholder, 'ord')]") #end xPath

    input_8 = driver.find_element(By.CSS_SELECTOR, "[placeholder *= 'ssw']")
    input_9 = driver.find_element(By.XPATH, "//*[contains(@placeholder,'ssw')]")

    # parent
    div_3 = driver.find_element(By.XPATH, "//h1/..")
    div_4 = driver.find_element(By.XPATH, "//h1/parent::div")
    div_5 = driver.find_element(By.XPATH, "//h1/parent::*")

    #ancestor
    ancestors = driver.find_elements(By.XPATH, "//h1/ancestor::*")
    for a in ancestors:
        print(a.tag_name)

    #ancestor_or_self
    print()

    ancestors_1 = driver.find_elements(By.XPATH, "//h1/ancestor-or-self::*")
    for a in ancestors_1:
        print(a.tag_name)

    #following_sibling

    following_sibling = driver.find_elements(By.XPATH, "//h1/following-sibling::*")
    for f in following_sibling:
        print(f.tag_name)

    print()

    #preceding_sibling
    preceding_sibling = driver.find_elements(By.XPATH, "//a[@href='/login']/preceding-sibling::*")

    for p in preceding_sibling:
        print(p.tag_name)

#inner text
    login_button_1 = driver.find_element(By.CSS_SELECTOR, "[name='login']")
    text = login_button_1.text
    print(text)

    print()
    form = driver.find_element(By.XPATH, "//form")
    text_form = form.text
    print("*"*14)
    print(text_form)

    print()

    html_element = driver.find_element(By.TAG_NAME, "html")
    text_all = html_element.text
    print("*"*14)
    print(text_all)

    print()

    br = driver.find_element(By.TAG_NAME, "br")
    print("*"*14)
    print("text br---->" + br.text)
#close browser
finally:
    driver.quit()