import os
import pytest
import tempfile
import uuid
import shutil
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time


def _build_chrome(headless: bool) -> webdriver.Chrome:
    options = ChromeOptions()
    # unique profile per test
    profile = tempfile.mkdtemp(prefix=f"chrome_{uuid.uuid4().hex}_")
    options.add_argument(f"--user-data-dir={profile}")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1440,900")
    if headless:
        options.add_argument("--headless=new")

    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    # clean-up hook (executed even if test crashes)
    def _cleanup():
        driver.quit()
        shutil.rmtree(profile, ignore_errors=True)

    import atexit
    atexit.register(_cleanup)
    return driver


# ---------- rest of your conftest is untouched ----------
@pytest.fixture(scope="session")
def base_url() -> str:
    return os.getenv("BASE_URL", "https://www.saucedemo.com")


@pytest.fixture(scope="session")
def headless() -> bool:
    return os.getenv("HEADLESS", "false").lower() in {"1", "true", "yes", "on"}


@pytest.fixture(scope="function")
def driver(headless: bool):
    driver = _build_chrome(headless=headless)
    driver.implicitly_wait(2)
    yield driver
    # driver.quit() is already called by atexit – safe to keep or remove


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_setup(item):
    print(f"\n=== Executing test: {item.nodeid} ===")
    time.sleep(1)
    yield


@pytest.fixture(autouse=True)
def visual_pause():
    yield
    time.sleep(1)