from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

    # Locators

    button_registration = page.get_by_test_id('registration-page-registration-button')
    field_email = page.get_by_test_id('registration-form-email-input').locator('input')
    field_username = page.get_by_test_id('registration-form-username-input').locator('input')
    field_password = page.get_by_test_id('registration-form-password-input').locator('input')

    # Actions

    expect(button_registration).to_be_disabled()
    print('Button is disabled')

    field_email.fill('user.name@gmail.com')
    field_username.fill('username')
    field_password.fill('password')

    expect(button_registration).to_be_enabled()
    print('Button is enabled')