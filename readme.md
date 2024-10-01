Команды ниже приведены для linux, но возможно вам надо запустить на windows,
так что вот аналоги этих команд для windows(формат linux - windows):
source - call
pip3 - pip
python3 - python
Также если у вас windows, то не забудьте взять пути к файлам в кавычки

Команды для установки и запуска виртуального окружения:
python3 -m venv venv
source venv/bin/activate
(для windows путь "Название_папки/Scripts/activate.bat")

Установка зависимостей:
pip3 install -r requirements.txt

cd lyceum
python3 manage.py runserver
