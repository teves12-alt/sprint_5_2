# test_login.py
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import BASE_URL
from locators import (LOGIN_BUTTON_MAIN, LOGIN_BUTTON_PROFILE, LOGIN_BUTTON_REG, LOGIN_BUTTON_RESET)

class TestLogin:
    def test_login_from_main_page(self, driver):
        """Тест: вход по кнопке «Войти в аккаунт» на главной."""
        driver.get(BASE_URL)
        wait = WebDriverWait(driver, 10)

        login_button = wait.until(EC.element_to_be_clickable(LOGIN_BUTTON_MAIN))
        login_button.click()

        # Проверяем переход на страницу входа
        assert "login" in driver.current_url.lower(), "Не произошёл переход на страницу входа"

    def test_login_from_profile_link(self, driver):
        """Тест: вход через кнопку «Личный кабинет»."""
        driver.get(f"{BASE_URL}/profile")
        wait = WebDriverWait(driver, 10)

        login_button = wait.until(EC.element_to_be_clickable(LOGIN_BUTTON_PROFILE))
        login_button.click()

        assert "login" in driver.current_url.lower(), "Не произошёл переход к форме входа"

    def test_login_from_registration_form(self, driver):
        """Тест: вход через кнопку в форме регистрации."""
        driver.get(f"{BASE_URL}/register")
        wait = WebDriverWait(driver, 10)

        login_button = wait.until(EC.element_to_be_clickable(LOGIN_BUTTON_REG))
        login_button.click()

        assert "login" in driver.current_url.lower(), "Не произошёл переход к форме входа из регистрации"

    def test_login_from_reset_form(self, driver):
        """Тест: вход через кнопку в форме восстановления пароля."""
        driver.get(f"{BASE_URL}/reset-password")
        wait = WebDriverWait(driver, 10)

        login_button = wait.until(EC.element_to_be_clickable(LOGIN_BUTTON_RESET))
        login_button.click()

        assert "login" in driver.current_url.lower(), "Не произошёл переход к форме входа из сброса пароля"
