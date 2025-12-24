from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_login_with_enter():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    driver.get("https://www.saucedemo.com/")

    try:

        wait.until(EC.visibility_of_element_located((By.ID, 'user-name'))).send_keys('standard_user')
        wait.until(EC.visibility_of_element_located((By.ID, 'password'))).send_keys('secret_sauce', Keys.ENTER)

        items = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'inventory_item')))
        wait.until(EC.url_contains('/inventory.html'))
        wait.until(EC.title_contains('Swag Labs'))

        assert "inventory" in driver.current_url
        assert "Swag Labs" in driver.title
        assert len(items) >= 1

    finally:
        driver.quit()
