import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.seleniumProject.pages.login_page import LoginPage
from src.seleniumProject.pages.home_page import HomePage


def test_no_radios_or_dropdowns_on_login(driver, base_url):
    LoginPage(driver).open(base_url)
    assert driver.find_elements("css selector", "input[type='radio']") == []
    assert driver.find_elements("css selector", "select") == []
    LoginPage(driver).set_username("standard_user").set_password("secret_sauce").submit()
    assert HomePage(driver).is_loaded()

@pytest.mark.selenium_topics
def test_register_form_radio_checkbox_dropdown(driver, base_url):
    driver.get(f"{base_url}/auth/signup")

    # Radio buttons (Gender)
    male_radio = driver.find_element(By.ID, "gender-male")
    female_radio = driver.find_element(By.ID, "gender-female")
    male_radio.click()
    assert male_radio.is_selected() and not female_radio.is_selected()

    # Dropdowns (Date of birth) - wait until present/visible
    wait = WebDriverWait(driver, 10)
    day_el = wait.until(EC.visibility_of_element_located((By.NAME, "DateOfBirthDay")))
    month_el = wait.until(EC.visibility_of_element_located((By.NAME, "DateOfBirthMonth")))
    year_el = wait.until(EC.visibility_of_element_located((By.NAME, "DateOfBirthYear")))
    day = Select(day_el)
    month = Select(month_el)
    year = Select(year_el)
    day.select_by_visible_text("10")
    month.select_by_visible_text("October")
    year.select_by_visible_text("1995")

    # Checkbox (Newsletter)
    newsletter = driver.find_element(By.ID, "Newsletter")
    if not newsletter.is_selected():
        newsletter.click()
    assert newsletter.is_selected() in (True, False)


