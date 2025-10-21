from __future__ import annotations
from typing import Tuple
from selenium.common import TimeoutException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, os

class BasePage:
    def __init__(self, driver: WebDriver, timeout: int = 10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self, url: str) -> None:
        self.driver.get(url)

    def click(self, locator: Tuple[str, str]) -> None:
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def js_click(self, locator: Tuple[str, str]) -> None:
        el = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].click();", el)

    def type(self, locator: Tuple[str, str], text: str | None, clear: bool = True) -> None:
        el = self.wait.until(EC.visibility_of_element_located(locator))
        if clear:
            el.clear()
        el.send_keys(text or "")

    def text_of(self, locator: Tuple[str, str]) -> str:
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    def exists(self, locator: Tuple[str, str]) -> bool:
        try:
            self.driver.find_element(*locator)
            return True
        except Exception:
            return False

    def accept_alert(self, timeout: int = 5) -> str:
        """
        Wait for a JS alert to appear, return its text, and accept it.
        """
        try:
            alert = WebDriverWait(self.driver, timeout).until(EC.alert_is_present())
            text = alert.text
            alert.accept()
            return text
        except TimeoutException:
            return ""

    def screenshot(self, name: str) -> str:
        """Save PNG to screenshots/ and return absolute path."""
        os.makedirs("screenshots", exist_ok=True)
        file_name = f"screenshots/{name}_{int(time.time())}.png"
        self.driver.save_screenshot(file_name)
        return os.path.abspath(file_name)