# Automated UI Testing Framework – SauceDemo

## 📌 Project Overview
This project is an automated UI testing framework built to validate core user workflows of an e-commerce web application using **Python, Selenium, and Pytest**.

The purpose of this project is to demonstrate real-world software testing practices including functional testing, negative testing, validation checks, and regression coverage.

The application under test is **SauceDemo**, a commonly used demo website for UI automation practice.

---

## 🛠️ Tech Stack
- Python
- Selenium WebDriver
- Pytest
- Pytest Fixtures (`conftest.py`)
- HTML Test Reporting
- IntelliJ IDEA / PyCharm

---

## 🧪 Test Coverage
Tests are organized by feature to mirror real-world QA automation frameworks.

### 🔐 Login & Access Control
- Valid login
- Invalid login
- Missing username or password
- Incorrect credentials
- Session invalidation after logout

### 🛒 Cart Functionality
- Add items to cart
- Remove items from cart
- Validate correct items appear in cart
- Cart updates dynamically

### 📦 Inventory Page
- Verify items are displayed
- Product sorting (alphabetical & reverse order)
- Dropdown sorting validation

### 💳 Checkout Validation
- Required field validation
- Error message verification
- Successful checkout flow

---

## ⚠️ Testing Strategy
- Positive testing to validate expected user behavior
- Negative testing to verify error handling and validation logic
- Regression-style testing to ensure stability across features
- Tests are designed to be repeatable, readable, and maintainable

Manual test cases were designed and executed prior to automation to identify edge cases and UI behavior.

---

## 📂 Project Structure

```
automated-ui-testing-saucedemo/
├── documentation/
│   ├── sample_test_cases.md
│   └── sample_bug_reports.md
├── tests/
│   ├── Access_Control/
│   ├── cart_functionality/
│   ├── Checkout_Validation/
│   ├── test_inventory_page/
│   ├── test_login/
│   └── conftest.py
├── README.md
├── requirements.txt
└── .gitignore
```


---

## ▶️ How to Run Tests

Run the following commands in order from the project root.

```bash
# 1. Clone the repository
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

# 2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate    # macOS / Linux
venv\Scripts\activate       # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run tests
pytest

# 5. Generate HTML test report
pytest --html=report.html

