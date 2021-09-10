# Описание:
Проект сервиса API для Avito.

Создана документация http://127.0.0.1:8000/redoc/.

# Позволяет:
* получать, создавать, изменять и удалять пользователей;
* получать, создавать, изменять и удалять платежи пользователей;
* получать, создавать, изменять и удалять переводы пользователей;
* получать, фильтровать баланс пользователей;

# Используемые технологии:
* Django==3.2.6
* pytz==2021.1* 
* Python 3.7
* djangorestframework-queryfields
* django-filter
* drf-yasg

# Как запустить проект:
Клонировать репозиторий и перейти в него в командной строке:
```bash
git clone https://github.com/feyaschuk/autumn-2021-intern-assignment.git
```
```bash
cd api_avito
```
Cоздать и активировать виртуальное окружение:
```bash
python3 -m venv env
source env/bin/activate или для Win10 source venv/Scripts/activate
python3 -m pip install --upgrade pip
```
Установить зависимости из файла requirements.txt:
```bash
pip install -r requirements.txt
```
Выполнить миграции:
```bash
python3 manage.py migrate
```
Запустить проект:
```bash
python3 manage.py runserver
```
# Примеры запросов:
