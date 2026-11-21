from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import time

class CheckoutPage(BasePage):
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    CANCEL_BUTTON = (By.ID, "cancel")
    ERROR_CONTAINER = (By.CSS_SELECTOR, "h3[data-test='error']")

    FINISH_BUTTON = (By.ID, "finish")
    SUBTOTAL_LABEL = (By.CLASS_NAME, "summary_subtotal_label")
    TAX_LABEL = (By.CLASS_NAME, "summary_tax_label")
    TOTAL_LABEL = (By.CLASS_NAME, "summary_total_label")
    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")
    BACK_HOME_BUTTON = (By.ID, "back-to-products")

    def fill_checkout_info(self, first_name="", last_name="", postal_code=""):
        if first_name:
            self.type_text(self.FIRST_NAME_INPUT, first_name)
        if last_name:
            self.type_text(self.LAST_NAME_INPUT, last_name)
        if postal_code:
            self.type_text(self.POSTAL_CODE_INPUT, postal_code)
        self.click(self.CONTINUE_BUTTON)
        time.sleep(0.5)

    def get_error_message(self):
        return self.get_text(self.ERROR_CONTAINER)

    def click_finish(self):
        self.click(self.FINISH_BUTTON)
        time.sleep(0.5)

    def is_order_complete(self):
        return self.is_displayed(self.COMPLETE_HEADER) and "thank you" in self.get_text(self.COMPLETE_HEADER).lower()

    def get_order_complete_text(self):
        return self.get_text(self.COMPLETE_HEADER)
