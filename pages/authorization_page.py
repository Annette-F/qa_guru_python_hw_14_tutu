from selene import browser, be, have


class AuthorizationUserPage:
    def open(self):
        browser.open('/')

    def open_authorization_page(self):
        browser.element('[data-ti="login_link"]').click()

    def fill_email(self, email):
        browser.element('[name="email"]').should(be.blank).type(email)

    def fill_password(self, password):
        browser.element('[name="password"]').should(be.blank).type(password)

    def submit_authorization(self):
        browser.element('[data-ti="submit-trigger"]').click()

    def should_have_logout_form(self):
        browser.element('[data-ti="logout_link"]').click()

    def should_have_text(self, text):
        browser.element('[data-ti-error="authApi"]').should(have.text(text))


authorization_page = AuthorizationUserPage()
