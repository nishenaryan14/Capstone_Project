from __future__ import annotations
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from src.seleniumProject.pages.base_page import BasePage


class SauceSidebarPage(BasePage):
    """Sidebar (burger menu) actions."""
    _menu_btn      = (By.ID, "react-burger-menu-btn")
    _about_link    = (By.ID, "about_sidebar_link")
    _logout_link   = (By.ID, "logout_sidebar_link")

    def open_sidebar(self) -> None:
        self.click(self._menu_btn)

    def right_click_about(self) -> None:
        about = self.wait.until(EC.element_to_be_clickable(self._about_link))
        ActionChains(self.driver).context_click(about).perform()

    def click_logout(self) -> None:
        self.click(self._logout_link)

    def is_sidebar_open(self) -> bool:
        return self.exists(self._logout_link)