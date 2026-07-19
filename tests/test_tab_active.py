import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import BASE_URL
from locators import OTHER_TAB, TARGET_TAB, ACTIVE_TAB_INDICATOR

@pytest.fixture
def driver():
    from selenium import webdriver
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_tab_is_active(driver):
    driver.get(BASE_URL)
    wait = WebDriverWait(driver, 10)

    other_tab = wait.until(EC.element_to_be_clickable(OTHER_TAB))
    other_tab.click()

    target_tab = wait.until(EC.element_to_be_clickable(TARGET_TAB))
    target_tab.click()

    active_tab = wait.until(
        EC.presence_of_element_located(ACTIVE_TAB_INDICATOR)
    )
    assert active_tab.is_displayed()
