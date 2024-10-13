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

### Задание переменных окружения
```
cat .env.template >> lyceum/lyceum/example.env
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

##### Статус пайплайна последнего коммита
[![pipeline status](https://gitlab.crja72.ru/django/2024/autumn/course/students/196470-maxpawgdbs-course-1187/badges/main/pipeline.svg)](https://gitlab.crja72.ru/django/2024/autumn/course/students/196470-maxpawgdbs-course-1187/-/pipelines)
(https://gitlab.crja72.ru/django/2024/autumn/course/students/196470-maxpawgdbs-course-118
7/-/blob/main/ER.jpg?ref_type=heads)