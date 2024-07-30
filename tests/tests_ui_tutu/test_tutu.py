from selene import browser, have, be


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
    browser.element('#editDForm_first_name').type('Maria')

    # Fill middle name field
    browser.element('#editDForm_middle_name').type('Ivanovna')

    # Fill last name field
    browser.element('#editDForm_last_name').type('Petrova')

    # Fill phone number
    browser.element('#editDForm_phone').type('9007778899')

    # Fill birthday
    browser.element('#editDForm_birthday').type('20.04.2000').click()

    # Check consent to the processing of personal data
    browser.element('#editDForm_agree').click()

    # Submit
    browser.element('#editDForm_submit').click()

    # Open main page
    browser.element('.jUzldXN___logoLink').click()


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

    # Open page with plane tickets
    browser.all('[class="styles__navigation__OSoea"]').element('[data-ti-nav-item="avia"]').click()

    # Select city from
    browser.element('[data-ti="city_from"]').type('Москва').press_enter()

    # Select city to
    browser.element('[data-ti="city_to"]').type('Сочи').press_enter()

    # Select date From
    browser.element('[data-ti="date_fromDate"]').element('[data-ti="order-calendar-navigation-next"]').element(
        '[data-day="24"]').click()

    # Select date To
    browser.element('[data-ti="date_toDate"]').element('[data-ti="order-calendar-navigation-next"]').element(
        '[data-day="26"]').click()

    # Select the number of passengers
    browser.element('[data-ti="passengers_service_class"]').click()
    browser.element('[data-ti="passenger_counter_adult"]').element('[data-ti="plus"]').click()
    browser.element('[data-ti="passenger_counter_child"]').element('[data-ti="plus"]').click()
    browser.element('[data-ti="passenger_counter_infant"]').element('[data-ti="plus"]').click()

    # Select class
    browser.element('[data-ti="class_selector_F"]').should(have.text('Первый')).click()

    # Close modal-windows with passengers
    browser.element('[data-ti="order-popper-close"]').click()

    # Submit selection
    browser.element('[data-ti="order-popper-close"]').click()


def test_research_vacancy():
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


