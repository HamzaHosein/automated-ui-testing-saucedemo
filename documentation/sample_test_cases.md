# Sample Test Cases – SauceDemo

> This document contains representative test cases designed for this project.  
> Some scenarios were executed through automation using Selenium and Pytest, while others were validated manually where automation was not practical.  
> The purpose of this document is to demonstrate test design, validation logic, and execution decisions.

---

## Test Case 1

### **Test Case ID:** TC_LOGIN_001
**Title:** Verify user cannot log in with empty password  
**Execution Type:** Automated  
**Precondition:** User is on the login page

**Steps:**
1. Enter a valid username
2. Leave the password field empty
3. Click the **Login** button

**Expected Result:**  
An error message is displayed indicating that the password is required

**Priority:** High  
**Test Type:** Negative

---

## Test Case 2

### **Test Case ID:** TC_LOGIN_002
**Title:** Verify user cannot log in with invalid credentials  
**Execution Type:** Automated  
**Precondition:** User is on the login page

**Steps:**
1. Enter an invalid username
2. Enter an invalid password
3. Click the **Login** button

**Expected Result:**  
An error message is displayed indicating invalid username or password

**Priority:** High  
**Test Type:** Negative

---

## Test Case 3

### **Test Case ID:** TC_CART_001
**Title:** Verify item is added to cart successfully  
**Execution Type:** Automated  
**Precondition:** User is logged in and on the inventory page

**Steps:**
1. Click **Add to Cart** on any product
2. Navigate to the cart page

**Expected Result:**  
The selected item appears in the cart

**Priority:** High  
**Test Type:** Functional

---

## Test Case 4

### **Test Case ID:** TC_INVENTORY_001
**Title:** Verify products can be sorted alphabetically (A–Z)  
**Execution Type:** Automated  
**Precondition:** User is logged in and on the inventory page

**Steps:**
1. Open the product sort dropdown
2. Select the option **Name (A to Z)**
3. Observe the order of displayed products

**Expected Result:**  
Products are displayed in alphabetical order from A to Z

**Priority:** Medium  
**Test Type:** Functional


---

## Test Case 5

### **Test Case ID:** TC_CHECKOUT_001
**Title:** Verify checkout cannot proceed with missing required fields  
**Execution Type:** Automated  
**Precondition:** User has items in the cart and is on the checkout page

**Steps:**
1. Leave one or more required fields empty
2. Click **Continue**

**Expected Result:**  
An error message is displayed indicating required fields must be filled

**Priority:** High  
**Test Type:** Validation

---

## Test Case 6

### **Test Case ID:** TC_UI_001
**Title:** Verify UI layout remains consistent across different screen sizes  
**Execution Type:** Manual  
**Precondition:** User is logged in

**Steps:**
1. Resize the browser window to different widths
2. Observe page layout and alignment

**Expected Result:**  
UI elements remain properly aligned with no overlap or distortion

**Priority:** Low  
**Test Type:** UI / Usability

---

## Test Case 7

### **Test Case ID:** TC_USABILITY_001
**Title:** Verify error messages are clear and user-friendly  
**Execution Type:** Manual  
**Precondition:** User is on the login or checkout page

**Steps:**
1. Trigger a validation error (e.g., missing required field)
2. Observe the error message displayed

**Expected Result:**  
Error message is clear, readable, and explains how to resolve the issue

**Priority:** Medium  
**Test Type:** Usability

---









