from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_no_username():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    try:
        driver.get('https://www.saucedemo.com/')

        wait.until(EC.visibility_of_element_located((By.ID, 'user-name'))).send_keys('standard_user')
        wait.until(EC.visibility_of_element_located((By.ID, 'password'))).send_keys('')
        wait.until(EC.element_to_be_clickable((By.ID, 'login-button'))).click()

        error_message = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'h3[data-test="error"]')))

        assert 'Epic sadface: Password is required' in error_message.text
    finally:
        driver.quit()