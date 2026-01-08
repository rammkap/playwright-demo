from playwright.sync_api import sync_playwright, expect

def test_empty_courses_list():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

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

        context.storage_state(path="browser-state.json")

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(storage_state="browser-state.json")
        page = context.new_page()

        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

        title_courses = page.get_by_test_id('courses-list-toolbar-title-text')
        title_no_results = page.get_by_test_id('courses-list-empty-view-title-text')
        icon_empty = page.get_by_test_id('courses-list-empty-view-icon')
        title_no_results_full = page.get_by_test_id('courses-list-empty-view-description-text')

        expect(title_courses).to_be_visible()
        print(f'"title_courses" is visible')
        expect(title_courses).to_have_text('Courses')

        expect(title_no_results).to_be_visible()
        print(f'"title_no_results" is visible')
        expect(title_no_results).to_have_text('There is no results')

        expect(icon_empty).to_be_visible()
        print(f'"icon_empty" is visible')

        expect(title_no_results_full).to_be_visible()
        print(f'"title_no_results_full" is visible')
        expect(title_no_results_full).to_have_text('Results from the load test pipeline will be displayed here')