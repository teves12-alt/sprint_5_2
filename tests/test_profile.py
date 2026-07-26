# test_profile.py
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import BASE_URL
from locators import (PROFILE_LINK, CONSTRUCTOR_BUTTON, LOGO, LOGOUT_BUTTON)

class TestProfileNavigation:
    def test_navigate_to_profile(self, driver):
        """Тест: переход по клику на «Личный кабинет»."""
        driver.get(BASE_URL)
        wait = WebDriverWait(driver, 10)

        profile_link = wait.until(EC.element_to_be_clickable(PROFILE_LINK))
        profile_link.click()

        # Проверяем переход в личный кабинет
        assert "/profile" in driver.current_url, "Не перешёл в личный кабинет"

    def test_navigate_to_constructor_from_profile(self, driver):
        """Тест: переход из личного кабинета в конструктор по кнопке «Конструктор»."""
        driver.get(f"{BASE_URL}/profile")
        wait = WebDriverWait(driver, 10)

        constructor_button = wait.until(EC.element_to_be_clickable(CONSTRUCTOR_BUTTON))
        constructor_button.click()

        assert "/constructor" in driver.current_url, "Не перешёл в конструктор"

    def test_navigate_to_constructor_via_logo(self, driver):
        """Тест: переход в конструктор через клик по логотипу Stellar Burgers."""
        driver.get(f"{BASE_URL}/profile")
        wait = WebDriverWait(driver, 10)

        logo = wait.until(EC.element_to_be_clickable(LOGO))
        logo.click()

        # Ждём загрузки главной страницы с конструктором
        wait.until(lambda d: "/constructor" in d.current_url)
        assert "/constructor" in driver.current_url, "Клик по логотипу не перевёл в конструктор"

    def test_logout_from_profile(self, driver):
        """Тест: выход из аккаунта по кнопке «Выйти» в личном кабинете."""
        driver.get(f"{BASE_URL}/profile")
        wait = WebDriverWait(driver, 10)

        logout_button = wait.until(EC.element_to_be_clickable(LOGUT_BUTTON))
        logout_button.click()

        # Проверяем переход на главную страницу после выхода
        assert BASE_URL in driver.current_url and "/profile" not in driver.current_url
