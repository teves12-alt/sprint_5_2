def test_login_via_profile_link(driver):
    user = TEST_DATA["valid_user"]
    driver.get(BASE_URL)  # Главная страница
    wait = WebDriverWait(driver, 10)

    profile_link = wait.until(EC.element_to_be_clickable(PROFILE_LINK))
    profile_link.click()

    # Здесь должна быть форма логина — заполняем её аналогично тесту 1
    email_field = wait.until(EC.element_to_be_clickable(EMAIL_FIELD))
    email_field.send_keys(user["email"])

    password_field = wait.until(EC.element_to_be_clickable(PASSWORD_FIELD))
    password_field.send_keys(user["password"])

    login_button = wait.until(EC.element_to_be_clickable(LOGIN_BUTTON))
    login_button.click()

    wait.until(lambda d: "profile" in d.current_url.lower())
    assert "profile" in driver.current_url.lower()
