from __future__ import annotations

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class LoginPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    # Locators
    _email = (By.ID, "Email")
    _password = (By.ID, "Password")
    _remember_me = (By.ID, "RememberMe")
    _login_button = (By.CSS_SELECTOR, "button.login-button")
    _forgot_password_link = (By.LINK_TEXT, "Forgot password?")
    _validation_summary = (By.CSS_SELECTOR, "div.message-error.validation-summary-errors")
    _field_validation_errors = (By.CSS_SELECTOR, "span.field-validation-error")

    def open(self, base_url: str) -> "LoginPage":
        self.driver.get(f"{base_url}/login")
        return self

    def set_email(self, email: str) -> "LoginPage":
        el = self.driver.find_element(*self._email)
        el.clear()
        el.send_keys(email)
        return self

    def set_password(self, password: str) -> "LoginPage":
        el = self.driver.find_element(*self._password)
        el.clear()
        el.send_keys(password)
        return self

    def toggle_remember_me(self, check: bool = True) -> "LoginPage":
        el = self.driver.find_element(*self._remember_me)
        if el.is_selected() != check:
            el.click()
        return self

    def submit(self) -> None:
        self.driver.find_element(*self._login_button).click()

    def click_forgot_password(self) -> None:
        self.driver.find_element(*self._forgot_password_link).click()

    def get_summary_error_text(self) -> str:
        try:
            return self.driver.find_element(*self._validation_summary).text.strip()
        except Exception:
            return ""

    def get_field_error_texts(self) -> list[str]:
        return [e.text.strip() for e in self.driver.find_elements(*self._field_validation_errors)]


