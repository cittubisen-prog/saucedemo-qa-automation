from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
import time

class CartPage(BasePage):
    URL = "https://www.saucedemo.com/cart.html"

    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    ITEM_NAMES = (By.CSS_SELECTOR, ".cart_item .inventory_item_name")
    CHECKOUT_BUTTON = (By.ID, "checkout")
    CONTINUE_SHOPPING_BUTTON = (By.ID, "continue-shopping")

    def get_cart_items_count(self):
        self.wait.until(EC.url_contains("cart.html"))
        try:
            return len(self.find_all(self.CART_ITEMS))
        except Exception:
            return 0

    def get_cart_item_names(self):
        self.wait.until(EC.url_contains("cart.html"))
        time.sleep(0.5)
        try:
            elements = self.find_all(self.ITEM_NAMES)
            return [e.text for e in elements]
        except Exception:
            elements = self.driver.find_elements(*self.ITEM_NAMES)
            return [e.text for e in elements]

    def remove_item(self, item_name):
        self.wait.until(EC.url_contains("cart.html"))
        items = self.find_all(self.CART_ITEMS)
        for item in items:
            name = item.find_element(By.CLASS_NAME, "inventory_item_name").text
            if name.lower() == item_name.lower():
                item.find_element(By.CSS_SELECTOR, "button.cart_button").click()
                time.sleep(0.3)
                return True
        return False

    def click_checkout(self):
        self.wait.until(EC.url_contains("cart.html"))
        self.click(self.CHECKOUT_BUTTON)

    def continue_shopping(self):
        self.wait.until(EC.url_contains("cart.html"))
        self.click(self.CONTINUE_SHOPPING_BUTTON)
        self.wait.until(EC.url_contains("inventory.html"))
