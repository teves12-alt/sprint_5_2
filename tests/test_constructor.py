# test_constructor.py
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import BASE_URL
from locators import (BUNS_TAB, SAUCES_TAB, INGREDIENTS_TAB)

class TestConstructorNavigation:
    def test_navigate_to_buns_tab(self, driver):
        """Тест: переход к разделу «Булки» в конструкторе."""
        driver.get(f"{BASE_URL}/constructor")
        wait = WebDriverWait(driver, 10)

        buns_button = wait.until(EC.element_to_be_clickable(BUNS_TAB))
        buns_button.click()

        # Проверяем активацию вкладки
        assert driver.find_element(*BUNS_TAB).is_displayed(), "Вкладка «Булки» не активирована"

    def test_navigate_to_sauces_tab(self, driver):
        """Тест: переход к разделу «Соусы» в конструкторе."""
        driver.get(f"{BASE_URL}/constructor")
        wait = WebDriverWait(driver, 10)

        sauces_button = wait.until(EC.element_to_be_clickable(SAUCES_TAB))
        sauces_button.click()

        assert driver.find_element(*SAUCES_TAB).is_displayed(), "Вкладка «Соусы» не активирована"

    def test_navigate_to_ingredients_tab(self, driver):
        """Тест: переход к разделу «Начинки» в конструкторе."""
        driver.get(f"{BASE_URL}/constructor")
        wait = WebDriverWait(driver, 10)

        ingredients_button = wait.until(EC.element_to_be_clickable(INGREDIENTS_TAB))
        ingredients_button.click()

        assert driver.find_element(*INGREDIENTS_TAB).is_displayed(), "Вкладка «Начинки» не активирована"
