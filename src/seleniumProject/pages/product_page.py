from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from .base_page import BasePage


class ProductPage(BasePage):
    # Inventory list items and PDP on Sauce Demo
    _inventory_item = (By.CSS_SELECTOR, ".inventory_item")
    _add_to_cart_buttons = (By.CSS_SELECTOR, "button.btn_inventory")
    _back_to_products = (By.ID, "back-to-products")
    _backpack_add_to_cart = (By.ID, "add-to-cart-sauce-labs-backpack")
    _bike_light_add_to_cart = (By.ID, "add-to-cart-sauce-labs-bike-light")  # FIXED

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    # ---------- helpers ----------
    def _wait_for_badge(self, expected_count: int) -> None:
        """Wait until cart badge shows exact number."""
        WebDriverWait(self.driver, 10).until(
            lambda d: d.find_element(By.CLASS_NAME, "shopping_cart_badge").text == str(expected_count)
        )

    # ---------- actions ----------
    def add_first_item_to_cart(self) -> None:
        self.click(self._add_to_cart_buttons)

    def inventory_item_count(self) -> int:
        return len(self.driver.find_elements(*self._inventory_item))

    def add_backpack_to_cart(self) -> None:
        self.click(self._backpack_add_to_cart)
        self._wait_for_badge(1)

    def add_bike_light_to_cart(self) -> None:
        self.click(self._bike_light_add_to_cart)
        self._wait_for_badge(2)

    def add_item_to_cart_by_name(self, name: str, expected_count: int = None) -> None:
        """Generic add-to-cart by product name. Optionally wait for badge count."""
        items = self.driver.find_elements(*self._inventory_item)
        for item in items:
            title = item.find_element(By.CLASS_NAME, "inventory_item_name").text.strip()
            if title == name:
                item.find_element(By.CSS_SELECTOR, "button.btn_inventory").click()
                if expected_count is not None:
                    self._wait_for_badge(expected_count)
                return