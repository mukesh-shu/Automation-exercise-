import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="function")
def setup():
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--no-sandbox")                
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-extensions")
    options.add_argument("--remote-allow-origins=*")

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)

    yield driver   # test runs here

    driver.quit()
