from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    # Locators

    field_email = page.get_by_test_id("registration-form-email-input").locator("input")
    field_username = page.get_by_test_id("registration-form-username-input").locator("input")
    field_password = page.get_by_test_id("registration-form-password-input").locator("input")
    button_registration = page.get_by_test_id("registration-page-registration-button")
    title_dashboard = page.get_by_test_id("dashboard-toolbar-title-text")

    # Actions

    field_email.fill("user.name@gmail.com")
    field_email.fill("username")
    field_password.fill("password")
    button_registration.click()
    expect(title_dashboard).to_be_visible()
    expect(title_dashboard).to_have_text("Dashboard")

