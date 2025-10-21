import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from src.seleniumProject.pages.login_page import LoginPage
from src.seleniumProject.pages.home_page import HomePage


@pytest.mark.selenium_topics
def test_js_executor_scroll_dropdown(driver):
    """JS executor examples + scroll + drop-down on SauceDemo."""
    login_page = LoginPage(driver)
    home_page = HomePage(driver)

    # 1. Login
    login_page.open("https://www.saucedemo.com")
    login_page.login_with("standard_user", "secret_sauce")
    login_page.screenshot("01_logged_in")

    # 2. Verify inventory page loaded
    assert home_page.is_loaded()
    home_page.screenshot("02_inventory_loaded")

    # 3. ---- JS SCROLL TO BOTTOM ----
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)
    home_page.screenshot("03_scroll_bottom_js")

    # 4. ---- JS SCROLL TO TOP ----
    driver.execute_script("window.scrollTo(0, 0);")
    time.sleep(1)
    home_page.screenshot("04_scroll_top_js")

    # 5. ---- JS SCROLL TO SPECIFIC ELEMENT (footer) ----
    footer = driver.find_element(By.CLASS_NAME, "footer")
    driver.execute_script("arguments[0].scrollIntoView();", footer)
    time.sleep(1)
    home_page.screenshot("05_scroll_to_footer_js")

    # 6. ---- JS HIGHLIGHT ELEMENT ----
    product = driver.find_element(By.CLASS_NAME, "inventory_item_name")
    driver.execute_script("arguments[0].style.border='3px solid red'", product)
    time.sleep(1)
    home_page.screenshot("06_highlight_product_js")

    # 7. ---- JS CLICK (burger menu) ----
    menu_btn = driver.find_element(By.ID, "react-burger-menu-btn")
    driver.execute_script("arguments[0].click();", menu_btn)
    time.sleep(1)
    home_page.screenshot("07_menu_clicked_js")

    # 8. ---- JS GET PAGE TITLE ----
    title = driver.execute_script("return document.title;")
    print(f"Page title via JS: {title}")

    # 9. ---- JS GET PAGE URL ----
    url = driver.execute_script("return document.URL;")
    print(f"Page URL via JS: {url}")

    # 10. ---- KEYBOARD PAGE DOWN ----
    driver.find_element(By.TAG_NAME, "body").send_keys(Keys.PAGE_DOWN)
    time.sleep(1)
    home_page.screenshot("08_page_down_keyboard")

    # 11. ---- KEYBOARD PAGE UP ----
    driver.find_element(By.TAG_NAME, "body").send_keys(Keys.PAGE_UP)
    time.sleep(1)
    home_page.screenshot("09_page_up_keyboard")

    # 12. ---- NATIVE DROP-DOWN (product sort) ----
    sort_dropdown = driver.find_element(By.CLASS_NAME, "product_sort_container")
    Select(sort_dropdown).select_by_visible_text("Price (low to high)")
    time.sleep(1)
    home_page.screenshot("10_price_sorted")

    # 13. ---- SCROLL BACK TO TOP (JS) ----
    driver.execute_script("window.scrollTo(0, 0);")
    home_page.screenshot("11_scrolled_to_top")

    print("JS executor + scroll + drop-down completed with screenshots")