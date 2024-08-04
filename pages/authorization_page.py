from selene import browser, be, have
import allure


class AuthorizationUserPage:
    def open(self):
        with allure.step('Open the main page https://www.tutu.ru'):
            browser.open('/')

    def open_authorization_page(self):
        with allure.step('Open authorization form'):
            browser.element('[data-ti="login_link"]').click()

    def fill_email(self, email):
        with allure.step('Fill Email'):
            browser.element('[name="email"]').should(be.blank).type(email)

    def fill_password(self, password):
        with allure.step('Fill Password'):
            browser.element('[name="password"]').should(be.blank).type(password)

    def submit_authorization(self):
        with allure.step('Submit authorization'):
            browser.element('[data-ti="submit-trigger"]').click()

    def should_have_logout_form(self):
        with allure.step('Check the successful authorization'):
            browser.element('[data-ti="logout_link"]').click()

    def should_have_text(self, text):
        with allure.step('Check that the authorization failed'):
            browser.element('[data-ti-error="authApi"]').should(have.text(text))


authorization_page = AuthorizationUserPage()
