from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_login_fail():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    try:
        driver.get('https://www.saucedemo.com/')

        enter_username = wait.until(EC.visibility_of_element_located((By.ID, 'user-name')))
        enter_username.send_keys('Standard_User')
        enter_password = wait.until(EC.visibility_of_element_located((By.ID, 'password')))
        enter_password.send_keys('Secret_Sauce')

        click_login = wait.until(EC.element_to_be_clickable((By.ID, 'login-button')))
        click_login.click()

        error_message = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'h3[data-test="error"]')))

        assert "Username and password do not match any user in this service" in error_message.text
    finally:
        driver.quit()
