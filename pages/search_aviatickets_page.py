from selene import browser
import allure


class SearchAviatickets:
    def type_city_from(self, cityfrom):
        with allure.step('Select the city from'):
            browser.element('[name="city_from"]').type(cityfrom).press_enter()

    def type_city_to(self, cityto):
        with allure.step('Select the city to'):
            browser.element('[name="city_to"]').type(cityto).press_enter()

    def type_date_from(self, datefrom):
        with allure.step('Select the departure date'):
            browser.element('[name="date_from"]').type(datefrom).press_enter()

    def type_date_to(self, dateto):
        with allure.step('Select the date of the return ticket'):
            browser.element('[name="date_back"]').type(dateto)

    def count_adult_passengers(self):
        with allure.step('Select the number of adult passengers'):
            browser.element('[class="counter_adult_wrp"]').element('[class="increase"]').click()

    def select_class(self):
        with allure.step('Select class'):
            browser.element('[class="j-dropdown"]').click()
            browser.element('[data-value="C"]').click()

    def submit_selection(self):
        with allure.step('Submit selection'):
            browser.element('[class="button_wrp j-buttons_block"]').click()


search_aviaticket = SearchAviatickets()
