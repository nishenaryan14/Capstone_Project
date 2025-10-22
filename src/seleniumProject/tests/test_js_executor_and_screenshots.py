import os
import pytest
import os
from datetime import datetime
from src.seleniumProject.pages.login_page import LoginPage
from src.seleniumProject.pages.home_page import HomePage


def test_take_inventory_screenshot(driver, base_url, tmp_path):
    LoginPage(driver).open(base_url)\
        .set_username("standard_user")\
        .set_password("secret_sauce")\
        .submit()
    assert HomePage(driver).is_loaded()
    # Scroll to bottom using JS executor
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # Save screenshot
    file_path = os.path.join(str(tmp_path), f"inventory_{datetime.now().strftime('%H%M%S')}.png")
    driver.save_screenshot(file_path)
    assert os.path.exists(file_path)

@pytest.mark.selenium_topics
def test_js_executor_scroll_and_screenshot(tmp_path, driver, base_url):
    driver.get(base_url)

    # Execute JS: return title and scroll
    title = driver.execute_script("return document.title;")
    assert "Swag Labs" in title
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    driver.execute_script("window.scrollTo(0, 0);")

    # Screenshot
    out_file = os.path.join(str(tmp_path), "homepage.png")
    assert driver.save_screenshot(out_file)
    assert os.path.exists(out_file)


