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


class UpdatePersonalData:
    def open_profile(self):
        browser.element('[data-ti="user_name_link"]').click()
        browser.element('#editDataLink').click()

    def type_first_name(self, firstname):
        browser.element('#editDForm_first_name').clear().type(firstname)

    def type_middle_name(self, middlename):
        browser.element('#editDForm_middle_name').clear().type(middlename)

    def type_last_name(self, lastname):
        browser.element('#editDForm_last_name').clear().type(lastname)

    def type_phone(self, phone):
        browser.element('#editDForm_phone').clear().type(phone)

    def type_birthday(self, birthday):
        browser.element('#editDForm_birthday').clear().type(birthday).click()

    def confirm_agreement_form(self):
        browser.element('#editDForm_agree').click()

    def submit_edit_form(self):
        browser.element('#editDForm_submit').click()

    def open_main_page(self):
        browser.element('.jUzldXN___logoLink').click()


class ChangeLanguagePage:
    def select_eng_language(self):
        browser.element('[class="flag eng"]').click()

    def select_rus_language(self):
        browser.element('[class="flag rus"]').click()


class SearchAviatickets:
    def type_city_from(self, cityfrom):
        browser.element('[name="city_from"]').type(cityfrom).press_enter()

    def type_city_to(self, cityto):
        browser.element('[name="city_to"]').type(cityto).press_enter()

    def type_date_from(self, datefrom):
        browser.element('[name="date_from"]').type(datefrom).press_enter()

    def type_date_to(self, dateto):
        browser.element('[name="date_back"]').type(dateto)

    def count_adult_passengers(self):
        browser.element('[class="counter_adult_wrp"]').element('[class="increase"]').click()

    def select_class(self):
        browser.element('[class="j-dropdown"]').click()
        browser.element('[data-value="C"]').click()

    def submit_selection(self):
        browser.element('[class="button_wrp j-buttons_block"]').click()
