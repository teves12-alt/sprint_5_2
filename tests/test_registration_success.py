import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import BASE_URL
from fixtures import TEST_DATA
from locators import NAME_FIELD, EMAIL_FIELD, PASSWORD_FIELD, REGISTER_BUTTON

@pytest.fixture
def driver():
    from selenium import webdriver
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_successful_registration(driver):
    user = TEST_DATA["valid_user"]
    driver.get(f"{BASE_URL}/register")
    wait = WebDriverWait(driver, 10)

    wait.until(EC.presence_of_element_located(NAME_FIELD))
    driver.find_element(*NAME_FIELD).send_keys(user["name"])
    driver.find_element(*EMAIL_FIELD).send_keys(user["email"])
    driver.find_element(*PASSWORD_FIELD).send_keys(user["password"])
    driver.find_element(*REGISTER_BUTTON).click()

    wait.until(lambda d: BASE_URL in d.current_url)
    assert BASE_URL in driver.current_url
