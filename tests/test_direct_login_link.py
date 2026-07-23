def test_direct_login_link(driver):
    user = TEST_DATA["valid_user"]
    driver.get(f"{BASE_URL}/login")  # Прямой переход
    wait = WebDriverWait(driver, 10)

    email_field = wait.until(EC.element_to_be_clickable(EMAIL_FIELD))
    email_field.send_keys(user["email"])

    password_field = wait.until(EC.element_to_be_clickable(PASSWORD_FIELD))
    password_field.send_keys(user["password"])

    login_button = wait.until(EC.element_to_be_clickable(LOGIN_BUTTON))
    login_button.click()

    wait.until(lambda d: "profile" in d.current_url.lower())
    assert "profile" in driver.current_url.lower()
