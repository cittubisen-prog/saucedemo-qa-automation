import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

class TestSauceDemoUI:

    def test_01_successful_standard_user_login(self, driver):
        """TC_AUTH_01: Verify standard user can successfully log in and view product catalogue."""
        login_page = LoginPage(driver)
        login_page.load()
        login_page.login("standard_user", "secret_sauce")

        inventory_page = InventoryPage(driver)
        assert "inventory.html" in driver.current_url
        assert inventory_page.get_product_count() == 6
        assert "Sauce Labs Backpack" in inventory_page.get_all_product_titles()

    def test_02_locked_out_user_shows_error(self, driver):
        """TC_AUTH_02: Verify locked out user receives explicit error message."""
        login_page = LoginPage(driver)
        login_page.load()
        login_page.login("locked_out_user", "secret_sauce")

        error_msg = login_page.get_error_message()
        assert "Epic sadface: Sorry, this user has been locked out." in error_msg

    def test_03_invalid_password_shows_error(self, driver):
        """TC_AUTH_03: Verify login with incorrect password displays error."""
        login_page = LoginPage(driver)
        login_page.load()
        login_page.login("standard_user", "wrong_sauce")

        error_msg = login_page.get_error_message()
        assert "Username and password do not match any user in this service" in error_msg

    def test_04_empty_credentials_validation(self, driver):
        """TC_AUTH_04: Verify submitting blank credentials triggers validation."""
        login_page = LoginPage(driver)
        login_page.load()
        login_page.login("", "")

        error_msg = login_page.get_error_message()
        assert "Epic sadface: Username is required" in error_msg

    def test_05_product_sorting_price_low_to_high(self, driver):
        """TC_PROD_02: Verify products can be sorted by Price (low to high)."""
        login_page = LoginPage(driver)
        login_page.load()
        login_page.login("standard_user", "secret_sauce")

        inventory_page = InventoryPage(driver)
        inventory_page.sort_by("lohi")

        prices = inventory_page.get_all_product_prices()
        assert prices == sorted(prices), f"Prices not sorted ascending: {prices}"
        assert prices[0] <= prices[-1]

    def test_06_add_and_remove_item_from_inventory_page(self, driver):
        """TC_CART_01 & TC_CART_02: Verify adding and removing item updates cart badge."""
        login_page = LoginPage(driver)
        login_page.load()
        login_page.login("standard_user", "secret_sauce")

        inventory_page = InventoryPage(driver)
        assert inventory_page.get_cart_count() == 0

        inventory_page.add_product_to_cart("Sauce Labs Backpack")
        assert inventory_page.get_cart_count() == 1

        inventory_page.remove_product_from_cart("Sauce Labs Backpack")
        assert inventory_page.get_cart_count() == 0

    def test_07_item_persists_in_cart_after_continue_shopping(self, driver):
        """TC_CART_04: Verify cart contents persist after navigating back to inventory."""
        login_page = LoginPage(driver)
        login_page.load()
        login_page.login("standard_user", "secret_sauce")

        inventory_page = InventoryPage(driver)
        inventory_page.add_product_to_cart("Sauce Labs Bike Light")
        inventory_page.open_cart()

        cart_page = CartPage(driver)
        assert "cart.html" in driver.current_url
        assert "Sauce Labs Bike Light" in cart_page.get_cart_item_names()

        cart_page.continue_shopping()
        assert "inventory.html" in driver.current_url
        assert inventory_page.get_cart_count() == 1

        inventory_page.open_cart()
        assert "cart.html" in driver.current_url
        assert "Sauce Labs Bike Light" in cart_page.get_cart_item_names()

    def test_08_end_to_end_checkout_workflow(self, driver):
        """TC_CHK_01: Verify complete end-to-end purchasing workflow from cart to order confirmation."""
        login_page = LoginPage(driver)
        login_page.load()
        login_page.login("standard_user", "secret_sauce")

        inventory_page = InventoryPage(driver)
        inventory_page.add_product_to_cart("Sauce Labs Onesie")
        inventory_page.open_cart()

        cart_page = CartPage(driver)
        cart_page.click_checkout()

        checkout_page = CheckoutPage(driver)
        checkout_page.fill_checkout_info("John", "Doe", "90210")
        assert "checkout-step-two.html" in driver.current_url

        checkout_page.click_finish()
        assert "checkout-complete.html" in driver.current_url
        assert checkout_page.is_order_complete()
        assert "Thank you for your order!" in checkout_page.get_order_complete_text()

    def test_09_checkout_missing_fields_validation(self, driver):
        """TC_CHK_02: Verify missing Postal Code in checkout information shows error."""
        login_page = LoginPage(driver)
        login_page.load()
        login_page.login("standard_user", "secret_sauce")

        inventory_page = InventoryPage(driver)
        inventory_page.add_product_to_cart("Sauce Labs Backpack")
        inventory_page.open_cart()

        cart_page = CartPage(driver)
        cart_page.click_checkout()

        checkout_page = CheckoutPage(driver)
        checkout_page.fill_checkout_info("Jane", "Smith", "")  # Empty postal code

        error_msg = checkout_page.get_error_message()
        assert "Error: Postal Code is required" in error_msg

    def test_10_problem_user_broken_image_defect_detection(self, driver):
        """TC_BUG_01: Verify automated detection of broken product images for problem_user."""
        login_page = LoginPage(driver)
        login_page.load()
        login_page.login("problem_user", "secret_sauce")

        # In problem_user, product images point to sl-404.168b1cce.jpg
        from selenium.webdriver.common.by import By
        img_elements = driver.find_elements(By.CSS_SELECTOR, ".inventory_item img")
        broken_count = sum(1 for img in img_elements if "sl-404" in img.get_attribute("src"))
        assert broken_count > 0, "Expected problem_user to have broken dog replacement images"
