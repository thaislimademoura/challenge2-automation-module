from appium.webdriver.common.appiumby import AppiumBy
from pages.basepage import BasePage

# In D6/home_page.py
class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.POPUP_TITLE_ID = (AppiumBy.ID, "android:id/alertTitle")
        self.POPUP_MESSAGE_ID = (AppiumBy.ID, "android:id/message")
        self.OK_BUTTON_ID = (AppiumBy.ID, "android:id/button1")
        self.CANCEL_BUTTON_ID = (AppiumBy.ID, "android:id/button2")

    def click_show_popup(self):
        self.click_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Show Popup")')

    # def get_popup_title(self):
    #     return self.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Confirm")').text

    def get_popup_title(self):
        return self.get_element_text(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Confirm")')



    # def get_popup_message(self):
    #     return self.get_element_text(*self.Locators.POPUP_MESSAGE)

    # def accept_popup(self):
    #     self.click_element(*self.Locators.OK_BUTTON)

    # def dismiss_popup(self):
    #     self.click_element(*self.Locators.CANCEL_BUTTON)