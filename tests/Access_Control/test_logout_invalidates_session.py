from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


def test_logout_invalidates_session():

    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    try:
        driver.get('https://www.saucedemo.com/')

        wait.until(EC.visibility_of_element_located((By.ID, 'user-name'))).send_keys('standard_user')
        wait.until(EC.visibility_of_element_located((By.ID, 'password'))).send_keys('secret_sauce', Keys.ENTER)
        wait.until(EC.url_contains('inventory'))

        wait.until(EC.element_to_be_clickable((By.ID, 'react-burger-menu-btn'))).click()
        wait.until(EC.element_to_be_clickable((By.ID, 'logout_sidebar_link'))).click()


        wait.until(EC.visibility_of_element_located((By.ID, 'user-name')))
        assert 'inventory' not in driver.current_url

        driver.back()
        wait.until(EC.element_to_be_clickable((By.ID, 'user-name')))
        assert 'inventory' not in driver.current_url

        driver.get('https://www.saucedemo.com/inventory.html')
        wait.until(EC.element_to_be_clickable((By.ID, 'login-button')))
        assert 'inventory' not in driver.current_url

    finally:
        driver.quit()
