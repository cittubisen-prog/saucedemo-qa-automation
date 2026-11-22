# SauceDemo  QA Automation  Assessment Suite

![QA Automation CI Pipeline](https://github.com/cittubisen-prog/saucedemo-qa-automation/actions/workflows/ci.yml/badge.svg)
![Python Version](https://img.shields.io/badge/python-3.12-blue.svg)
![Pytest Version](https://img.shields.io/badge/pytest-9.2-green.svg)
![Selenium Version](https://img.shields.io/badge/selenium-4.43-orange.svg)
![License](https://img.shields.io/badge/license-MIT-lightgrey.svg)

**Author:** Vishwa Vijay Kumar  
**GitHub Profile:** [@cittubisen-prog](https://github.com/cittubisen-prog)  
**Target Web Application:** [SauceDemo (Swag Labs)](https://www.saucedemo.com/)  
**Target REST API:** [Reqres.in](https://reqres.in/)  
**Evaluator:** Khalid Shekhani, HR Manager, ZA Charity Feed Foundation (ZACFF / Tech.co)  
**Date:** 21-Nov-2026  

---

## 📖 Executive Summary
This repository contains the complete 4-part deliverables for the **Junior QA Tester** assessment:
1. **Part 1 — Manual Test Plan & Test Cases:** A comprehensive test plan covering authentication, catalog, cart, and checkout workflows alongside **30 meticulously documented test cases** covering functional, UI, negative, security, and edge scenarios.
2. **Part 2 — Bug Reports & Evidence:** Detailed documentation of **3 real defects** discovered on SauceDemo using seeded accounts (`problem_user`, `locked_out_user`) with step-by-step reproduction and attached screenshot evidence.
3. **Part 3 — Web UI Test Automation:** A production-grade **Page Object Model (POM)** automation framework built with **Selenium WebDriver & Pytest** automating 10 comprehensive UI scenarios runnable with a single command.
4. **Part 4 — REST API Test Automation:** Automated test suite validating status codes AND JSON response body schema/shape for GET, POST, 400 Bad Request, and 404 Not Found endpoints on `https://reqres.in`.
5. **Bonus — CI/CD Pipeline:** A configured **GitHub Actions workflow** (`.github/workflows/ci.yml`) executing the full test suite automatically on push and pull requests.

---

## 📂 Repository Directory Structure

```text
saucedemo-qa-automation/
├── .github/
│   └── workflows/
│       └── ci.yml                     # Bonus: GitHub Actions CI automated pipeline
├── docs/
│   ├── TEST_PLAN.md                  # Part 1: Comprehensive E-Commerce Test Plan
│   ├── TEST_CASES.md                 # Part 1: 30 Detailed Manual Test Cases Table
│   ├── BUG_REPORTS.md                # Part 2: Detailed Real Bug Reports with Steps & Evidence
│   └── GITHUB_SETUP_GUIDE.md         # Step-by-step GitHub Issues & Project Board guide
├── pages/                             # Page Object Model (POM) Design Pattern
│   ├── __init__.py
│   ├── base_page.py                  # Core driver wrapper & explicit waits
│   ├── login_page.py                 # Authentication actions & locators
│   ├── inventory_page.py             # Product catalog, sorting, and cart badge logic
│   ├── cart_page.py                  # Shopping cart item verification & actions
│   └── checkout_page.py              # Checkout step 1, step 2, and complete flows
├── tests/                             # Automated Test Suites
│   ├── __init__.py
│   ├── conftest.py                   # Pytest fixtures & headless Chrome driver setup
│   ├── test_saucedemo_ui.py          # Part 3: 10 Automated UI Regression Tests
│   └── test_reqres_api.py            # Part 4: 5 Automated REST API Tests
├── screenshots/                       # Evidence Screenshots for Bug Reports
│   ├── BUG-01_problem_user_broken_images.png
│   ├── BUG-02_problem_user_checkout_lastname_broken.png
│   ├── BUG-03_locked_out_user_error.png
│   └── standard_user_inventory_success.png
├── package.json                       # Cross-platform npm scripts
├── pytest.ini                         # Pytest configuration & options
├── requirements.txt                   # Python dependencies
├── ZACFF_Junior_QA_Assessment_Vishwa_Vijay_Kumar.xlsx # Excel spreadsheet with Test Plan & Cases
└── README.md                          # Main project documentation
```

---

## Setup & Execution Guide

### Prerequisites
* **Python 3.10+** (Tested on Python 3.12)
* **Google Chrome Browser** installed
* Optional: Node.js & npm (for `npm test`)

### 1. Installation
Clone this repository and install dependencies:
```bash
git clone https://github.com/cittubisen-prog/saucedemo-qa-automation.git
cd saucedemo-qa-automation

# Install Python requirements
pip install -r requirements.txt
```

### 2. Running Automated Tests with a Single Command

#### Run All Automated Tests (UI + API):
```bash
pytest
```
*or via npm:*
```bash
npm test
```

#### Run Web UI Automation Only (Part 3):
```bash
pytest tests/test_saucedemo_ui.py
```

#### Run REST API Tests Only (Part 4):
```bash
pytest tests/test_reqres_api.py
```

---

##  Part 3: UI Test Automation Suite Overview

The UI suite implements the **Page Object Model (POM)** pattern for maintainability and separation of concerns. All 10 tests run in headless Chrome mode:

| Test Method | Coverage & Validation |
| :--- | :--- |
| `test_01_successful_standard_user_login` | Validates `standard_user` login, redirect to `/inventory.html`, and verifies catalog item count. |
| `test_02_locked_out_user_shows_error` | Negative test asserting that `locked_out_user` receives explicit suspension warning. |
| `test_03_invalid_password_shows_error` | Negative test asserting credential mismatch error message. |
| `test_04_empty_credentials_validation` | Negative test asserting field validation for empty username and password. |
| `test_05_product_sorting_price_low_to_high` | Functional test asserting ascending price sort order (`lohi`). |
| `test_06_add_and_remove_item_from_inventory` | Functional test verifying dynamic shopping cart badge increment and decrement. |
| `test_07_item_persists_in_cart_after_continue` | State test verifying cart items persist across navigation via "Continue Shopping". |
| `test_08_end_to_end_checkout_workflow` | End-to-end happy path from adding item, cart review, customer details, to order confirmation. |
| `test_09_checkout_missing_fields_validation` | Boundary test verifying error alert when Postal Code is missing. |
| `test_10_problem_user_broken_image_defect` | Automated bug assertion detecting that `problem_user` product images fall back to the 404 dog image. |

---

##  Part 4: API Testing Suite Overview

Automated tests for `https://reqres.in` targeting both status codes and **response body shape / schema integrity**:

* **`test_01_get_users_list_successful`:** GET `/api/users?page=2` asserting HTTP 200, pagination metadata schema, and verifying data items contain `id`, `email`, `first_name`, `last_name`, and valid URL `avatar`.
* **`test_02_create_user_post_successful`:** POST `/api/users` with payload asserting HTTP 201 Created, body mirroring `name` and `job`, and presence of generated `id` and `createdAt` timestamp.
* **`test_03_post_register_missing_password_negative`:** POST `/api/register` with missing password asserting HTTP 400 Bad Request and exact error shape `{"error": "Missing password"}`.
* **`test_04_get_single_user_not_found`:** GET `/api/users/23` asserting HTTP 404 Not Found and empty JSON body `{}`.
* **`test_05_update_user_put_successful`:** PUT `/api/users/2` asserting HTTP 200 OK and presence of `updatedAt`.

---

##  Part 2: Bug Reports Summary

Full details in [docs/BUG_REPORTS.md](docs/BUG_REPORTS.md):

1. **BUG-001 (High):** All product cards render broken dog image (`sl-404`) instead of item images when logged in as `problem_user`.
2. **BUG-002 (Critical):** Checkout Last Name field refuses input / locks, triggering *"Error: Last Name is required"* and permanently blocking order checkout (`problem_user`).
3. **BUG-003 (Medium):** `locked_out_user` receives account lock error without any recovery link or customer support guidance.

---

## Bonus: GitHub Actions CI Pipeline

The project includes `.github/workflows/ci.yml` which executes automatically on every `push` and `pull_request` to `main`:
1. Provisions Ubuntu runner with Python 3.12.
2. Installs headless Google Chrome and required dependencies.
3. Executes `pytest -v --tb=short`.
4. Publishes real-time test status.
