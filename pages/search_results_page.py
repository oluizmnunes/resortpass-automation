from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage

class SearchResultsPage(BasePage):
    RESULTS_CONTAINER = (By.CSS_SELECTOR, "[data-testid='search-results'], .search-results, .results-container")
    RESULT_ITEM = (By.CSS_SELECTOR, "[data-testid='result-item'], h2.truncate")
    
    def get_results(self):
        try:
            # Try to find results container first
            results_container = self.driver.find_elements(*self.RESULTS_CONTAINER)
            if results_container:
                return results_container[0].find_elements(*self.RESULT_ITEM)
            else:
                # Fallback: look for individual result items directly
                return self.driver.find_elements(*self.RESULT_ITEM)
        except Exception:
            # If no specific selectors work, return empty list
            return []
    
    def get_result_count(self):
        # Wait for results to load
        try:
            WebDriverWait(self.driver, 10).until(
                lambda d: len(self.get_results()) > 0
            )
        except:
            pass  # Continue even if no results found
        return len(self.get_results())
    
    def get_result_texts(self):
        results = self.get_results()
        return results

    def print_results_for_city(self, city):
        result_count = self.get_result_count()
        print(f' *** Found {result_count} search results')
        
        results = self.get_results()
        print(f' *** First 30 Hotel Day Passes in and near "{city}":')

        for i, result in enumerate(results, 1):
            print(f' *** Hotel {i}: {result.text[:30]}')
        
        return result_count
