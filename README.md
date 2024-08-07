# Проект по автоматизации тестирования онлайн-сервиса путешествий [Tutu.ru](https://www.tutu.ru)

## Содержание

- [Технологии и инструменты](#octocat-технологии-и-инструменты)
- [Список реализованных проверок в автотестах](#white_check_mark-список-реализованных-проверок-в-автотестах)
- [Запуск тестов в Jenkins с параметрами](#rocketl-Запуск-тестов-в-Jenkins-с-параметрами)
- [Отчет о результатах тестирования в Allure-reports](#bookmark_tabs-Отчет-о-результатах-тестрования-в-Allure-reports)
- [Уведомление в Telegram о результатах проверки с использованием бота](#loudspeaker-Уведомление-в-Telegram-о-результатах-проверки-с-использованием-бота)
- [Видео-отчет прохождения теста на Selenoid](#movie_camera-Видео-отчет-прохождения-теста-на-Selenoid)


#### [Сайт онлайн-сервиса Tutu](https://www.tutu.ru)


## Цель проекта

Тестирование основных функций онлайн-сервиса, позволяющих пользователям пройти успешную авторизацию, заполнить персональные данные в личном кабинете, успешно найти необходимую информацию по наличию и стоимости билетов.

## :octocat: Технологии и инструменты

<p align="left">
<img src="https://raw.githubusercontent.com/Annette-F/Annette-F/main/icons/python.svg" width="50" heigth="50"/>
<img src="https://raw.githubusercontent.com/Annette-F/Annette-F/main/icons/jenkins.svg" width="50" heigth="50"/>
<img src="https://raw.githubusercontent.com/Annette-F/Annette-F/main/icons/pycharm.svg" width="50" heigth="50"/>
<img src="https://raw.githubusercontent.com/Annette-F/Annette-F/main/icons/pytest.svg" width="50" heigth="50"/>
<img src="https://raw.githubusercontent.com/Annette-F/Annette-F/main/icons/github.svg" width="50" heigth="50"/>
<img src="https://raw.githubusercontent.com/Annette-F/Annette-F/main/icons/visualstudio.svg" width="50" heigth="50"/>
<img src="https://github.com/Annette-F/qa_guru_python_hw_14_tutu/blob/main/resources/images/AllureReport.png" height="50" width="50">
<img src="https://github.com/Annette-F/qa_guru_python_hw_14_tutu/blob/main/resources/images/Selenoid.png" height="50" width="50">
<img src="https://github.com/Annette-F/qa_guru_python_hw_14_tutu/blob/main/resources/images/selene.png" height="50" width="50">
<img src="https://raw.githubusercontent.com/Annette-F/Annette-F/main/icons/Telegram.svg" width="50" heigth="50"/>
</p>

## :white_check_mark: Список реализованных проверок в автотестах

- Проверка успешной авторизации пользователя
- Проверка отсутствия авторизации при вводе неверного пароля
- Редактирование данных профиля пользователя
- Изменение изыка сайта
- Поиск авиабилетов
- Поиск информации в разделе Справочная


## :rocket: Запуск тестов в Jenkins с параметрами

Сборка, параметризация и запуск проекта производятся с помощью Jenkins. При каждом запросе на тестирование браузера Selenoid запускает новый Docker-контейнер и останавливает его после закрытия браузера. Перед запуском можно указать версию браузера (в данном случае запуск тестов проводился на браузере Chrome версии 126.0). Также в параметрах добавлена возможность выбора окружения, на котором будут запущены тесты. 

<p>
<img title="Jenkins" src="resources/photo/jenkins.png">
</p>

## :bookmark_tabs: Отчет о результатах тестирования в Allure-reports

После прохождения тестов автоматически формируется отчет в Allure Report. Открыть его можно пройдя по [ссылке](https://jenkins.autotests.cloud/job/qa_guru_014_tutu/19/allure/). 
Allure формирует подробный отчет о результатах прогона тестов. Кастомные фильтры и листенеры делают отчет максимально понятным. Например, в отчет пишутся все селекторы и методы Selene, отчеты формируются по категориям.
После окончания выполнения автотестов по каждому из них в отчете доступны скриншоты, лог консоли браузера и видеозапись выполнения теста.

<p>
<img title="Allure общая статистика" src="resources/photo/allure.png">
<img title="Allure графики" src="resources/photo/allure2.png">
<img title="Allure отчет" src="resources/photo/allure3.png">
<img title="Allure отчет" src="resources/photo/allure4.png">
</p>

## :loudspeaker: Уведомление в Telegram о результатах проверки с использованием бота.

Настроено автоматическое оповещение о результатах прохождения тестов в Telegram-бот с полной информацией о прогоне и ссылкой на Allure

<p>
<img title="Telegram" src="resources/photo/telegram.png">
</p>

## :movie_camera: Видео прохождения тестов на Selenoid

Пример видеозаписи выполнения теста.

<p>
<img title="Video" src="resources/video/video.gif" alt="video">
</p>
