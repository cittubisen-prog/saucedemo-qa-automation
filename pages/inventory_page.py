from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
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
            self.click((By.ID, btn_id))
            time.sleep(0.5)
            return True
        except Exception:
            items = self.find_all(self.INVENTORY_ITEMS)
            for item in items:
                name = item.find_element(By.CLASS_NAME, "inventory_item_name").text
                if name.lower() == product_name.lower():
                    item.find_element(By.CSS_SELECTOR, "button.btn_inventory").click()
                    time.sleep(0.5)
                    return True
            return False

    def remove_product_from_cart(self, product_name):
        btn_id = "remove-" + product_name.lower().replace(" ", "-")
        try:
            self.click((By.ID, btn_id))
            time.sleep(0.5)
            return True
        except Exception:
            items = self.find_all(self.INVENTORY_ITEMS)
            for item in items:
                name = item.find_element(By.CLASS_NAME, "inventory_item_name").text
                if name.lower() == product_name.lower():
                    item.find_element(By.CSS_SELECTOR, "button.btn_inventory").click()
                    time.sleep(0.5)
                    return True
            return False

    def get_cart_count(self):
        badges = self.driver.find_elements(*self.CART_BADGE)
        if badges and badges[0].is_displayed():
            return int(badges[0].text)
        return 0

    def open_cart(self):
        self.click(self.CART_LINK)

    def sort_by(self, sort_value):
        select = Select(self.find(self.SORT_DROPDOWN))
        select.select_by_value(sort_value)

    def logout(self):
        self.click(self.BURGER_MENU_BUTTON)
        self.click(self.LOGOUT_LINK)
