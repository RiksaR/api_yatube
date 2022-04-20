# API_Yatube

## Краткое описание проекта
API_Yatube - это проект, в котором реализован REST API для проекта Yatube.
Аутентификация настроена по JWT-токену.

Ссылка на проект Yatube: https://github.com/RiksaR/Yatube

Yatube - это социальная сеть для публикации дневников. Проект разработан по
классической MVT-архитектуре. Используется пагинация постов и кэширование.
Регистрация реализована с верификацией данных, сменой и восстановлением пароля
через почту. Написаны тесты, проверяющие работу сервиса.

Для того, чтобы запустить проект API_Yatube, необходимо клонировать репозиторий с помощью
команды 
```python
    git clone <адрес репозитория>
```
После этого необходимо зайти в директорию проекта и создать виртуальное
окружение с помощью команды
```python
    python -m venv venv # если у вас Windows
    python3 -m venv venv # если у вас Mac или Linux
```
Запустить виртуальное окружение
```python
    source venv/Scripts/activate # если у вас Windows
    source venv/bin/activate # если у вас Mac или Linux
```
И установить зависимости
```python
    python -m pip install --upgrade pip # если у вас Windows
    python3 -m pip install --upgrade pip # если у вас Mac или Linux
    pip install -r requirements.txt
```

После этого необходимо убедиться, что вы находитесь в директории, в которой
лежит файл manage.py, и выполнить команду
```python
    python manage.py runserver # если у вас Windows
    python3 manage.py runserver # если у вас Mac или Linux
```
Проверить работу API можно, сделав запросы по следующим адресам:
```python
http://127.0.0.1:8000/api/v1/posts/ # список всех постов
http://127.0.0.1:8000/api/v1/posts/{id} # получить пост с определённым id
http://127.0.0.1:8000/api/v1/posts/<post_id>/comments/ # список комментариев
                                                       # к указанному посту
http://127.0.0.1:8000/api/v1/group/ # список всех групп
http://127.0.0.1:8000/api/v1/group/{id} # получить группу с определённым id
http://127.0.0.1:8000/api/v1/follow/ # список подписчиков текущего пользователя
```

### Используемые технологии
Python 3.9  
Django 3.1.6  
Pytest 5.4.1  
SQLite3  
Django REST Framework  
Simple-JWT  

### Автор проекта:
Смоленский Алексей