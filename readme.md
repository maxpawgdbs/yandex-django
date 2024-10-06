УСТАНОВКА И ЗАПУСК ВИРТУАЛЬНОГО ОКРУЖЕНИЯ
python3 -m venv venv
source venv/bin/activate

УСТАНОВКА ЗАВИСИМОСТЕЙ
PROD
pip3 install -r requirements/prod.txt
TEST
pip3 install -r requirements/test.txt
DEV
pip3 install -r requirements/dev.txt

ЗАДАНИЕ ПЕРЕМЕННЫХ ОКРУЖЕНИЯ
cd lyceum
cd lyceum
cat .env.template >> example.env

ЗАПУСК СЕРВЕРА
cd lyceum
python3 manage.py runserver

ЗАПУСК ТЕСТОВ
cd lyceum
python3 manage.py test

СТАТУС ПАЙПЛАЙНА ПОСЛЕДНЕГО КОММИТА
[![pipeline status](https://gitlab.crja72.ru/django/2024/autumn/course/students/196470-maxpawgdbs-course-1187/badges/main/pipeline.svg)](https://gitlab.crja72.ru/django/2024/autumn/course/students/196470-maxpawgdbs-course-1187/-/pipelines)