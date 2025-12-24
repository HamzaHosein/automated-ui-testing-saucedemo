from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC


def test_add_item_to_cart_update(driver, login):
    wait = WebDriverWait(driver, 10)

    #Click all buttons
    add_buttons = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//button[starts-with(@id,'add-to-cart')]")))
    for btn in add_buttons:
        btn.click()

    #Get badge number after all are added to cart
    badge = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'shopping_cart_badge'))).text
    expected_count = len(add_buttons)
    assert int(badge) == expected_count
    Add_buttons = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//button[starts-with(@id,'add-to-cart')]")))


