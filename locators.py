# locators.py
from pytest.webdriver.common.by import By

# Регистрация
NAME_FIELD = (By.NAME, "name")
EMAIL_FIELD_REG = (By.NAME, "email")
PASSWORD_FIELD_REG = (By.NAME, "password")
REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")
ERROR_MESSAGE = (By.CLASS_NAME, "input__error")
SUCCESS_MESSAGE = (By.CLASS_NAME, "success-message")

# Авторизация
LOGIN_BUTTON_MAIN = (By.XPATH, "//button[contains(text(), 'Войти в аккаунт')]")
LOGIN_BUTTON_PROFILE = (By.XPATH, "//button[contains(text(), 'Личный кабинет')]")
LOGIN_BUTTON_REG = (By.XPATH, "//form[@id='register-form']//button[text()='Войти']")
LOGIN_BUTTON_RESET = (By.XPATH, "//form[@id='reset-form']//button[text()='Войти']")

# Навигация
PROFILE_LINK = (By.XPATH, "//a[contains(text(), 'Личный кабинет')]")
CONSTRUCTOR_BUTTON = (By.XPATH, "//button[contains(text(), 'Конструктор')]")
LOGO = (By.CLASS_NAME, "logo")  # логотип Stellar Burgers

# Конструктор
BUNS_TAB = (By.XPATH, "//div[contains(text(), 'Булки')]")
SAUCES_TAB = (By.XPATH, "//div[contains(text(), 'Соусы')]")
INGREDIENTS_TAB = (By.XPATH, "//div[contains(text(), 'Начинки')]")

# Выход
LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(), 'Выйти')]")
