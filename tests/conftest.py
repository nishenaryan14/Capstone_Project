import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


def _build_chrome(headless: bool) -> webdriver.Chrome:
    options = ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1440,900")
    if headless:
        options.add_argument("--headless=new")
    service = ChromeService(ChromeDriverManager().install())
    return webdriver.Chrome(service=service, options=options)


@pytest.fixture(scope="session")
def base_url() -> str:
    return os.getenv("BASE_URL", "https://demo.nopcommerce.com")


@pytest.fixture(scope="session")
def headless() -> bool:
    return os.getenv("HEADLESS", "true").lower() in {"1", "true", "yes", "on"}


@pytest.fixture(scope="function")
def driver(headless: bool):
    driver = _build_chrome(headless=headless)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


