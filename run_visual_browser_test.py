import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

def slow_type(element, text, delay=0.08):
    element.clear()
    for char in text:
        element.send_keys(char)
        time.sleep(delay)

def main():
    print("=" * 70)
    print("    LIVE VISUAL AUTOMATION DEMO (HEADED CHROME BROWSER)")
    print("    Application: SauceDemo (Swag Labs)")
    print("    Candidate: Vishwa Vijay Kumar")
    print("=" * 70)
    print("\n[INFO] Opening Google Chrome Browser on your screen...")

    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-notifications")
    # NOT headless - browser window will be fully visible!

    driver = webdriver.Chrome(options=chrome_options)
    wait = WebDriverWait(driver, 10)

    try:
        # Step 1: Open SauceDemo
        print("\n[STEP 1] Navigating to https://www.saucedemo.com/ ...")
        driver.get("https://www.saucedemo.com/")
        time.sleep(1.5)

        # Step 2: Login standard_user
        print("[STEP 2] Entering Username: 'standard_user' and Password: 'secret_sauce'...")
        username_input = wait.until(EC.visibility_of_element_located((By.ID, "user-name")))
        password_input = wait.until(EC.visibility_of_element_located((By.ID, "password")))
        slow_type(username_input, "standard_user")
        time.sleep(0.5)
        slow_type(password_input, "secret_sauce")
        time.sleep(0.8)

        print("[STEP 3] Clicking 'Login' button...")
        login_btn = driver.find_element(By.ID, "login-button")
        login_btn.click()
        time.sleep(1.5)

        # Step 3: Product inventory
        print("[STEP 4] Inventory Page Loaded! Verifying 6 products display...")
        items = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item")))
        print(f"         ✓ Total products visible on screen: {len(items)}")
        time.sleep(1.5)

        # Step 4: Sorting Low to High
        print("[STEP 5] Selecting 'Price (low to high)' from sorting dropdown...")
        sort_dropdown = Select(driver.find_element(By.CLASS_NAME, "product_sort_container"))
        sort_dropdown.select_by_value("lohi")
        time.sleep(2)
        prices = [e.text for e in driver.find_elements(By.CLASS_NAME, "inventory_item_price")]
        print(f"         ✓ Products sorted by price: {', '.join(prices)}")
        time.sleep(1.5)

        # Step 5: Add items to Cart
        print("[STEP 6] Adding 'Sauce Labs Onesie' ($7.99) & 'Sauce Labs Bike Light' ($9.99) to cart...")
        driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()
        time.sleep(1)
        driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()
        time.sleep(1)
        badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
        print(f"         ✓ Shopping Cart Badge count is now: {badge}")
        time.sleep(1.5)

        # Step 6: Open Cart
        print("[STEP 7] Clicking Shopping Cart Icon to view Cart Page...")
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        time.sleep(2)

        # Step 7: Proceed to Checkout
        print("[STEP 8] Clicking 'Checkout' button...")
        driver.find_element(By.ID, "checkout").click()
        time.sleep(1.5)

        # Step 8: Fill Checkout Form
        print("[STEP 9] Entering Customer Information:")
        first_name = wait.until(EC.visibility_of_element_located((By.ID, "first-name")))
        last_name = driver.find_element(By.ID, "last-name")
        postal_code = driver.find_element(By.ID, "postal-code")

        print("         -> First Name: 'Vishwa'")
        slow_type(first_name, "Vishwa")
        time.sleep(0.5)
        print("         -> Last Name: 'Kumar'")
        slow_type(last_name, "Kumar")
        time.sleep(0.5)
        print("         -> Postal Code: '400016'")
        slow_type(postal_code, "400016")
        time.sleep(1)

        print("[STEP 10] Clicking 'Continue' to review Order Overview...")
        driver.find_element(By.ID, "continue").click()
        time.sleep(2)

        # Step 9: Verify total & click Finish
        item_total = driver.find_element(By.CLASS_NAME, "summary_subtotal_label").text
        tax = driver.find_element(By.CLASS_NAME, "summary_tax_label").text
        total = driver.find_element(By.CLASS_NAME, "summary_total_label").text
        print(f"         ✓ Summary: {item_total} | {tax} | {total}")
        time.sleep(1.5)

        print("[STEP 11] Clicking 'Finish' button to complete purchase...")
        driver.find_element(By.ID, "finish").click()
        time.sleep(2)

        complete_header = driver.find_element(By.CLASS_NAME, "complete-header").text
        print(f"         ✓ ORDER STATUS: \"{complete_header}\"")
        time.sleep(2)

        # Step 10: Show BUG-01 (problem_user)
        print("\n" + "=" * 70)
        print("    DEMONSTRATING SEEDED DEFECT: BUG-001 (problem_user broken images)")
        print("=" * 70)
        print("[STEP 12] Logging out standard_user...")
        driver.find_element(By.ID, "react-burger-menu-btn").click()
        time.sleep(1)
        wait.until(EC.element_to_be_clickable((By.ID, "logout_sidebar_link"))).click()
        time.sleep(1.5)

        print("[STEP 13] Logging in as 'problem_user' to show defect on screen...")
        slow_type(driver.find_element(By.ID, "user-name"), "problem_user")
        time.sleep(0.5)
        slow_type(driver.find_element(By.ID, "password"), "secret_sauce")
        time.sleep(0.5)
        driver.find_element(By.ID, "login-button").click()
        time.sleep(2)

        images = driver.find_elements(By.CSS_SELECTOR, ".inventory_item_img img")
        broken_count = sum(1 for img in images if "sl-404" in img.get_attribute("src"))
        print(f"         ✓ BUG CAUGHT: {broken_count}/{len(images)} images are broken dog placeholder (sl-404)!")
        time.sleep(3)

        print("\n" + "=" * 70)
        print("    ✓ LIVE VISUAL DEMO COMPLETED SUCCESSFULLY!")
        print("    All actions executed automatically by Selenium WebDriver.")
        print("=" * 70)

    finally:
        print("\n[INFO] Closing browser in 3 seconds...")
        time.sleep(3)
        driver.quit()

if __name__ == "__main__":
    main()
