import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from .base_page import BasePage


class CheckoutPage(BasePage):
    _first_name = (By.ID, "first-name")
    _last_name = (By.ID, "last-name")
    _postal_code = (By.ID, "postal-code")
    _continue = (By.ID, "continue")
    _finish = (By.ID, "finish")
    _complete_header = (By.CSS_SELECTOR, "h2.complete-header")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def fill_information(self, first: str, last: str, postal: str) -> None:
        self.type(self._first_name, first)
        self.type(self._last_name, last)
        self.type(self._postal_code, postal)
        self.click(self._continue)

    def finish(self) -> None:
        self.click(self._finish)

    def is_completed(self) -> bool:
        return self.exists(self._complete_header)

    def wait_for_checkout_form(self) -> None:
        """Wait for checkout form to be visible"""
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self._first_name)
        )
        time.sleep(3)
        self.accept_alert()


