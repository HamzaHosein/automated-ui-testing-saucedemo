from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_logged_out_user_access():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    driver.get('https://www.saucedemo.com/')

    try:
        wait.until(EC.visibility_of_element_located((By.ID, 'password')))
        enter_button = wait.until(EC.visibility_of_element_located((By.ID, 'login-button')))
        enter_button.send_keys(Keys.ENTER)
        error_message = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'h3[data-test= error'))).text

        assert 'https://www.saucedemo.com/' in driver.current_url
        assert 'Epic sadface: Username is required' in error_message

    finally:
        driver.quit()
