Команды ниже приведены для linux, но возможно вам надо запустить на windows,
так что вот аналоги этих команд для windows(формат linux - windows):
source - call
pip3 - pip
python3 - python
export - SET
Также если у вас windows, то не забудьте взять пути к файлам в кавычки

Команды для установки и запуска виртуального окружения:
python3 -m venv venv
source venv/bin/activate
(для windows путь "Название_папки/Scripts/activate.bat")

Установка зависимостей:
Для prod-режима:
pip3 install -r requirements/prod.txt
Для test-режима:
pip3 install -r requirements/test.txt
Для dev-режима:
pip3 install -r requirements/dev.txt

Перед запуском проекта откройте файл .env через блокнот и замените значения переменных на свои
Команды для запуска проекта:
cd lyceum
python3 manage.py runserver

Показ статуса пайплайна последнего коммита(это не команды):
[![pipeline status](https://gitlab.crja72.ru/django/2024/autumn/course/students/196470-maxpawgdbs-course-1187/badges/main/pipeline.svg)](https://gitlab.crja72.ru/django/2024/autumn/course/students/196470-maxpawgdbs-course-1187/-/pipelines)