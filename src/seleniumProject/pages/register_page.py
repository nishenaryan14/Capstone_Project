from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from .base_page import BasePage


class RegisterPage(BasePage):
    # Not applicable for Sauce Demo; keep placeholder for compatibility
    def __init__(self, driver: WebDriver):
        super().__init__(driver)

