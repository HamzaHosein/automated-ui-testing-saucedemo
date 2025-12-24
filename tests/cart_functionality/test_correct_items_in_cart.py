from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_correct_items_in_cart(driver, login):
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

    # All items in cart
    cart_name_elements = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item_name")))
    inside_cart = [el.text for el in cart_name_elements]

    assert len(inside_cart) == len(added_to_cart)
    assert set(inside_cart) == set(added_to_cart)
