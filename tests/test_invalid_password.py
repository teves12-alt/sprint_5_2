import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import BASE_URL
from fixtures import TEST_DATA
from locators import NAME_FIELD, EMAIL_FIELD, PASSWORD_FIELD, REGISTER_BUTTON, ERROR_MESSAGE

@pytest.fixture
def driver():
    from selenium import webdriver
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_invalid_password_registration(driver):
    user = TEST_DATA["invalid_password"]
    driver.get(f"{BASE_URL}/register")
    wait = WebDriverWait(driver, 10)

    driver.find_element(*NAME_FIELD).send_keys(user["name"])
    driver.find_element(*EMAIL_FIELD).send_keys(user["email"])
    driver.find_element(*PASSWORD_FIELD).send_keys(user["password"])
    driver.find_element(*REGISTER_BUTTON).click()

    error_element = wait.until(
        EC.visibility_of_element_located(ERROR_MESSAGE)
    )
    error_message = error_element.text
    assert "Пароль слишком короткий" in error_message or "password too short" in error_message.lower()
