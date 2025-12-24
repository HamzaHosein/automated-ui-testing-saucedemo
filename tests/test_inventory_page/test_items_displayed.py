from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver



def test_access_control_redirect():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    try:
        driver.get("https://www.saucedemo.com/inventory.html")

        wait.until(EC.visibility_of_element_located((By.ID, 'user-name'))).send_keys('standard_user')
        wait.until(EC.visibility_of_element_located((By.ID, 'password'))).send_keys('secret_sauce')
        wait.until(EC.element_to_be_clickable((By.ID, 'login-button'))).click()

        wait.until(EC.url_contains('/inventory'))

        items = driver.find_elements(By.CLASS_NAME, 'inventory_item')
        assert len(items) == 6, f'Expected 6 items, but found {len(items)}'

        for i, item in enumerate(items, start=1):
            image = item.find_element(By.CLASS_NAME, 'inventory_item_img')
            title = item.find_element(By.CLASS_NAME,'inventory_item_name').text
            description = item.find_element(By.CLASS_NAME, 'inventory_item_desc').text
            price = item.find_element(By.CLASS_NAME, 'inventory_item_price').text
            button = item.find_element(By.TAG_NAME, 'button')

        assert image.is_displayed(), f'Item {i} is not displayed'
        assert title != "", f'Title {i} is invalid'
        assert description != "", f'Description {i} is invalid'
        assert "$" in price, f'Item {i} contains a faulty price'
        assert button.is_displayed(), f'item {i} button is not displaying'

    finally:
        driver.quit()
