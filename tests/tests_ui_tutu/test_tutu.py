from selene import browser, have, be
from allure_commons.types import Severity
import allure


@allure.tag('Web')
@allure.severity(Severity.CRITICAL)
@allure.label('Owner', 'Annette-F')
@allure.feature('Authorization with valid login and password')
@allure.story('Authorization')
@allure.link('https://www.tutu.ru', name='Tutu')
def test_valid_authorization():
    # Open main page
    browser.open('/')

    # Open authorization form
    browser.element('[data-ti="login_link"]').click()

    # Fill mail field
    browser.element('[name="email"]').should(be.blank).type('marivtest@mail.ru')

    # Fill password field
    browser.element('[name="password"]').should(be.blank).type('qwerty123')

    # Submit authorization
    browser.element('[data-ti="submit-trigger"]').click()
    browser.element('[data-ti="user_name_link"]').should(have.text('marivtest@mail.ru'))


@allure.tag('Web')
@allure.severity(Severity.CRITICAL)
@allure.label('Owner', 'Annette-F')
@allure.feature('Authorization with wrong password')
@allure.story('Authorization')
@allure.link('https://www.tutu.ru', name='Tutu')
def test_authorization_with_wrong_password():
    # Open main page
    browser.open('/')

    # Open authorization form
    browser.element('[data-ti="login_link"]').click()

    # Fill mail field
    browser.element('[name="email"]').should(be.blank).type('marivtest@mail.ru')

    # Fill password field with wrong password
    browser.element('[name="password"]').should(be.blank).type('zxcv1234')

    # Submit authorization
    browser.element('[data-ti="submit-trigger"]').click()
    browser.element('[data-ti-error="authApi"]').should(have.text('Неверный адрес почты или пароль.'))


@allure.tag('Web')
@allure.severity(Severity.NORMAL)
@allure.label('Owner', 'Annette-F')
@allure.feature('Update profile')
@allure.story('Profile')
@allure.link('https://www.tutu.ru', name='Tutu')
def test_update_personal_data():
    # Open main page
    browser.open('/')

    # Open authorization form
    browser.element('[data-ti="login_link"]').click()

    # Fill mail field
    browser.element('[name="email"]').should(be.blank).type('marivtest@mail.ru')

    # Fill password field
    browser.element('[name="password"]').should(be.blank).type('qwerty123')

    # Submit authorization
    browser.element('[data-ti="submit-trigger"]').click()

    # Open profile
    browser.element('[data-ti="user_name_link"]').click()

    # Open the Edit Data section
    browser.element('#editDataLink').click()

    # Fill name field
    browser.element('#editDForm_first_name').clear().type('Maria')

    # Fill middle name field
    browser.element('#editDForm_middle_name').clear().type('Ivanovna')

    # Fill last name field
    browser.element('#editDForm_last_name').clear().type('Petrova')

    # Fill phone number
    browser.element('#editDForm_phone').clear().type('9007778899')

    # Fill birthday
    browser.element('#editDForm_birthday').clear().type('20.04.2000').click()

    # Check consent to the processing of personal data
    browser.element('#editDForm_agree').click()

    # Submit
    browser.element('#editDForm_submit').click()

    # Open main page
    browser.element('.jUzldXN___logoLink').click()


@allure.tag('Web')
@allure.severity(Severity.MINOR)
@allure.label('Owner', 'Annette-F')
@allure.feature('Page language changes')
@allure.story('Page language')
@allure.link('https://www.tutu.ru', name='Tutu')
def test_change_language_page():
    # Open main page
    browser.open('/')

    # Open authorization form
    browser.element('[data-ti="login_link"]').click()

    # Fill mail field
    browser.element('[name="email"]').should(be.blank).type('marivtest@mail.ru')

    # Fill password field
    browser.element('[name="password"]').should(be.blank).type('qwerty123')

    # Submit authorization
    browser.element('[data-ti="submit-trigger"]').click()

    # Change language
    browser.element('[class="flag eng"]').click()
    browser.element('[class="flag rus"]').click()


@allure.tag('Web')
@allure.severity(Severity.CRITICAL)
@allure.label('Owner', 'Annette-F')
@allure.feature('Search aviatickets')
@allure.story('Page aviatickets')
@allure.link('https://www.tutu.ru', name='Tutu')
def test_search_aviaticket():
    # Open main page
    browser.open('/')

    # Open authorization form
    browser.element('[data-ti="login_link"]').click()

    # Fill mail field
    browser.element('[name="email"]').should(be.blank).type('marivtest@mail.ru')

    # Fill password field
    browser.element('[name="password"]').should(be.blank).type('qwerty123')

    # Submit authorization
    browser.element('[data-ti="submit-trigger"]').click()

    # Select city from
    browser.element('[name="city_from"]').type('Москва').press_enter()

    # Select city to
    browser.element('[name="city_to"]').type('Сочи').press_enter()

    # Select date From
    browser.element('[name="date_from"]').type('24.09.2024').press_enter()

    # Select date To
    browser.element('[name="date_back"]').type('28.11.2024')

    # Select the number of passengers
    browser.element('[class="counter_adult_wrp"]').element('[class="increase"]').click()

    # Select class
    browser.element('[class="j-dropdown"]').click()
    browser.element('[data-value="C"]').click()

    # Submit selection
    browser.element('[class="button_wrp j-buttons_block"]').click()
