import os
import pytest
import tempfile
import uuid
import shutil
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.edge.service import Service as EdgeService
import time


def pytest_addoption(parser):
    """Add command-line options for browser selection"""
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser to run tests: chrome, edge (default: chrome)"
    )


def _get_edge_driver_path():
    """
    Find Edge driver in multiple locations.
    Returns the path to msedgedriver.exe or None if not found.
    """
    # Get project root (go up 2 levels from src/seleniumProject/)
    project_root = Path(__file__).parent.parent.parent

    # List of possible locations
    possible_paths = [
        # Project drivers folder with edgedriver_win64 subfolder
        project_root / "drivers" / "edgedriver_win64" / "msedgedriver.exe",
        # Project drivers folder (direct)
        project_root / "drivers" / "msedgedriver.exe",
        # Common WebDriver location
        Path("C:/WebDrivers/msedgedriver.exe"),
        # User's local folder
        Path.home() / "WebDrivers" / "msedgedriver.exe",
        # Current directory
        Path("msedgedriver.exe"),
    ]

    # Check if driver is in PATH
    import shutil as sh
    path_driver = sh.which("msedgedriver")
    if path_driver:
        print(f"✓ Found Edge driver in PATH: {path_driver}")
        return path_driver

    # Check predefined locations
    for path in possible_paths:
        if path.exists() and path.is_file():
            print(f"✓ Found Edge driver at: {path}")
            return str(path)

    # Debug output
    print("✗ Edge driver not found. Searched locations:")
    for path in possible_paths:
        status = "EXISTS" if path.exists() else "NOT FOUND"
        print(f"  [{status}] {path}")

    return None


def _build_chrome(headless: bool) -> webdriver.Chrome:
    """Build Chrome driver with temporary profile"""
    options = ChromeOptions()
    # unique profile per test
    profile = tempfile.mkdtemp(prefix=f"chrome_{uuid.uuid4().hex}_")
    options.add_argument(f"--user-data-dir={profile}")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1440,900")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)

    if headless:
        options.add_argument("--headless=new")

    driver = webdriver.Chrome(options=options)

    # clean-up hook (executed even if test crashes)
    def _cleanup():
        try:
            driver.quit()
        except Exception as e:
            print(f"Error quitting Chrome driver: {e}")
        finally:
            shutil.rmtree(profile, ignore_errors=True)

    import atexit
    atexit.register(_cleanup)
    return driver


def _build_edge(headless: bool) -> webdriver.Edge:
    """Build Edge driver with temporary profile"""
    options = EdgeOptions()
    # unique profile per test
    profile = tempfile.mkdtemp(prefix=f"edge_{uuid.uuid4().hex}_")
    options.add_argument(f"--user-data-dir={profile}")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1440,900")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)

    if headless:
        options.add_argument("--headless=new")

    # Try to find Edge driver manually first
    driver_path = _get_edge_driver_path()

    if driver_path:
        # Use manually downloaded driver
        print(f"→ Using Edge driver from: {driver_path}")
        service = EdgeService(executable_path=driver_path)
        driver = webdriver.Edge(service=service, options=options)
    else:
        # Provide helpful error message
        project_root = Path(__file__).parent.parent.parent
        error_msg = f"""
╔════════════════════════════════════════════════════════════════╗
║                   Edge Driver Not Found!                       ║
╚════════════════════════════════════════════════════════════════╝

The driver should be at:
  {project_root / 'drivers' / 'edgedriver_win64' / 'msedgedriver.exe'}

Current structure detected:
  {project_root / 'drivers' / 'edgedriver_win64' / 'msedgedriver.exe'}

If the file exists but wasn't found, try:
1. Move msedgedriver.exe directly to:
   {project_root / 'drivers' / 'msedgedriver.exe'}

2. Or run from PowerShell:
   Move-Item "drivers\\edgedriver_win64\\msedgedriver.exe" "drivers\\msedgedriver.exe"

Your Edge version: 141.0.3537.85
Driver download: https://msedgedriver.azureedge.net/141.0.3537.85/edgedriver_win64.zip
        """
        raise FileNotFoundError(error_msg)

    # clean-up hook (executed even if test crashes)
    def _cleanup():
        try:
            driver.quit()
        except Exception as e:
            print(f"Error quitting Edge driver: {e}")
        finally:
            shutil.rmtree(profile, ignore_errors=True)

    import atexit
    atexit.register(_cleanup)
    return driver


# ---------- Fixtures ----------
@pytest.fixture(scope="session")
def base_url() -> str:
    """Base URL for the application under test"""
    return os.getenv("BASE_URL", "https://www.saucedemo.com")


@pytest.fixture(scope="session")
def headless() -> bool:
    """Determine if browser should run in headless mode"""
    return os.getenv("HEADLESS", "false").lower() in {"1", "true", "yes", "on"}


@pytest.fixture(scope="function")
def driver(request, headless: bool):
    """
    WebDriver fixture with browser selection support.

    Usage:
        pytest --browser=chrome (default)
        pytest --browser=edge

    Environment variables:
        HEADLESS=true/false (default: false)
        BASE_URL=<url> (default: https://www.saucedemo.com)
    """
    browser = request.config.getoption("--browser").lower()

    if browser == "chrome":
        driver_instance = _build_chrome(headless=headless)
    elif browser == "edge":
        driver_instance = _build_edge(headless=headless)
    else:
        raise ValueError(
            f"Unsupported browser: {browser}. "
            f"Supported browsers: chrome, edge"
        )

    driver_instance.implicitly_wait(2)

    yield driver_instance

    # driver.quit() is already handled by atexit in build functions


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_setup(item):
    """Hook to print test name before execution"""
    print(f"\n=== Executing test: {item.nodeid} ===")
    time.sleep(0.5)
    yield


@pytest.fixture(autouse=True)
def visual_pause():
    """Pause after each test for visual verification"""
    yield
    time.sleep(0.5)