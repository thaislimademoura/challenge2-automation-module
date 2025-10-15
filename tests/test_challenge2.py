import pytest
from pages.homepage import HomePage

# Import other page objects as needed

def test_challenge_2(driver):
    # Initialize page objects with the driver provided by the fixture
    homepage = HomePage(driver)

    # Perform actions using page object methods
    homepage.click_show_popup()
    assert homepage.get_popup_title() == "Confirm"

    homepage.click_accept()

    homepage.click_notification_button()
    homepage.click_allow_button()
    # homepage.get_popup_message()
    # homepage.accept_popup()
    # homepage.dismiss_popup()


