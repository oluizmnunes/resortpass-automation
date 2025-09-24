from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
from datetime import datetime

class HomePage(BasePage):
    #region Selectors
    INPUT_WHERE_TO = (By.XPATH, "//p[contains(text(), 'Where to?')]")
    BTN_SEARCH = (By.XPATH, "//button[contains(., 'Search')]")
    #endregion

    #region Interaction methods
    def search_city(self, city):
        self.click(*self.INPUT_WHERE_TO)
        
        # avoid stale elements: find the focused input and type the city with JS
        input_where_to_field = WebDriverWait(self.driver, 10).until(
            lambda d: d.switch_to.active_element 
            
            if d.switch_to.active_element.tag_name.lower() in ("input", "textarea") 
            else False
        )
        
        input_where_to_field.clear()
        input_where_to_field.send_keys(city)
        
        # wait for and click the first suggestion (using JS)
        # TODO: make it more robust. E.g.: there's "Newark" in many US states
        first_result = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"//span[contains(., '{city}')]"))
        )
        self.driver.execute_script("arguments[0].click();", first_result)
    #endregion