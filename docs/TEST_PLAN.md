# Test Plan: SauceDemo E-Commerce Application

**Application Under Test:** [SauceDemo (Swag Labs)](https://www.saucedemo.com/)  
**Prepared For:** ZA Charity Feed Foundation (ZACFF / Tech.co)  
**Author:** Vishwa Vijay Kumar (Junior QA Automation Tester)  
**Date:** 21-Nov-2026  
**Document Version:** 1.0  

---

## 1. Introduction & Objectives
The objective of this test plan is to define the testing strategy, scope, environment, and verification criteria for the SauceDemo e-commerce web platform. Testing verifies end-to-end user workflows, functional boundaries, seeded user profiles, shopping cart state management, and checkout operations to ensure a defect-free, resilient user experience.

---

## 2. Scope of Testing

### 2.1 In-Scope Features
* **Authentication & Session Management:**
  * Valid login with standard user credentials.
  * Seeded user personas: `standard_user`, `locked_out_user`, `problem_user`, `performance_glitch_user`, `error_user`, `visual_user`.
  * Form field validation: Empty username/password, invalid credentials, case sensitivity, SQL injection & XSS sanitization.
  * Session termination via burger menu Logout.
* **Product Catalog & Inventory Management:**
  * Catalog rendering (6 default items with image, description, and pricing).
  * Product sorting options: Name (A to Z), Name (Z to A), Price (low to high), Price (high to low).
  * Individual product detail page navigation.
* **Shopping Cart Operations:**
  * Adding and removing single/multiple items from both catalog and cart views.
  * Real-time shopping cart badge counter updates.
  * Cart state persistence across page navigation and "Continue Shopping" actions.
* **Checkout & Order Fulfillment:**
  * Two-step checkout process (`/checkout-step-one.html` and `/checkout-step-two.html`).
  * Customer information form validation: First Name, Last Name, Postal/ZIP code.
  * Order summary calculations: Item subtotal, tax calculation (8%), and final total.
  * Order dispatch confirmation and post-completion navigation ("Back Home").
  * Edge scenarios: Empty cart checkout, back-button navigation after payment completion.

### 2.2 Out-of-Scope
* Actual third-party credit card gateway processing (SauceDemo uses simulated checkout).
* Multi-lingual localization beyond standard English US.

---

## 3. Test Strategy & Methodologies
* **Manual Testing:** Exploratory testing across various seeded user accounts, boundary value analysis, equivalence partitioning, and UI verification.
* **Automated Regression Testing:** Python + Selenium WebDriver + Pytest following the Page Object Model (POM) pattern.
* **API Testing:** Automated REST API tests on `https://reqres.in` validating schemas, status codes, and edge conditions.
* **Defect Management:** Issues tracked on GitHub Issues with Kanban board categorization (To Do, In Progress, Done).

---

## 4. Test Environment & Personas

| User Persona | Password | Purpose & Seeded Behavior |
| :--- | :--- | :--- |
| `standard_user` | `secret_sauce` | Golden happy-path user with fully functional behavior. |
| `locked_out_user` | `secret_sauce` | Negative authentication test; user account is suspended. |
| `problem_user` | `secret_sauce` | Defect testing; exhibits broken images, broken Last Name input, and sorting bugs. |
| `performance_glitch_user` | `secret_sauce` | Latency testing; introduces artificial 5-second server delay. |

**Hardware & Software:**
* **OS:** Windows 11 (64-bit) / Ubuntu Linux (CI environment)
* **Browser:** Google Chrome (Headless & Desktop, v133+)
* **Automation Framework:** Pytest 9.2, Selenium WebDriver 4.43, Python 3.12

---

## 5. Entry & Exit Criteria
* **Entry Criteria:** Target application accessible via internet; test automation environment configured.
* **Exit Criteria:**
  * 100% of critical path test cases executed.
  * Minimum 25 manual test cases documented.
  * All identified bugs logged with reproduction steps, severity, priority, and screenshots.
  * Automated UI (8+ cases) and API (4+ cases) passing with zero flakiness in local and CI environments.
