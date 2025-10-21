from __future__ import annotations
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from src.seleniumProject.pages.base_page import BasePage


class ProductDetailPage(BasePage):
    """Product-detail page (opens in new tab)."""

    _add_to_cart_btn   = (By.ID, "add-to-cart-sauce-labs-backpack")
    _inventory_item_id = (By.CLASS_NAME, "inventory_details_name")

    def is_detail_page_loaded(self) -> bool:
        return self.exists(self._inventory_item_id)

    def add_to_cart_in_new_tab(self) -> None:
        self.click(self._add_to_cart_btn)

    def get_item_id_from_url(self) -> str:
        """Extract id=... from current URL."""
        return self.driver.current_url.split("id=")[-1]