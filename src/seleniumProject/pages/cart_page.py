from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage


class CartPage(BasePage):
    _cart_list = (By.CSS_SELECTOR, ".cart_list .cart_item")
    _checkout_button = (By.XPATH, "/html/body/div/div/div/div[2]/div/div[2]/button[2]")
    _cart_item_names = (By.CSS_SELECTOR, ".cart_item .inventory_item_name")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    # ----------  new helper ----------
    def wait_for_cart_rows(self, count: int = 2) -> None:
        """Wait until exactly <count> cart rows are present."""
        WebDriverWait(self.driver, 10).until(
            lambda d: len(d.find_elements(*self._cart_list)) == count
        )

    def row_count(self) -> int:
        return len(self.driver.find_elements(*self._cart_list))

    def click_checkout(self) -> None:
        self.js_click(self._checkout_button)

    def get_cart_item_names(self) -> list[str]:
        elements = self.driver.find_elements(*self._cart_item_names)
        return [elem.text.strip() for elem in elements]

    # kept for backward compatibility – delegates to new helper
    def wait_for_cart_items(self) -> None:
        self.wait_for_cart_rows(2)   # default 2 items