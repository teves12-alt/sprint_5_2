# locators.py
from selenium.webdriver.common.by import By

# Регистрация
NAME_FIELD = (By.NAME, "name")
EMAIL_FIELD = (By.NAME, "email")
PASSWORD_FIELD = (By.CSS_SELECTOR, "input[type='password']")
REGISTER_BUTTON = (By.XPATH, "//button[contains(text(), 'Зарегистрироваться')]")
ERROR_MESSAGE = (By.CLASS_NAME, "error-message")

# Вкладки
OTHER_TAB = (By.XPATH, "//a[contains(text(), 'Профиль')]")
TARGET_TAB = (By.XPATH, "//a[contains(text(), 'Главная')]")
ACTIVE_TAB_INDICATOR = (By.XPATH, "//a[contains(text(), 'Главная') and contains(@class, 'active')]")
