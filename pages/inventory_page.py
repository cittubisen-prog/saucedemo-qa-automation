from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
import time

class InventoryPage(BasePage):
    URL = "https://www.saucedemo.com/inventory.html"

    INVENTORY_ITEMS = (By.CLASS_NAME, "inventory_item")
    ITEM_NAMES = (By.CLASS_NAME, "inventory_item_name")
    ITEM_PRICES = (By.CLASS_NAME, "inventory_item_price")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")
    BURGER_MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")

    def get_product_count(self):
        return len(self.find_all(self.INVENTORY_ITEMS))

    def get_all_product_titles(self):
        elements = self.find_all(self.ITEM_NAMES)
        return [e.text for e in elements]

    def get_all_product_prices(self):
        elements = self.find_all(self.ITEM_PRICES)
        return [float(e.text.replace("$", "")) for e in elements]

    def add_product_to_cart(self, product_name):
        btn_id = "add-to-cart-" + product_name.lower().replace(" ", "-")
        try:
            btn = self.wait.until(EC.element_to_be_clickable((By.ID, btn_id)))
            btn.click()
            time.sleep(0.4)
            return True
        except Exception:
            items = self.find_all(self.INVENTORY_ITEMS)
            for item in items:
                name = item.find_element(By.CLASS_NAME, "inventory_item_name").text
                if name.lower() == product_name.lower():
                    btn = item.find_element(By.CSS_SELECTOR, "button.btn_inventory")
                    self.driver.execute_script("arguments[0].click();", btn)
                    time.sleep(0.4)
                    return True
            return False

    def remove_product_from_cart(self, product_name):
        btn_id = "remove-" + product_name.lower().replace(" ", "-")
        try:
            btn = self.wait.until(EC.element_to_be_clickable((By.ID, btn_id)))
            btn.click()
            time.sleep(0.4)
            return True
        except Exception:
            items = self.find_all(self.INVENTORY_ITEMS)
            for item in items:
                name = item.find_element(By.CLASS_NAME, "inventory_item_name").text
                if name.lower() == product_name.lower():
                    btn = item.find_element(By.CSS_SELECTOR, "button.btn_inventory")
                    self.driver.execute_script("arguments[0].click();", btn)
                    time.sleep(0.4)
                    return True
            return False

    def get_cart_count(self):
        end = time.time() + 2
        while time.time() < end:
            badges = self.driver.find_elements(*self.CART_BADGE)
            if badges and badges[0].is_displayed() and badges[0].text.strip():
                return int(badges[0].text.strip())
            time.sleep(0.1)
        badges = self.driver.find_elements(*self.CART_BADGE)
        if badges and badges[0].is_displayed() and badges[0].text.strip():
            return int(badges[0].text.strip())
        return 0

    def open_cart(self):
        try:
            self.click(self.CART_LINK)
        except Exception:
            el = self.find(self.CART_LINK)
            self.driver.execute_script("arguments[0].click();", el)
        
        try:
            WebDriverWait(self.driver, 4).until(EC.url_contains("cart.html"))
        except Exception:
            el = self.find(self.CART_LINK)
            self.driver.execute_script("arguments[0].click();", el)
            try:
                WebDriverWait(self.driver, 4).until(EC.url_contains("cart.html"))
            except Exception:
                self.driver.get("https://www.saucedemo.com/cart.html")
        time.sleep(0.3)

    def sort_by(self, sort_value):
        select = Select(self.find(self.SORT_DROPDOWN))
        select.select_by_value(sort_value)

    def logout(self):
        self.click(self.BURGER_MENU_BUTTON)
        self.click(self.LOGOUT_LINK)
