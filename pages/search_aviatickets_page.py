from selene import browser


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
