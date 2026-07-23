def test_logout(driver):
    user = TEST_DATA["valid_user"]
    driver.get(f"{BASE_URL}/login")
    wait = WebDriverWait(driver, 10)

    # Логин
    email_field = wait.until(EC.element_to_be_clickable(EMAIL_FIELD))
    email_field.send_keys(user["email"])

    password_field = wait.until(EC.element_to_be_clickable(PASSWORD_FIELD))
    password_field.send_keys(user["password"])

    login_button = wait.until(EC.element_to_be_clickable(LOGIN_BUTTON))
    login_button.click()

    wait.until(lambda d: "profile" in d.current_url.lower())

    # Выходим
    logout_button = wait.until(EC.element_to_be_clickable(LOGOUT_BUTTON))
    logout_button.click()

    # Проверяем, что вернулись на главную
    wait.until(lambda d: BASE_URL in d.current_url)
    assert BASE_URL in driver.current_url
    assert LOGIN_FORM in driver.page_source  # Должна быть видна форма логина
