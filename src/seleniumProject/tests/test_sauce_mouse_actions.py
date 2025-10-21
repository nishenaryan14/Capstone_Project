import pytest
from src.seleniumProject.pages.login_page import LoginPage
from src.seleniumProject.pages.sauce_hover_name import SauceHoverNamePage


@pytest.mark.selenium_topics
def test_hover_item_name_colour_changes(driver):
    """Hover first item name link → colour is different after hover."""
    login_page = LoginPage(driver)
    login_page.open("https://www.saucedemo.com")
    login_page.login_with("standard_user", "secret_sauce")

    hover = SauceHoverNamePage(driver)
    before = hover.name_link_colour()
    hover.hover_item_name()
    assert hover.colour_changed_after_hover(before), f"Colour did not change: before={before}, after={hover.name_link_colour()}"
    hover.screenshot("after_hover")