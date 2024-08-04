from allure_commons.types import Severity
import allure
from pages.authorization_page import AuthorizationUserPage
from pages.change_language_page import ChangeLanguagePage
from pages.edit_personal_data_page import EditPersonalData
from pages.search_aviatickets_page import SearchAviatickets


# def test_decorator_labels():
@allure.tag('Web')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'Annette-F')
@allure.feature('Authorization with valid login and password')
@allure.story('Authorization')
@allure.link('https://www.tutu.ru', name='Tutu.ru')
def test_valid_authorization():
    with allure.step('Open main page https://www.tutu.ru'):
        authorization_page = AuthorizationUserPage()
        authorization_page.open()

    with allure.step('Открываем окно авторизации'):
        authorization_page.open_authorization_page()

    with allure.step('Заполняем поле ввода Email'):
        authorization_page.fill_email('marivtest@mail.ru')

    with allure.step('Заполняем поле ввода Пароль'):
        authorization_page.fill_password('qwerty123')

    with allure.step('Подтверждаем авторизацию пользователя'):
        authorization_page.submit_authorization()

    with allure.step('Проверяем успешную авторизацию'):
        authorization_page.should_have_logout_form()


@allure.tag('Web')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'Annette-F')
@allure.feature('Authorization with wrong password')
@allure.story('Authorization')
@allure.link('https://www.tutu.ru', name='Tutu.ru')
def test_authorization_with_wrong_password():
    with allure.step('Открываем главную страницу сайта https://www.tutu.ru'):
        authorization_page = AuthorizationUserPage()
        authorization_page.open()

    with allure.step('Открываем окно авторизации'):
        authorization_page.open_authorization_page()

    with allure.step('Заполняем поле ввода Email'):
        authorization_page.fill_email('marivtest@mail.ru')

    with allure.step('Заполняем поле ввода Пароль'):
        authorization_page.fill_password('zxcv1234')

    with allure.step('Подтверждаем успешную авторизацию пользователя'):
        authorization_page.submit_authorization()

    with allure.step('Проверяем, что авторизация не прошла'):
        authorization_page.should_have_text('Неверный адрес почты или пароль.')


@allure.tag('Web')
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'Annette-F')
@allure.feature('Update profile')
@allure.story('Profile')
@allure.link('https://www.tutu.ru', name='Tutu.ru')
def test_update_personal_data():
    with allure.step('Открываем главную страницу сайта https://www.tutu.ru'):
        authorization_page = AuthorizationUserPage()
        authorization_page.open()

    with allure.step('Открываем окно авторизации'):
        authorization_page.open_authorization_page()

    with allure.step('Заполняем поле ввода Email'):
        authorization_page.fill_email('marivtest@mail.ru')

    with allure.step('Заполняем поле ввода Пароль'):
        authorization_page.fill_password('qwerty123')

    with allure.step('Подтверждаем авторизацию пользователя'):
        authorization_page.submit_authorization()

    with allure.step('Открываем профиль пользователя'):
        profile_page = EditPersonalData()
        profile_page.open_profile()

    with allure.step('Заполняем поле ввода Имя'):
        profile_page.type_first_name('Maria')

    with allure.step('Заполняем поле ввода Отчество'):
        profile_page.type_middle_name('Ivanovna')

    with allure.step('Заполняем поле ввода Фамилия'):
        profile_page.type_last_name('Petrova')

    with allure.step('Заполняем поле ввода Номер телефона'):
        profile_page.type_phone('9007778899')

    with allure.step('Заполняем поле Дата рождения'):
        profile_page.type_birthday('20.04.2000')

    with allure.step('Отмечаем согласие на обработку персональных данных'):
        profile_page.confirm_agreement_form()

    with allure.step('Подтверждаем редактирование профиля'):
        profile_page.submit_edit_form()

    with allure.step('Возвращаемся на главную страницу'):
        profile_page.open_main_page()


@allure.tag('Web')
@allure.severity(Severity.MINOR)
@allure.label('owner', 'Annette-F')
@allure.feature('Page language changes')
@allure.story('Page language')
@allure.link('https://www.tutu.ru', name='Tutu.ru')
def test_change_language_page():
    with allure.step('Открываем главную страницу сайта https://www.tutu.ru'):
        authorization_page = AuthorizationUserPage()
        authorization_page.open()

    with allure.step('Меняем язык отображения страницы на английский'):
        language_page = ChangeLanguagePage()
        language_page.select_eng_language()

    with allure.step('Меняем язык отображения страницы на русский'):
        language_page.select_rus_language()


@allure.tag('Web')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'Annette-F')
@allure.feature('Search aviatickets')
@allure.story('Page aviatickets')
@allure.link('https://www.tutu.ru', name='Tutu.ru')
def test_search_aviaticket():
    with allure.step('Открываем главную страницу сайта https://www.tutu.ru'):
        authorization_page = AuthorizationUserPage()
        authorization_page.open()

    with allure.step('Выбираем город отправления'):
        search_aviaticket = SearchAviatickets()
        search_aviaticket.type_city_from('Москва')

    with allure.step('Выбираем город прибытия'):
        search_aviaticket.type_city_to('Сочи')

    with allure.step('Выбираем дату вылета'):
        search_aviaticket.type_date_from('24.09.2024')

    with allure.step('Выбираем дату обратного билета'):
        search_aviaticket.type_date_to('28.11.2024')

    with allure.step('Выбираем количесиво взрослых пассажиров'):
        search_aviaticket.count_adult_passengers()

    with allure.step('Выбираем класс '):
        search_aviaticket.select_class()

    with allure.step('Подтверждаем выбор'):
        search_aviaticket.submit_selection()
