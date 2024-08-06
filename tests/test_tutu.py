from allure_commons.types import Severity
import allure
from pages.authorization_page import authorization_page
from pages.change_language_page import change_language_page
from pages.edit_personal_data_page import edit_personal_data_page
from pages.search_aviatickets_page import search_aviaticket_page
from pages.query_page import query_page


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
    edit_personal_data_page.open_profile()
    edit_personal_data_page.type_first_name('Maria')
    edit_personal_data_page.type_middle_name('Ivanovna')
    edit_personal_data_page.type_last_name('Petrova')
    edit_personal_data_page.type_phone('9007778899')
    edit_personal_data_page.type_birthday('20.04.2000')
    edit_personal_data_page.confirm_agreement_form()
    edit_personal_data_page.submit_edit_form()
    edit_personal_data_page.open_main_page()


@allure.tag('Web')
@allure.severity(Severity.MINOR)
@allure.label('owner', 'Annette-F')
@allure.feature('Page language changes')
@allure.story('Page language')
@allure.link('https://www.tutu.ru', name='Tutu.ru')
def test_change_language_page():
    authorization_page.open()
    change_language_page.select_eng_language()
    change_language_page.select_rus_language()


@allure.tag('Web')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'Annette-F')
@allure.feature('Search aviatickets')
@allure.story('Page aviatickets')
@allure.link('https://www.tutu.ru', name='Tutu.ru')
def test_search_aviaticket():
    authorization_page.open()
    search_aviaticket_page.type_city_from('Москва')
    search_aviaticket_page.type_city_to('Сочи')
    search_aviaticket_page.type_date_from('24.09.2024')
    search_aviaticket_page.type_date_to('28.11.2024')
    search_aviaticket_page.count_adult_passengers()
    search_aviaticket_page.select_class()
    search_aviaticket_page.submit_selection()
    search_aviaticket_page.should_be_change_search_button()


@allure.tag('Web')
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'Annette-F')
@allure.feature('Search query')
@allure.story('Page query')
@allure.link('https://www.tutu.ru', name='Tutu.ru')
def test_search_query():
    authorization_page.open()
    query_page.information_table()
    query_page.enter_search_query()
    query_page.check_search_query()
