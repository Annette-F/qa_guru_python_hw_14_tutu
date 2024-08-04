from selene import browser

class EditPersonalData:
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
