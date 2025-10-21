import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from src.seleniumProject.pages.login_page import LoginPage
from utils.excel_reader import read_excel

# ----------  read data once  ----------
excel_file = "test_data/login_data.xlsx"
test_data = read_excel(excel_file, "LoginTests")

# ----------  fixture  ----------
@pytest.fixture(scope="function")
def driver():
    service = ChromeService(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    d = webdriver.Chrome(service=service, options=options)
    yield d
    d.quit()

# ----------  data-driven test  ----------
@pytest.mark.parametrize("row", test_data, ids=[r["TestCaseID"] for r in test_data])
def test_login_hybrid(driver, row):
    login_page = LoginPage(driver)
    login_page.open("https://www.saucedemo.com")

    # implementation
    login_page.login_with(row["Username"], row["Password"])

    # assertion
    actual = "Success" if login_page.is_login_successful() else "Error"
    expected = row["ExpectedResult"]

    if actual != expected:
        login_page.screenshot(row["TestCaseID"])
        pytest.fail(f"{row['TestCaseID']}: expected {expected}, got {actual} – {login_page.get_error_text()}")