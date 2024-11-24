[![pipeline status](https://gitlab.crja72.ru/django/2024/autumn/course/students/196470-maxpawgdbs-course-1187/badges/main/pipeline.svg)](https://gitlab.crja72.ru/django/2024/autumn/course/students/196470-maxpawgdbs-course-1187/-/pipelines)

![image](https://gitlab.crja72.ru/django/2024/autumn/course/students/196470-maxpawgdbs-course-1187/-/raw/main/Main_ER.png)

Проект разработан под Python 3.11
### Установка и запуск виртуального окружение
```
python3 -m venv venv
source venv/bin/activate
```

### Установка зависимостей

#### PROD
```
pip3 install -r requirements/prod.txt
```

#### TEST
```
pip3 install -r requirements/test.txt
```

#### DEV
```
pip3 install -r requirements/dev.txt
```

##### Перенос шаблона .env
```
cat .env.template >> .env
```

### Запуск сервера
```
cd lyceum
python3 manage.py runserver
```

### Запуск тестов
```
python3 lyceum/manage.py test
```

### Локализация
##### Установка gettext
```
sudo apt install gettext
```
##### Создаём перевод
```
django-admin compilemessages
```
