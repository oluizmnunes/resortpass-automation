from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.common.keys import Keys
from time import sleep

class BasePage:
    BTN_TAKE_ME_TO_THE_SITE = (By.XPATH, "//button[contains(text(), 'take me to the site')]")
    
    def __init__(self, driver):
        self.driver = driver

    def click(self, by, locator):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((by, locator))
            )
            element.click()
        except Exception:
            # due to dynamic DOM, use JS to click if still blocked
            element = self.driver.find_element(by, locator)
            self.driver.execute_script("arguments[0].click();", element)

    def fill_with(self, by, locator, text):
        field = self.driver.find_element(by, locator)
        field.clear()
        field.send_keys(text)

    # close email subscribing pop-up
    def dismiss_promo_if_present(self, timeout=5):
        try:
            wait = WebDriverWait(self.driver, timeout)
            
            button = wait.until(
                EC.element_to_be_clickable(self.BTN_TAKE_ME_TO_THE_SITE)
            )
            button.click()
            return
        except (TimeoutException, WebDriverException):
            # press 'ESC' as last resource
            try:
                self.driver.switch_to.active_element.send_keys(Keys.ESCAPE)
                return
            except Exception:
                print(' *** Error: Couldn\'t close promo frame.')
                pass