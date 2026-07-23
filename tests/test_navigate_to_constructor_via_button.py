def test_navigate_to_constructor_via_button(driver):
    user = TEST_DATA["valid_user"]
    driver.get(f"{BASE_URL}/login")
    wait = WebDriverWait(driver, 10)

    # Логин (аналогично предыдущим тестам)
    email_field = wait.until(EC.element_to_be_clickable(EMAIL_FIELD))
    email_field.send_keys(user["email"])

    password_field = wait.until(EC.element_to_be_clickable(PASSWORD_FIELD))
    password_field.send_keys(user["password"])

    login_button = wait.until(EC.element_to_be_clickable(LOGIN_BUTTON))
    login_button.click()

    wait.until(lambda d: "profile" in d.current_url.lower())

    # Переходим в конструктор через кнопку
    constructor_button = wait.until(EC.element_to_be_clickable(CONSTRUCTOR_BUTTON))
    constructor_button.click()

    wait.until(lambda d: "constructor" in d.current_url.lower())  # Ждём загрузки конструктора
    assert "constructor" in driver.current_url.lower()
