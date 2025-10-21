import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from src.seleniumProject.pages.login_page import LoginPage
from src.seleniumProject.pages.sauce_sidebar import SauceSidebarPage


@pytest.mark.selenium_topics
def test_sidebar_about_new_tab_then_logout(driver):
    """
    Sidebar → right-click About → open in new tab → click 'Try it for free'
    → close tab → back to parent → logout via still-open sidebar.
    """
    login_page = LoginPage(driver)
    login_page.open("https://www.saucedemo.com")
    login_page.login_with("standard_user", "secret_sauce")
    login_page.screenshot("01_inventory_page")

    time.sleep(3)

    # 1. Open sidebar
    sidebar = SauceSidebarPage(driver)
    sidebar.open_sidebar()
    login_page.screenshot("02_sidebar_opened")

    # 2. Right-click “About”
    sidebar.right_click_about()
    login_page.screenshot("03_context_menu_about")

    # 3. Simulate “Open in new tab” (Ctrl + Shift + Enter on the link)
    about_link = driver.find_element(By.ID, "about_sidebar_link")
    about_link.send_keys(Keys.CONTROL + Keys.SHIFT + Keys.RETURN)
    login_page.screenshot("04_new_tab_opened")

    # 4. Switch to the new tab
    original_tab = driver.current_window_handle
    WebDriverWait(driver, 5).until(lambda d: len(d.window_handles) == 2)
    new_tab = [h for h in driver.window_handles if h != original_tab][0]
    driver.switch_to.window(new_tab)
    login_page.screenshot("05_switched_to_about_tab")

    # 5. Verify we landed on SauceLabs external page
    assert "saucelabs.com" in driver.current_url
    login_page.screenshot("06_external_about_page")

    # 6. Click “Try it for free” (external sign-up page)
    try_it_btn = driver.find_element(By.XPATH, "/html/body/div[1]/header/div/div/div[2]/div[3]/a/button")
    try_it_btn.click()
    login_page.screenshot("07_try_it_free_clicked")

    # 7. Close the new tab and return to parent
    driver.close()
    driver.switch_to.window(original_tab)
    login_page.screenshot("08_back_to_inventory")

    # 8. Sidebar still open – click Logout
    assert sidebar.is_sidebar_open()
    sidebar.click_logout()
    login_page.screenshot("09_after_logout")

    # 9. Verify back on login page
    assert login_page.exists((By.ID, "user-name"))
    login_page.screenshot("10_final_login_page")

    print("Sidebar → new-tab About → close → logout completed.")