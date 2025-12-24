from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC


def test_dropdown_reverse_alphabetical():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    try:
        driver.get('https://www.saucedemo.com/')

        wait.until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys('standard_user')
        wait.until(EC.visibility_of_element_located((By.ID, 'password'))).send_keys('secret_sauce')
        wait.until(EC.element_to_be_clickable((By.ID, 'login-button'))).send_keys(Keys.ENTER)
        wait.until(EC.url_contains('inventory'))

        items_before = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'inventory_item_name')))
        names_before = [item.text for item in items_before]

        dropdown = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'product_sort_container')))
        Select(dropdown).select_by_value('za')

        order_after_dropdown = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'inventory_item_name')))
        names_after = [item.text for item in order_after_dropdown]

        expected = sorted(names_before, reverse=True)
        assert names_after == expected

    finally:
        driver.quit()
