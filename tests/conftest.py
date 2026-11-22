import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="function")
def driver():
    chrome_options = Options()
    
    # Run in visual (headed) mode if HEADLESS=false or HEADED=true
    is_headless = os.environ.get("HEADLESS", "true").lower() not in ["false", "0", "no"]
    if os.environ.get("HEADED", "false").lower() in ["true", "1", "yes"]:
        is_headless = False

    if is_headless:
        chrome_options.add_argument("--headless=new")
    else:
        chrome_options.add_argument("--start-maximized")

    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0 Safari/537.36")

    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()
