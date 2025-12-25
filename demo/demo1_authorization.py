from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

    # field_email = page.locator('//div[@data-testid="login-form-email-input"]//div//input')
    field_email = page.get_by_test_id("login-form-email-input").locator("//div//input")
    field_email.fill("user.name@gmail.com")

    # field_password = page.locator('//div[@data-testid="login-form-password-input"]//div//input')
    field_password = page.get_by_test_id("login-form-password-input").locator("//div//input")
    field_password.fill("password")

    # button_login = page.locator('//button[@data-testid="login-page-login-button"]')
    button_login = page.get_by_test_id("login-page-login-button")
    button_login.click()

    alert_wrong_email_password = page.locator('//div[@data-testid="login-page-wrong-email-or-password-alert"]')
    expect(alert_wrong_email_password).to_be_visible()
    expect(alert_wrong_email_password).to_have_text("Wrong email or password")

    page.wait_for_timeout(5000)