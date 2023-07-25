 # “Parsing_orm_postgresql”
 [![License: MIT](https://img.shields.io/badge/License-MIT-brightgreen.svg)](https://opensource.org/licenses/MIT)


## Описание
Цель: Написать программу, которая будет парсить файл excel и загружать данные в базу postgresql.

## Требования к реализации
- Загрузка в базу должна осуществляться с помощью Django ORM.
- База данных Postgresql.
- Можно пользоваться любыми библиотеками.

## **Стек:**
![python version](https://img.shields.io/badge/Python-3.11-green) ![django version](https://img.shields.io/badge/Django-4.2.3-green)


### **Дополнительные библиотеки:**
[![Pandas Version](https://img.shields.io/badge/Pandas-2.0.3-blue.svg)](https://pandas.pydata.org/)
[![Openpyxl Version](https://img.shields.io/badge/Openpyxl-3.1.2-blue.svg)](https://openpyxl.readthedocs.io/en/stable/)
[![django-extensions](https://img.shields.io/badge/django--extensions-3.2.3-blue)](https://pypi.org/project/django-extensions/)
[![Psycopg2-Binary](https://img.shields.io/badge/Psycopg2--Binary-v2.9.6-blue)](https://pypi.org/project/psycopg2-binary/)
[![python-dotenv](https://img.shields.io/badge/python--dotenv-1.0.0-blue)](https://pypi.org/project/python-dotenv/)


## **Схема(структура) базы данных:**
<img src="screens/chema_db.jpg" alt="img_6.png" width="700">

## **Запуск проекта в dev-режиме**
Инструкция ориентирована на операционную систему Windows и утилиту git bash.<br/>
##### Для прочих инструментов используйте аналоги команд для вашего окружения.

1. Клонируйте репозиторий и перейдите в него в командной строке:
```python
git clone https://github.com/artyom-vah/parsing_orm_postgresql.git
```

2. Установите и активируйте виртуальное окружение
```python
python -m venv venv
```

```python
source venv/Scripts/activate
```

_или сразу так:_

```python
python -m venv venv && . venv/Scripts/activate
```

3. Обновите pip 
```python
python -m pip install --upgrade pip
```

4. Установите зависимости из файла requirements.txt
```python
pip install -r requirements.txt
```
5. Если нужно запустить базу данных [sqlite3](sqlite3), то в файле settings.py раскомментируем:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```
_и делаем миграции:_
```python
python manage.py makemigrations 
```
```python
python manage.py migrate
```

5.1 Если нужно запустить базу данных postgresql, сначала создаем бд в pgAdmin, далее добавляем файл [.env](.env) в папку [project](project) (там где находится файл [settings.py](project%2Fsettings.py))
 в нем прописываем 
```python
DB_ENGINE=django.db.backends.postgresql_psycopg2
DB_NAME=postgres # testdb например 
DB_USER=postgres
DB_PASSWORD=postgres # 12345678 например 
DB_HOST=localhost
DB_PORT=5432
```
_в DB_NAME прописываем имя базы данных, в DB_PASSWORD прописываем пароль_

6. В файле settings.py прописываем:
```python
DATABASES = {
    'default': {
        'ENGINE': os.getenv('DB_ENGINE', default='django.db.backends.postgresql_psycopg2'),
        'NAME': os.getenv('DB_NAME', default='postgres'),
        'USER': os.getenv('POSTGRES_USER', default='postgres'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD', default='postgres'),
        'HOST': os.getenv('DB_HOST', default='localhost'),
        'PORT': os.getenv('DB_PORT', default='5432')
    }
}
```

7. В папке с файлом manage.py создайте и выполните миграции:

```python
python manage.py makemigrations 
```
```python
python manage.py migrate
```

**Скрины из базы данных Postgres :**

<img src="screens/bd_1.jpg" alt="img_6.png" width="200">

<img src="screens/bd_2.jpg" alt="img_6.png" width="500">

<img src="screens/bd_3.jpg" alt="img_6.png" width="500">

<img src="screens/bd_4.jpg" alt="img_6.png" width="500">

<img src="screens/bd_5.jpg" alt="img_6.png" width="500">

<img src="screens/bd_6.jpg" alt="img_6.png" width="500">

<img src="screens/bd_7.jpg" alt="img_6.png" width="500">

<br>
**Автор проекта: Артем Вахрушев.**