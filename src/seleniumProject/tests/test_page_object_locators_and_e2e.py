import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.seleniumProject.pages.login_page import LoginPage
from src.seleniumProject.pages.home_page import HomePage
from src.seleniumProject.pages.product_page import ProductPage
from src.seleniumProject.pages.cart_page import CartPage
from src.seleniumProject.pages.checkout_page import CheckoutPage


def test_locators_and_methods_on_login(driver, base_url):
    """Test basic login functionality using page objects"""
    page = LoginPage(driver).open(base_url)
    username = driver.find_element("id", "user-name")
    password = driver.find_element("id", "password")
    assert username.is_displayed() and password.is_displayed()
    page.set_username("standard_user").set_password("secret_sauce").submit()


@pytest.mark.selenium_topics
def test_saucedemo_twelve_locators(driver, base_url):
    """
    login → interact with product page → checkout → logout
    """
    # Initialize page objects
    login_page = LoginPage(driver)
    home_page = HomePage(driver)
    product_page = ProductPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    # 1-3. Login using page object
    login_page.open(base_url)
    login_page.set_username("standard_user")
    login_page.set_password("secret_sauce")
    login_page.submit()
    login_page.screenshot("01_after_login")

    time.sleep(3)

    # 4. Add to cart by ID using page object
    product_page.add_backpack_to_cart()
    product_page.screenshot("02_backpack_added")

    # 5. Add another item by ID
    product_page.add_bike_light_to_cart()
    product_page.screenshot("03_bike_light_added")

    # 6. Open cart using home page
    time.sleep(2)
    home_page.go_to_cart()
    home_page.screenshot("04_in_cart")

    # 7-8. Wait for and verify cart items using page object
    cart_page.wait_for_cart_items()
    names = cart_page.get_cart_item_names()
    try:
        assert "Sauce Labs Backpack" in names
        assert any("Bike Light" in n for n in names)
    except AssertionError:
        cart_page.screenshot("05_cart_assert_failed")
        raise
    cart_page.screenshot("05_cart_verified")

    # 9. Checkout using page object
    cart_page.click_checkout()
    cart_page.screenshot("06_checkout_clicked")

    # 10. Wait for checkout form and fill information
    checkout_page.wait_for_checkout_form()
    checkout_page.fill_information("Aryan", "Tester", "12345")
    checkout_page.screenshot("07_checkout_filled")

    # 11. Finish checkout
    checkout_page.finish()
    checkout_page.screenshot("08_finished")

    # 12. Verify completion
    assert checkout_page.is_completed()
    checkout_page.screenshot("09_completion_verified")

    # Logout via burger menu
    driver.find_element(By.ID, "react-burger-menu-btn").click()
    driver.find_element(By.LINK_TEXT, "Logout").click()
    login_page.screenshot("10_after_logout")

    # Verify back on login page
    assert login_page.exists((By.ID, "user-name"))
    login_page.screenshot("11_final_login_page")

    print("SauceDemo – 12 locator strategies completed (page-object version)")