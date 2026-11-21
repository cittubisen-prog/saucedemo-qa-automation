# Manual Test Cases: SauceDemo (Swag Labs)

**Application:** [SauceDemo](https://www.saucedemo.com/)  
**Total Test Cases:** 30  
**Coverage:** Functional, UI, Negative, Edge Cases, Security Boundaries, and Seeded Defect Detection  
**Author:** Vishwa Vijay Kumar  
**Date:** 21-Nov-2026  

---

## 1. Authentication & Session Management (TC_AUTH_01 to TC_AUTH_07)

| Test ID | Title | Preconditions | Test Steps | Expected Result | Priority |
| :--- | :--- | :--- | :--- | :--- | :---: |
| **TC_AUTH_01** | Verify successful login with valid standard credentials | User is on login page | 1. Enter Username: `standard_user`<br>2. Enter Password: `secret_sauce`<br>3. Click "Login" button | User is authenticated and redirected to `/inventory.html`. Product catalog displays 6 items. | **High** |
| **TC_AUTH_02** | Verify login rejection for locked out user persona | User is on login page | 1. Enter Username: `locked_out_user`<br>2. Enter Password: `secret_sauce`<br>3. Click "Login" button | Access denied. Red error container displays: *"Epic sadface: Sorry, this user has been locked out."* | **High** |
| **TC_AUTH_03** | Verify login rejection with invalid password | User is on login page | 1. Enter Username: `standard_user`<br>2. Enter Password: `wrong_password`<br>3. Click "Login" button | Access denied. Error banner displays: *"Epic sadface: Username and password do not match any user in this service"* | **High** |
| **TC_AUTH_04** | Verify login rejection with empty username and password | User is on login page | 1. Leave Username field blank<br>2. Leave Password field blank<br>3. Click "Login" button | Form submission prevented. Error container displays: *"Epic sadface: Username is required"* | **High** |
| **TC_AUTH_05** | Verify login rejection with empty password only | User is on login page | 1. Enter Username: `standard_user`<br>2. Leave Password field blank<br>3. Click "Login" button | Form submission prevented. Error container displays: *"Epic sadface: Password is required"* | **Medium** |
| **TC_AUTH_06** | Verify SQL/XSS payload sanitization in username field (Security Edge Case) | User is on login page | 1. Enter Username: `' OR '1'='1' -- <script>alert(1)</script>`<br>2. Enter Password: `secret_sauce`<br>3. Click "Login" | Input is safely escaped without server crash (500) or script execution. Generic authentication error displayed. | **High** |
| **TC_AUTH_07** | Verify successful session logout via side navigation menu | User is logged in on `/inventory.html` | 1. Click burger menu button (`#react-burger-menu-btn`)<br>2. Click "Logout" link | User session terminated. Redirected to login page (`/`). Back navigation does not access authenticated pages. | **High** |

---

## 2. Product Catalog & Sorting (TC_PROD_01 to TC_PROD_06)

| Test ID | Title | Preconditions | Test Steps | Expected Result | Priority |
| :--- | :--- | :--- | :--- | :--- | :---: |
| **TC_PROD_01** | Verify default inventory page catalog rendering | Logged in as `standard_user` | 1. Navigate to `/inventory.html`<br>2. Inspect items on page | Exactly 6 products displayed with title, description, price, matching image, and "Add to cart" button. | **High** |
| **TC_PROD_02** | Verify product sorting by Price: Low to High | Logged in as `standard_user` | 1. Open sort dropdown (`.product_sort_container`)<br>2. Select "Price (low to high)" (`lohi`) | Products rearrange in ascending order by price ($7.99 Onesie first, $49.99 Fleece Jacket last). | **High** |
| **TC_PROD_03** | Verify product sorting by Price: High to Low | Logged in as `standard_user` | 1. Open sort dropdown<br>2. Select "Price (high to low)" (`hilo`) | Products rearrange in descending order by price ($49.99 Fleece Jacket first, $7.99 Onesie last). | **High** |
| **TC_PROD_04** | Verify product sorting by Name: Z to A | Logged in as `standard_user` | 1. Open sort dropdown<br>2. Select "Name (Z to A)" (`za`) | Products rearrange in reverse alphabetical order ("Test.allTheThings() T-Shirt" first). | **Medium** |
| **TC_PROD_05** | Verify product sorting by Name: A to Z (Default) | Logged in as `standard_user` | 1. Sort by Z to A first<br>2. Re-select "Name (A to Z)" (`az`) | Products return to alphabetical order ("Sauce Labs Backpack" first). | **Medium** |
| **TC_PROD_06** | Verify product detail page navigation and content integrity | Logged in as `standard_user` | 1. Click on product title "Sauce Labs Backpack"<br>2. Inspect product details page | Redirects to `/inventory-item.html?id=4`. Large image, title, detailed description, and correct price ($29.99) load. | **Medium** |

---

## 3. Shopping Cart Management (TC_CART_01 to TC_CART_06)

| Test ID | Title | Preconditions | Test Steps | Expected Result | Priority |
| :--- | :--- | :--- | :--- | :--- | :---: |
| **TC_CART_01** | Verify adding product to cart from inventory updates badge | Logged in as `standard_user` | 1. Click "Add to cart" on "Sauce Labs Backpack" | Button text toggles to "Remove". Cart badge displays "1". | **High** |
| **TC_CART_02** | Verify removing product from inventory updates badge | 1 item in cart | 1. Click "Remove" button on "Sauce Labs Backpack" | Button toggles back to "Add to cart". Cart badge counter disappears. | **High** |
| **TC_CART_03** | Verify adding multiple products increments cart badge correctly | Logged in as `standard_user` | 1. Click "Add to cart" on Backpack<br>2. Click "Add to cart" on Bike Light<br>3. Click "Add to cart" on Bolt T-Shirt | Cart badge updates incrementally to "3". | **High** |
| **TC_CART_04** | Verify cart item persistence across navigation ("Continue Shopping") | Item added to cart | 1. Open cart page (`/cart.html`)<br>2. Click "Continue Shopping"<br>3. Verify inventory page and reopen cart | Cart badge remains "1". Cart retains "Sauce Labs Bike Light" with correct price and quantity. | **Medium** |
| **TC_CART_05** | Verify removing product directly from `/cart.html` | 2 items in cart | 1. Open `/cart.html`<br>2. Click "Remove" on one item | Item is removed from list. Remaining item persists. Cart badge decrements to "1". | **Medium** |
| **TC_CART_06** | Verify adding item from Product Detail view | On `/inventory-item.html?id=4` | 1. Click "Add to cart" on detail view<br>2. Click cart icon | Button toggles to "Remove". Cart badge displays "1". Item appears in cart. | **Medium** |

---

## 4. Checkout Operations & Edge Scenarios (TC_CHK_01 to TC_CHK_08)

| Test ID | Title | Preconditions | Test Steps | Expected Result | Priority |
| :--- | :--- | :--- | :--- | :--- | :---: |
| **TC_CHK_01** | Verify complete end-to-end checkout purchase (Happy Path) | Item in cart | 1. Navigate to `/cart.html`<br>2. Click "Checkout"<br>3. Enter First Name: `John`, Last Name: `Doe`, Zip: `90210`<br>4. Click "Continue"<br>5. Click "Finish" | Order placed successfully. Navigated to `/checkout-complete.html`. "Thank you for your order!" displayed. | **High** |
| **TC_CHK_02** | Verify checkout validation when Postal Code is missing | On `/checkout-step-one.html` | 1. Enter First Name: `John`<br>2. Enter Last Name: `Doe`<br>3. Leave Postal Code blank<br>4. Click "Continue" | Transition blocked. Error banner displayed: *"Error: Postal Code is required"*. | **High** |
| **TC_CHK_03** | Verify checkout validation when First Name is missing | On `/checkout-step-one.html` | 1. Leave First Name blank<br>2. Enter Last Name: `Doe`<br>3. Enter Postal Code: `90210`<br>4. Click "Continue" | Transition blocked. Error banner displayed: *"Error: First Name is required"*. | **High** |
| **TC_CHK_04** | Verify checkout validation when Last Name is missing | On `/checkout-step-one.html` | 1. Enter First Name: `John`<br>2. Leave Last Name blank<br>3. Enter Postal Code: `90210`<br>4. Click "Continue" | Transition blocked. Error banner displayed: *"Error: Last Name is required"*. | **High** |
| **TC_CHK_05** | Verify checkout calculation integrity (Subtotal, Tax, and Total) | 2 items in cart ($29.99 + $9.99) | 1. Complete Step One with valid info<br>2. Inspect Step Two summary | Item Total = $39.98. Tax (8%) = $3.20. Total = $43.18. Math is accurate. | **High** |
| **TC_CHK_06** | Verify cancel checkout button returns user to cart | On `/checkout-step-one.html` | 1. Click "Cancel" button | Navigated back to `/cart.html`. All items in cart remain preserved. | **Medium** |
| **TC_CHK_07** | Verify empty cart checkout behavior (Edge Case / Flaw) | Cart is empty (0 items) | 1. Open `/cart.html`<br>2. Click "Checkout"<br>3. Enter valid customer info<br>4. Click "Continue" | System should ideally block checkout with an empty cart. (Edge case: SauceDemo allows advancing to overview with $0). | **Medium** |
| **TC_CHK_08** | Verify browser back button after order completion (Edge Case) | Order completed (`/checkout-complete.html`) | 1. Click browser Back button | System does not re-submit payment or create duplicate order; cart remains 0. | **Medium** |

---

## 5. Seeded User Persona & Defect Testing (TC_BUG_01 to TC_BUG_03)

| Test ID | Title | Preconditions | Test Steps | Expected Result | Priority |
| :--- | :--- | :--- | :--- | :--- | :---: |
| **TC_BUG_01** | Verify `problem_user` broken product images defect | Login page | 1. Login with `problem_user`<br>2. Inspect product images on `/inventory.html` | **Defect Detection:** Product images fail to load correctly; all 6 items show the generic dog placeholder (`sl-404.168b1cce.jpg`). | **High** |
| **TC_BUG_02** | Verify `problem_user` checkout Last Name input defect | Login as `problem_user` with item in cart | 1. Go to `/checkout-step-one.html`<br>2. Type "Doe" in Last Name field<br>3. Click "Continue" | **Defect Detection:** Last Name input refuses text or clears; form triggers *"Error: Last Name is required"*, blocking checkout. | **High** |
| **TC_BUG_03** | Verify `performance_glitch_user` load latency | Login page | 1. Login with `performance_glitch_user`<br>2. Measure page load time to `/inventory.html` | **Performance Defect:** Inventory page load takes > 5 seconds due to deliberate backend throttling. | **Medium** |
