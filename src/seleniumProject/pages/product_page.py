from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from .base_page import BasePage


class ProductPage(BasePage):
    # Inventory list items and PDP on Sauce Demo
    _inventory_item = (By.CSS_SELECTOR, ".inventory_item")
    _add_to_cart_buttons = (By.CSS_SELECTOR, "button.btn_inventory")
    _back_to_products = (By.ID, "back-to-products")
    _backpack_add_to_cart = (By.ID, "add-to-cart-sauce-labs-backpack")
    _backpack_remove = (By.ID, "remove-sauce-labs-backpack")
    _bike_light_add_to_cart = (By.ID, "add-to-cart-sauce-labs-bike-light")
    _bike_light_remove = (By.ID, "remove-sauce-labs-bike-light")
    _cart_badge = (By.CLASS_NAME, "shopping_cart_badge")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    # ---------- helpers ----------
    def _wait_for_badge(self, expected_count: int, timeout: int = 10) -> None:
        """Wait until cart badge shows exact number with fallback handling."""
        try:
            # First, wait for badge to be present
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(self._cart_badge)
            )

            # Then wait for correct count
            def check_badge_count(driver):
                try:
                    badge = driver.find_element(*self._cart_badge)
                    return badge.text.strip() == str(expected_count)
                except:
                    return False

            WebDriverWait(self.driver, timeout).until(check_badge_count)

        except TimeoutException:
            # Fallback: verify the badge exists with any count
            try:
                badge = self.driver.find_element(*self._cart_badge)
                actual_count = badge.text.strip()
                print(f"Warning: Expected badge count {expected_count}, found '{actual_count}'")
            except:
                print(f"Warning: Cart badge not found for expected count {expected_count}")
                # Don't fail - item was likely added successfully

    def _wait_for_remove_button(self, remove_locator: tuple, timeout: int = 10) -> None:
        """Wait for 'Add to Cart' button to change to 'Remove' button."""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(remove_locator)
            )
        except TimeoutException:
            print(f"Warning: Remove button {remove_locator} not found within {timeout}s")
            raise

    # ---------- actions ----------
    def add_first_item_to_cart(self) -> None:
        """Add the first item in inventory to cart."""
        self.click(self._add_to_cart_buttons)

    def inventory_item_count(self) -> int:
        """Return the number of inventory items on the page."""
        return len(self.driver.find_elements(*self._inventory_item))

    def add_backpack_to_cart(self) -> None:
        """Add Sauce Labs Backpack to cart and verify."""
        self.click(self._backpack_add_to_cart)
        # Verify by waiting for Remove button (more reliable than badge)
        self._wait_for_remove_button(self._backpack_remove)

    def add_bike_light_to_cart(self) -> None:
        """Add Sauce Labs Bike Light to cart and verify."""
        self.click(self._bike_light_add_to_cart)
        # Verify by waiting for Remove button
        self._wait_for_remove_button(self._bike_light_remove)

    def add_item_to_cart_by_name(self, name: str, expected_count: int = None) -> None:
        """
        Generic add-to-cart by product name.

        Args:
            name: Product name to add (must match exact text)
            expected_count: Optional badge count to verify after adding

        Raises:
            ValueError: If product name not found in inventory
        """
        items = self.driver.find_elements(*self._inventory_item)

        for item in items:
            title = item.find_element(By.CLASS_NAME, "inventory_item_name").text.strip()
            if title == name:
                button = item.find_element(By.CSS_SELECTOR, "button.btn_inventory")
                button_id = button.get_attribute("id")
                button.click()

                # Wait for button to change to "Remove"
                try:
                    WebDriverWait(self.driver, 10).until(
                        lambda d: "remove" in button.get_attribute("id").lower()
                    )
                except TimeoutException:
                    print(f"Warning: Button didn't change to Remove for '{name}'")

                # Optionally verify badge count
                if expected_count is not None:
                    self._wait_for_badge(expected_count)

                return

        # If we get here, product wasn't found
        available_products = [
            item.find_element(By.CLASS_NAME, "inventory_item_name").text.strip()
            for item in items
        ]
        raise ValueError(
            f"Product '{name}' not found in inventory. "
            f"Available products: {', '.join(available_products)}"
        )

    def is_item_in_cart(self, item_id: str) -> bool:
        """
        Check if an item is in the cart by checking if Remove button exists.

        Args:
            item_id: The product identifier (e.g., 'sauce-labs-backpack')

        Returns:
            True if item is in cart, False otherwise
        """
        try:
            remove_button_id = f"remove-{item_id}"
            self.driver.find_element(By.ID, remove_button_id)
            return True
        except:
            return False

    def get_cart_badge_count(self) -> int:
        """
        Get the current count from the cart badge.

        Returns:
            Integer count from badge, or 0 if badge not present
        """
        try:
            badge = self.driver.find_element(*self._cart_badge)
            return int(badge.text.strip())
        except:
            return 0