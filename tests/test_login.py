def test_login_via_form(driver):
    user = TEST_DATA["valid_user"]
    driver.get(f"{BASE_URL}/login")
    wait = WebDriverWait(driver, 10)

    # Заполняем форму
    email_field = wait.until(EC.element_to_be_clickable(EMAIL_FIELD))
    email_field.send_keys(user["email"])

    password_field = wait.until(EC.element_to_be_clickable(PASSWORD_FIELD))
    password_field.send_keys(user["password"])

    login_button = wait.until(EC.element_to_be_clickable(LOGIN_BUTTON))
    login_button.click()

    # Проверяем, что перешли в личный кабинет
    wait.until(lambda d: PROFILE_LINK in d.page_source)
    assert "profile" in driver.current_url.lower(), "Не перешли в ЛК после успешного входа"
