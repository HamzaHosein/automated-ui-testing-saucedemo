from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_error_missing_fields(driver, login):
    wait = WebDriverWait(driver, 10)

    all_items = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item")))
    for item in all_items[:3]:
        item.find_element(By.XPATH, ".//button[starts-with(@id,'add-to-cart')]").click()

    wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))).click()
    wait.until(EC.url_contains("cart"))

    wait.until(EC.element_to_be_clickable((By.ID, "checkout"))).click()
    wait.until(EC.url_contains("checkout-step-one"))

    continue_button = wait.until(EC.element_to_be_clickable((By.ID, "continue")))
    first_name = wait.until(EC.visibility_of_element_located((By.ID, "first-name")))
    last_name = wait.until(EC.visibility_of_element_located((By.ID, "last-name")))
    zip_code = wait.until(EC.visibility_of_element_located((By.ID, "postal-code")))

    ERROR_LOC = (By.CSS_SELECTOR, "h3[data-test='error']")

    def hard_clear(el):
        el.click()
        el.send_keys(Keys.CONTROL, "a")
        el.send_keys(Keys.BACKSPACE)

    def clear_fields():
        hard_clear(first_name)
        hard_clear(last_name)
        hard_clear(zip_code)

    def click_continue_expect_error(expected_full_text):
        continue_button.click()

        # make sure we didn't pass validation (go to step two)
        assert "checkout-step-one" in driver.current_url

        # wait for the *specific* error text to be present
        wait.until(EC.text_to_be_present_in_element(ERROR_LOC, expected_full_text))
        return driver.find_element(*ERROR_LOC).text

    # Missing First name
    clear_fields()
    last_name.send_keys("joe")
    zip_code.send_keys("00000")
    assert click_continue_expect_error("Error: First Name is required") == "Error: First Name is required"

    # Missing postal code
    clear_fields()
    first_name.send_keys("Nick")
    last_name.send_keys("joe")
    assert click_continue_expect_error("Error: Postal Code is required") == "Error: Postal Code is required"

    # Missing last name
    clear_fields()
    first_name.send_keys("Nick")
    zip_code.send_keys("00000")
    assert click_continue_expect_error("Error: Last Name is required") == "Error: Last Name is required"
