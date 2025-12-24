from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_valid_checkout_info(driver, login):
    wait = WebDriverWait(driver, 10)

    # Get all Items
    all_items = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item")))

    # Add first 3 items to cart
    added_to_cart = []
    for item in all_items[:3]:
        name = item.find_element(By.CLASS_NAME, "inventory_item_name").text
        added_to_cart.append(name)

        item.find_element(By.XPATH, ".//button[starts-with(@id,'add-to-cart')]").click()

    # Click on cart
    wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))).click()
    wait.until(EC.url_contains("cart"))

    # List of checkout items
    items_in_checkout = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'inventory_item_name')))
    checkout_items = [items.text for items in items_in_checkout]
    assert len(checkout_items) == len(added_to_cart)
    assert set(checkout_items) == set(added_to_cart)

    # Click on checkout
    wait.until(EC.element_to_be_clickable((By.ID, 'checkout'))).click()
    wait.until(EC.url_contains('checkout-step-one'))
    first_name = wait.until(EC.visibility_of_element_located((By.ID, 'first-name')))
    last_name = wait.until(EC.visibility_of_element_located((By.ID, 'last-name')))
    zip_code = wait.until(EC.visibility_of_element_located((By.ID, 'postal-code')))
    continue_button = wait.until(EC.element_to_be_clickable((By.ID, 'continue')))

    first_name.send_keys('Nick')
    last_name.send_keys('Joe')
    zip_code.send_keys('00000')
    continue_button.click()

    assert driver.current_url == 'https://www.saucedemo.com/checkout-step-two.html'

    wait.until(EC.element_to_be_clickable((By.ID, 'finish'))).click()
    wait.until(EC.url_contains('checkout-complete'))

    header_after_complete = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'complete-header'))).text
    title_after_complete = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'title'))).text

    assert 'Thank you for your order!' in header_after_complete
    assert 'Checkout: Complete!' in title_after_complete
    assert driver.current_url == 'https://www.saucedemo.com/checkout-complete.html'
