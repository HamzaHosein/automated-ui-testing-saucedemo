# Sample Bug Reports – SauceDemo

> **Disclaimer:**  
> The bug reports below are provided as sample examples to demonstrate defect documentation, severity assessment, and clear communication.  
> They do not necessarily represent actual defects in the SauceDemo application and are included for portfolio and learning purposes.


---

## Bug Report 1

### **Bug ID:** BUG_CART_001
**Title:** Cart badge count does not update after removing item  
**Environment:** Chrome 120, Windows 11  
**Build/Version:** SauceDemo Web Application

**Precondition:**  
User is logged in and has at least one item added to the cart

**Steps to Reproduce:**
1. Add an item to the cart from the inventory page
2. Verify cart badge count increases
3. Navigate to the cart page
4. Click **Remove** on the item

**Expected Result:**  
Cart badge count updates to reflect item removal

**Actual Result:**  
Cart badge count remains unchanged after item is removed

**Severity:** Medium  
**Priority:** High

**Status:** Open

**Notes:**  
Issue impacts user trust and UI accuracy but does not always block checkout.

---

## Bug Report 2

### **Bug ID:** BUG_CHECKOUT_001
**Title:** Checkout allows continuation when required fields are left empty  
**Environment:** Chrome 120, Windows 11  
**Build/Version:** SauceDemo Web Application

**Precondition:**  
User is logged in and has items in the cart

**Steps to Reproduce:**
1. Navigate to the checkout page
2. Leave one or more required fields empty
3. Click **Continue**

**Expected Result:**  
User is blocked from continuing and an error message is displayed

**Actual Result:**  
Checkout proceeds without displaying validation error

**Severity:** High  
**Priority:** High

**Status:** Open

**Notes:**  
This issue blocks proper checkout validation and may lead to incomplete or incorrect orders.

---

