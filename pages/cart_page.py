from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
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
        try:
            return len(self.find_all(self.CART_ITEMS))
        except Exception:
            return 0

    def get_cart_item_names(self):
        end = time.time() + 3
        while time.time() < end:
            try:
                elements = self.driver.find_elements(*self.ITEM_NAMES)
                names = [e.text.strip() for e in elements if e.text.strip()]
                if names:
                    return names
            except Exception:
                pass
            time.sleep(0.2)
        try:
            elements = self.driver.find_elements(*self.ITEM_NAMES)
            return [e.text.strip() for e in elements if e.text.strip()]
        except Exception:
            return []

    def remove_item(self, item_name):
        items = self.find_all(self.CART_ITEMS)
        for item in items:
            name = item.find_element(By.CLASS_NAME, "inventory_item_name").text
            if name.lower() == item_name.lower():
                item.find_element(By.CSS_SELECTOR, "button.cart_button").click()
                time.sleep(0.3)
                return True
        return False

    def click_checkout(self):
        try:
            self.click(self.CHECKOUT_BUTTON)
        except Exception:
            el = self.find(self.CHECKOUT_BUTTON)
            self.driver.execute_script("arguments[0].click();", el)
        try:
            WebDriverWait(self.driver, 4).until(EC.url_contains("checkout-step-one.html"))
        except Exception:
            pass

    def continue_shopping(self):
        try:
            self.click(self.CONTINUE_SHOPPING_BUTTON)
        except Exception:
            el = self.find(self.CONTINUE_SHOPPING_BUTTON)
            self.driver.execute_script("arguments[0].click();", el)
        try:
            WebDriverWait(self.driver, 4).until(EC.url_contains("inventory.html"))
        except Exception:
            pass
