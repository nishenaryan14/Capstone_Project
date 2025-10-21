from __future__ import annotations

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from .base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    # Sauce Demo locators
    _username = (By.ID, "user-name")
    _password = (By.ID, "password")
    _login_button = (By.ID, "login-button")
    _error = (By.CSS_SELECTOR, "h3[data-test='error']")

    def open(self, base_url: str) -> "LoginPage":
        self.driver.get(base_url)
        return self

    def set_username(self, username: str) -> "LoginPage":
        self.type(self._username, username)
        return self

    def set_password(self, password: str) -> "LoginPage":
        self.type(self._password, password)
        return self

    def submit(self) -> None:
        self.click(self._login_button)

    def login_with(self, username: str, password: str) -> None:
        """Single-call login."""
        self.set_username(username).set_password(password).submit()

    def is_login_successful(self) -> bool:
        return "inventory" in self.driver.current_url

    def get_error_text(self) -> str:
        return self.error_text()

    def error_text(self) -> str:
        try:
            return self.driver.find_element(*self._error).get_attribute("textContent").strip()
        except Exception:
            return ""