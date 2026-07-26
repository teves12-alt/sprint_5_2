# fixtures.py
TEST_DATA = {
    "valid_user": {
        "name": "Иван Иванов",
        "email": "ivan@ya.ru",
        "password": "Secure123"
    },
    "invalid_password_short": {
        "name": "Тестовый Пользователь",
        "email": "test@ya.ru",
        "password": "short"  # меньше 6 символов
    },
    "invalid_password_no_letters": {
        "name": "Тестовый Пользователь",
        "email": "test@ya.ru",
        "password": "123456"  # только цифры
    }
}
