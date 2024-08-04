from selene import browser, be, have

class ChangeLanguagePage:
    def select_eng_language(self):
        browser.element('[class="flag eng"]').click()

    def select_rus_language(self):
        browser.element('[class="flag rus"]').click()