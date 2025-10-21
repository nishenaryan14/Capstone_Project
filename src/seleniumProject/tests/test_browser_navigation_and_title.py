import pytest
from src.seleniumProject.pages.login_page import LoginPage


def test_can_open_sauce_demo_and_see_login(driver, base_url):
    LoginPage(driver).open(base_url)
    assert driver.find_element("id", "login-button")

@pytest.mark.selenium_topics
def test_browser_launch_and_title(driver, base_url):
    driver.get(base_url)
    assert "Swag Labs" in driver.title


@pytest.mark.selenium_topics
def test_driver_methods_and_navigation(driver, base_url):
    driver.get(base_url)
    start_url = driver.current_url

    driver.maximize_window()
    driver.minimize_window()
    driver.set_window_size(1280, 800)
    driver.back()      # safe even if first page
    driver.forward()
    driver.refresh()

    assert start_url in driver.current_url