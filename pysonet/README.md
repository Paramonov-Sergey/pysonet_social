## Инструменты разработки
## Стек:
    Python >= 3.8
    Django Rest Framework
    Postgres
# Старт
#### 1) Сделать форк репозитория
### 2) Клонировать репозиторий
    git clone ссылка_сгенерированная_в_вашем_репозитории
### 3) Создать образ
    docker-compose build
### 4) Запустить контейнер   
    docker-compose up
### 5) Создать суперюзера
    docker exec -it pysonet_pysonet_back_1 python manage.py createsuperuser
### 6) Перейти по адресу
    http://127.0.0.1:8000/api/v1/swagger/
### 7) Если нужно очистить БД
    docker-compose down -v
