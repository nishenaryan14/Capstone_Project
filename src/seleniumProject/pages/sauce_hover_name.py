from __future__ import annotations
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from src.seleniumProject.pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

class SauceHoverNamePage(BasePage):
    """Real hover on SauceDemo: item name link colour changes."""

    _item_name_link = (By.CSS_SELECTOR, ".inventory_item:first-child .inventory_item_name")

    def hover_item_name(self) -> None:
        link = self.wait.until(EC.element_to_be_clickable(self._item_name_link))
        ActionChains(self.driver).move_to_element(link).perform()

    def name_link_colour(self) -> str:
        return self.driver.find_element(*self._item_name_link).value_of_css_property("color")

    def colour_changed_after_hover(self, before: str) -> bool:
        after = self.name_link_colour()
        return after != before