# Интернет-магазин (Django-проект)

Этот проект является учебным примером интернет-магазина, созданного в рамках выполнения домашних заданий на курсе по Django. В ходе курса проект будет постепенно дорабатываться, и в конце курса станет полноценным интернет-магазином 

## Функционал

На данный момент в проекте реализовано следующее:
- Настроено виртуальное окружение для проекта.
- Создано приложение catalog.
  
- Реализованы два контроллера:
  - Контроллер для отображения домашней страницы.
  - Контроллер для отображения страницы с контактной информацией.
- Шаблоны для страниц (главная страница и страница с контактами) вынесены в отдельную папку и стилизованы с использованием UIkit Bootstrap.
  
- Подключена СУБД PostgreSQL для раюоты с проектом:
  - создана база данных
  - Внесены изменения в настройки проекта  для подключения к PostgreSQL
    
- Созданы модели Product и Category:
  -Добавлены наименования
  -связь между проектами настроена по принципу "Один ко многим" с использованием поля ForeignKey()
-Настроена работа с медиафайлами для загрузки изображений товаров, добавлена библиотека Pillow для работы с изображениями.

-Реализованы миграции базы данных:
  - Созданы миграции для новых моделей.
  - Применены изменения через инструмент миграций.
  - Произведены тесты на откат миграций.
    
-Админка:
  - Для категорий настроен вывод id и наименования.
  - Для продуктов добавлены фильтры по категории, а также поиск по названию и описанию.
    
-С помощью инструмента shell заполнены категории и выполнены выборки по фильтрам.

## В домашнем задании (20.2) добавлены новые функции, а именно:

  - Новый контроллер и шаблон, которые  отвечают за отображение отдельной страницы с товаром и его описанием;
  - Выведен список товаров в цикле( отображаемое описание карточек ограничено первыми 100 символами);
  - Выделен общий (базовый) шаблон, а также подшаблон с главным меню;
  - Реализован шаблонный фильтр, который преобразует переданный путь в полный путь для доступа к медиафайлу.


## В домашнем задании (22.1) добавлены новые функции, а именно:

  - Для модели продуктов реализован механизм CRUD, задействован модуль django.forms. Условия для пользователей:
    1.могут создавать новые продукты,
    2.не могут создавать продукты с запрещенными словами в названии и описании;
  - Добавлена новая модель «Версия», которая содержит следующие поля:
    продукт,
    номер версии,
    название версии,
    признак текущей версии.
    При наличии активной версии реализуйте вывод в список продуктов информации об активной версии.;
  - Все созданные формы стилизованы в единой стилистике оформления всей платформы. Для этого использован метод__init__

## В домашнем задании (22.2) добавлены новые функции, а именно:

  -  Создано новое приложение для работы с пользователем. Определена собственная модель для пользователя,  задана электронная почта как поле для авторизации.Добавлены поля:аватар,номер телефона,страна
  - Применена функция python manage.py migrate auth zero, чтобы откатить миграции приложения auth
  - В сервисе реализован функционал аутентификации, а именно:Регистрация пользователя по почте и паролю, верификация почты пользователя через отправленное письмо, встроена автоматическая отправка      электронного сообщения пользователю на указанный в форме регистрации адрес, авторизация пользователя, восстановление пароля зарегистрированного пользователя на автоматически сгенерированный        пароль.
 -  Все контроллеры, которые отвечают за работу с продуктами, заакрыты для анонимных пользователей, при этом создаваемые продукты автоматически привязываны к авторизованному пользователю.


## В домашнем задании (23.1) добавлены новые функции, а именно:
  -  Создана группа для роли модератора и описаны необходимые доступы:может отменять публикацию продукта, может менять описание любого продукта,может менять категорию любого продукта.
  -  Внедрены в шаблоны проверка на владельца объекта и отображена кнопка редактирования только пользователям, которые являются владельцами (если пользователь не наделен другими правами).

## В домашнем задании (23.2) добавлены новые функции, а именно:
  -  Установлен брокер для кеширования Redis
  -  Настроено кеширование всего контроллера отображения данных относительно одного продукта
  -  Создана сервисная функция, которая отвечает за выборку категорий и которую можно переиспользовать в любом месте системы. Добавлено низкоуровневое кеширование для списка категорий
  -  Вынесены необходимые настройки в переменные окружения и настроен проект для работы с ними


## Структура проекта

- catalog/ — основное приложение проекта.
  - views.py — содержит контроллеры для отображения страниц.
  - urls.py — настроены URL-адреса для приложения.
  - models.py - содержит модели Product и Category
  - templates/ — содержит шаблоны для страниц:
    - home.html — главная страница.
    - contacts.html — страница контактов.
  -managment/commands/- содержит кастомную команду для загрузки данных в базу данных из JSON-файла
- config/ — основные настройки проекта:
  - urls.py — основной файл URL-адресов проекта, который включает маршруты для приложения catalog.
  - settings.py — настройки проекта.
  - Ekaterina Lyamina, [24.09.2024 00:41]
(.venv) kkatka@ubuntupc:~/PycharmProjects/Homework_19.2$ python3 manage.py showmigrations
admin

## Установка и настройка

1. Склонируйте репозиторий:
   ```bash
   git clone https://github.com/kkatka1/Homework_19.2

Перейдите в директорию проекта:
cd Homework_19.2

Установите и активируйте зависимости проекта
poetry install
poetry shell

Выполните миграции базы данных:
python manage.py migrate

Запустите сервер разработки:
python manage.py runserver

Используемые технологии

Django
UIkit Bootstrap для стилизации шаблонов
PostgreSQL -СУБД для хранения данных
Pillow - для работы с изображением
Python 3.8+
