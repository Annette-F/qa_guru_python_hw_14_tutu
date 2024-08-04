from allure_commons.types import Severity
import allure
from pages.authorization_page import authorization_page
from pages.change_language_page import language_page
from pages.edit_personal_data_page import profile_page
from pages.search_aviatickets_page import search_aviaticket


# def test_decorator_labels():
@allure.tag('Web')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'Annette-F')
@allure.feature('Authorization with valid login and password')
@allure.story('Authorization')
@allure.link('https://www.tutu.ru', name='Tutu.ru')
def test_valid_authorization():
    authorization_page.open()
    authorization_page.open_authorization_page()
    authorization_page.fill_email()
    authorization_page.fill_password()
    # authorization_page.fill_email('marivtest@mail.ru')
    # authorization_page.fill_password('qwerty123')
    authorization_page.submit_authorization()
    authorization_page.should_have_logout_form()


@allure.tag('Web')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'Annette-F')
@allure.feature('Authorization with wrong password')
@allure.story('Authorization')
@allure.link('https://www.tutu.ru', name='Tutu.ru')
def test_authorization_with_wrong_password():
    authorization_page.open()
    authorization_page.open_authorization_page()
    authorization_page.fill_email()
    authorization_page.fill_wrong_password()
    # authorization_page.fill_email('marivtest@mail.ru')
    # authorization_page.fill_password('zxcv1234')
    authorization_page.submit_authorization()
    authorization_page.should_have_text('Неверный адрес почты или пароль.')


@allure.tag('Web')
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'Annette-F')
@allure.feature('Update profile')
@allure.story('Profile')
@allure.link('https://www.tutu.ru', name='Tutu.ru')
def test_update_personal_data():
    authorization_page.open()
    authorization_page.open_authorization_page()
    authorization_page.fill_email()
    authorization_page.fill_password()
    authorization_page.submit_authorization()
    profile_page.open_profile()
    profile_page.type_first_name('Maria')
    profile_page.type_middle_name('Ivanovna')
    profile_page.type_last_name('Petrova')
    profile_page.type_phone('9007778899')
    profile_page.type_birthday('20.04.2000')
    profile_page.confirm_agreement_form()
    profile_page.submit_edit_form()
    profile_page.open_main_page()


@allure.tag('Web')
@allure.severity(Severity.MINOR)
@allure.label('owner', 'Annette-F')
@allure.feature('Page language changes')
@allure.story('Page language')
@allure.link('https://www.tutu.ru', name='Tutu.ru')
def test_change_language_page():
    authorization_page.open()
    language_page.select_eng_language()
    language_page.select_rus_language()


@allure.tag('Web')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'Annette-F')
@allure.feature('Search aviatickets')
@allure.story('Page aviatickets')
@allure.link('https://www.tutu.ru', name='Tutu.ru')
def test_search_aviaticket():
    authorization_page.open()
    search_aviaticket.type_city_from('Москва')
    search_aviaticket.type_city_to('Сочи')
    search_aviaticket.type_date_from('24.09.2024')
    search_aviaticket.type_date_to('28.11.2024')
    search_aviaticket.count_adult_passengers()
    search_aviaticket.select_class()
    search_aviaticket.submit_selection()
