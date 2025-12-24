from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC


def test_sort_products_low_to_high(driver, login):
    wait = WebDriverWait(driver, 10)

    # Prices BEFORE sorting
    price_elements_before = wait.until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item_price"))
    )
    prices_before = [float(p.text.replace("$", "")) for p in price_elements_before]

    # Select "Price (low to high)"
    sort_dropdown = wait.until(
        EC.element_to_be_clickable((By.CLASS_NAME, "product_sort_container"))
    )
    Select(sort_dropdown).select_by_value("lohi")

    # Prices AFTER sorting
    price_elements_after = wait.until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item_price"))
    )
    prices_after = [float(p.text.replace("$", "")) for p in price_elements_after]

    # Assertions
    assert prices_before != prices_after
    assert prices_after == sorted(prices_after)
