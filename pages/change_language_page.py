from selene import browser
import allure


class ChangeLanguagePage:
    def select_eng_language(self):
        with allure.step('Change the page to English'):
            browser.element('[class="flag eng"]').click()

    def select_rus_language(self):
        with allure.step('Change the page to Russian'):
            browser.element('[class="flag rus"]').click()


change_language_page = ChangeLanguagePage()
