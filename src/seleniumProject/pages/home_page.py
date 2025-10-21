from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from .base_page import BasePage


class HomePage(BasePage):
    # Inventory page after login
    _inventory_container = (By.ID, "inventory_container")
    _cart_icon = (By.CLASS_NAME, "shopping_cart_link")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def is_loaded(self) -> bool:
        return self.exists(self._inventory_container)

    def go_to_cart(self) -> None:
        self.driver.find_element(*self._cart_icon).click()


