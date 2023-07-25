[![License: MIT](https://img.shields.io/badge/License-MIT-brightgreen.svg)](https://opensource.org/licenses/MIT)
 **“Parsing_orm_postgresql”**

## Описание
Цель: Написать программу, которая будет парсить файл excel и загружать данные в базу postgresql.

## Требования к реализации
- Загрузка в базу должна осуществляться с помощью Django ORM.
- База данных Postgresql.
- Можно пользоваться любыми библиотеками.



## **Стек:**
![python version](https://img.shields.io/badge/Python-3.11-green) ![django version](https://img.shields.io/badge/Django-4.2.1-green)


### **Дополнительные библиотеки:**
[![Psycopg2-Binary](https://img.shields.io/badge/Psycopg2--Binary-v2.9.1-blue)](https://pypi.org/project/psycopg2-binary/)
[![Pandas Version](https://img.shields.io/badge/Pandas-1.3.0-blue.svg)](https://pandas.pydata.org/)

Описание вашего проекта и другая полезная информация.

[//]: # ([![django-allauth]&#40;https://img.shields.io/badge/django--allauth-0.54.0-blue?style=flat-square&#41;]&#40;https://django-allauth.readthedocs.io/en/latest/&#41; [![folium]&#40;https://img.shields.io/badge/folium-0.14-blue&#41;]&#40;https://python-visualization.github.io/folium/&#41;  [![django-smart-selects]&#40;https://img.shields.io/badge/geocoder-1.38.1-blue&#41;]&#40;https://pypi.org/project/geocoder/&#41; [![flake8]&#40;https://img.shields.io/badge/flake8-5.0.4-blue&#41;]&#40;https://pypi.org/project/flake8/5.0.4/&#41;)

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

5. Перейдите в папку project/
```python
cd project/
```

6. В папке с файлом manage.py создайте и выполните миграции:
```python
python manage.py makemigrations 
```
```python
python manage.py migrate
```
<br>
**Автор проекта: Артем Вахрушев.**