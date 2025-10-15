from appium.webdriver.common.appiumby import AppiumBy
from pages.basepage import BasePage
from utils.logger import log

# In D6/home_page.py
class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        # self.POPUP_TITLE_ID = (AppiumBy.ID, "android:id/alertTitle")
        # self.POPUP_MESSAGE_ID = (AppiumBy.ID, "android:id/message")
        # self.OK_BUTTON_ID = (AppiumBy.ID, "android:id/button1")
        # self.CANCEL_BUTTON_ID = (AppiumBy.ID, "android:id/button2")
        self.click_show_popup_id = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Show Popup")')
        self.popup_title_id = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Confirm")')
        self.click_accept_id = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Accept")')
        self.notification_button_id = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Notification")')
        self.allow_button_id = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Allow")')

    def click_show_popup(self):
        # log.info("Attempting to click on 'Show Popup'")
        self.click_element(*self.click_show_popup_id)
        # self.click_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Show Popup")')

    def get_popup_title(self):
        return self.get_element_text(*self.popup_title_id)
        # return self.get_element_text(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Confirm")')
    
    def click_accept(self):
        self.click_element(*self.click_accept_id)
        # self.click_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Accept")')

    def click_notification_button(self):
        self.click_element(*self.notification_button_id)
        # self.click_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Notification")')

    def click_allow_button(self):
        self.click_element(*self.allow_button_id)
        # self.click_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Allow")')





    # def get_popup_message(self):
    #     return self.get_element_text(*self.Locators.POPUP_MESSAGE)

    # def accept_popup(self):
    #     self.click_element(*self.Locators.OK_BUTTON)

    # def dismiss_popup(self):
    #     self.click_element(*self.Locators.CANCEL_BUTTON)