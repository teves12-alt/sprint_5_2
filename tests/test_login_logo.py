def test_login_via_logo(driver):
    user = TEST_DATA["valid_user"]
    driver.get(BASE_URL)
    wait = WebDriverWait(driver, 10)

    logo = wait.until(EC.element_to_be_clickable(HEADER_LOGO))
    logo.click()

    # Проверяем, что попали на форму логина
    assert "login" in driver.current_url.lower()
