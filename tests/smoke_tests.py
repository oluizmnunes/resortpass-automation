from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_search_valid_city(driver):
    city = "New York"
    home_page = HomePage(driver)
    
    home_page.search_city(city)
    home_page.click(*home_page.BTN_SEARCH)

    search_results_page = SearchResultsPage(driver)
    result_count = search_results_page.print_results_for_city(city)
    
    assert result_count > 0, ' *** Error: No results found for {city}.'