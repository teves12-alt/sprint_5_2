# conftest.py
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from config import BASE_URL

@pytest.fixture(scope="function")
def driver():
    """Фикстура для инициализации и очистки WebDriver."""
    options = Options()
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()

