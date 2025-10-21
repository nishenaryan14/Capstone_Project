import os
import pytest

from .pages.login_page import LoginPage


@pytest.mark.e2e
def test_invalid_login_shows_error(driver, base_url):
    page = LoginPage(driver).open(base_url)
    page.set_email("invalid@example.com").set_password("wrongpass").submit()
    summary = page.get_summary_error_text()
    assert "Login was unsuccessful." in summary


@pytest.mark.e2e
def test_empty_fields_show_validation(driver, base_url):
    page = LoginPage(driver).open(base_url)
    page.submit()
    errors = page.get_field_error_texts()
    assert any("Email is required" in e or "Enter your email" in e for e in errors)


@pytest.mark.e2e
def test_forgot_password_navigation(driver, base_url):
    page = LoginPage(driver).open(base_url)
    page.click_forgot_password()
    assert "/passwordrecovery" in driver.current_url


