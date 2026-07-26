# test_registration.py
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import BASE_URL
from fixtures import TEST_DATA
from locators import (NAME_FIELD, EMAIL_FIELD_REG, PASSWORD_FIELD_REG, REGISTER_BUTTON, SUCCESS_MESSAGE, ERROR_MESSAGE)

class TestRegistration:
    def test_valid_registration(self, driver):
        """Тест: успешная регистрация с корректными данными."""
        user = TEST_DATA["valid_user"]
        driver.get(f"{BASE_URL}/register")
        wait = WebDriverWait(driver, 10)

        # Заполняем форму регистрации
        name_field = wait.until(EC.element_to_be_clickable(NAME_FIELD))
        name_field.send_keys(user["name"])

        email_field = wait.until(EC.element_to_be_clickable(EMAIL_FIELD_REG))
        email_field.send_keys(user["email"])

        password_field = wait.until(EC.element_to_be_clickable(PASSWORD_FIELD_REG))
        password_field.send_keys(user["password"])

        register_button = wait.until(EC.element_to_be_clickable(REGISTER_BUTTON))
        register_button.click()

        # Ждём сообщения об успехе
        success_message = wait.until(
            EC.visibility_of_element_located(SUCCESS_MESSAGE)
        )

        assert "Регистрация успешна" in success_message.text, "Ожидалось сообщение об успешной регистрации"

    @pytest.mark.parametrize("user_key", ["invalid_password_short", "invalid_password_no_letters"])
    def test_invalid_password_registration(self, driver, user_key):
        """Тест: регистрация с некорректным паролем должна выдать ошибку."""
        user = TEST_DATA[user_key]
        driver.get(f"{BASE_URL}/register")
        wait = WebDriverWait(driver, 10)

        # Заполняем форму
        name_field = wait.until(EC.element_to_be_clickable(NAME_FIELD))
        name_field.send_keys(user["name"])

        email_field = wait.until(EC.element_to_be_clickable(EMAIL_FIELD_REG))
        email_field.send_keys(user["email"])

        password_field = wait.until(EC.element_to_be_clickable(PASSWORD_FIELD_REG))
        password_field.send_keys(user["password"])

        register_button = wait.until(EC.element_to_be_clickable(REGISTER_BUTTON))
        register_button.click()

        error_element = wait.until(
            EC.visibility_of_element_located(ERROR_MESSAGE)
        )

        assert "пароль" in error_element.text.lower(), f"Ожидалось сообщение об ошибке пароля для {user_key}"
