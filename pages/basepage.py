from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from appium.webdriver.webdriver import WebDriver  # Appium WebDriver

class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find_element(self, by, locator):
        return self.wait.until(EC.presence_of_element_located((by, locator)))

    def click_element(self, by, locator):
        self.find_element(by, locator).click()

    def send_keys_to_element(self, by, locator, text):
        self.find_element(by, locator).send_keys(text)

    def get_element_text(self, by, locator):
        return self.find_element(by, locator).text

    def is_element_displayed(self, by, locator):
        try:
            return self.find_element(by, locator).is_displayed()
        except:
            return False
        
    def is_element_enabled(self, by, locator):
        try:
            return self.find_element(by, locator).is_enabled()
        except:
            return False
        
    def clear_field(self, by, locator):
        self.find_element(by, locator).clear()

    def wait_for_visibility_of_element(self, by, locator, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.visibility_of_element_located((by, locator)))
        



        
    def open_notifications(self):
        try:
            self.driver.open_notifications()
        except AttributeError:
            raise Exception("open_notifications() não está disponível no driver atual.")

    def is_notification_displayed(self, expected_title):
        try:
            locator = (
                AppiumBy.XPATH,
                f"//*[@resource-id='android:id/title' and @text='{expected_title}']"
            )
            self.wait_for_visibility_of_element(*locator)
            return True
        except TimeoutException:
            return False
        finally:
            self.driver.back()

    def get_notification_text(self, expected_title):
        try:
            title_element = self.wait_for_visibility_of_element(
                AppiumBy.XPATH,
                f"//*[@resource-id='android:id/title' and @text='{expected_title}']"
            )
            notification_text = title_element.find_element(
                AppiumBy.XPATH,
                "following-sibling::*[@resource-id='android:id/text']"
            ).text
            return notification_text
        except Exception:
            return None
        finally:
            self.driver.back()
