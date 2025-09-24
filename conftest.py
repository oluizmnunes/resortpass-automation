import json, pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.home_page import HomePage

@pytest.fixture(scope="session")
def config():
    with open("config/config.json") as f:
        return json.load(f)

@pytest.fixture(scope="function")
def driver(config):
    options = Options()

    if config.get("headless", True):
        options.add_argument("--headless=new")
    
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(config["implicit_wait"])
    driver.get(config["base_url"])

    # avoid promo pop-up
    HomePage(driver).dismiss_promo_if_present(timeout=5)
    
    yield driver
    driver.quit()