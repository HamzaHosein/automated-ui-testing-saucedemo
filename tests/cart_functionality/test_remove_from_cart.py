from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC


def test_remove_from_cart(driver, login):
    wait = WebDriverWait(driver, 10)

    # Add 3 items to cart
    Add_buttons = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//button[starts-with(@id,'add-to-cart')]")))
    for buttons in Add_buttons[:3]:
        buttons.click()

    # Remove 2 items
    remove_button = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//button[starts-with(@id,'remove')]")))
    for buttons in remove_button[:2]:
        buttons.click()

    badge = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'shopping_cart_badge'))).text

    expected = 3 - 2
    assert badge == expected
