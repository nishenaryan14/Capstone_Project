import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.seleniumProject.pages.login_page import LoginPage
from src.seleniumProject.pages.home_page import HomePage


def test_login_valid_user(driver, base_url):
    LoginPage(driver).open(base_url)\
        .set_username("standard_user")\
        .set_password("secret_sauce")\
        .submit()
    assert HomePage(driver).is_loaded()

@pytest.mark.selenium_topics
def test_explicit_wait_for_cart_notification(driver, base_url):
    driver.get(f"{base_url}/apple-macbook-pro-13-inch")
    add_to_cart = driver.find_element(By.ID, "add-to-cart-button-4")
    add_to_cart.click()

    # Wait for the success bar notification to appear and disappear
    wait = WebDriverWait(driver, 10)
    success_bar = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.bar-notification.success")))
    assert "The product has been added" in success_bar.text
    wait.until(EC.invisibility_of_element(success_bar))


