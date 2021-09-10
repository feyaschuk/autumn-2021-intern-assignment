### Описание:
Проект сервиса API для Avito.

Создана документация http://127.0.0.1:8000/redoc/.

### Позволяет:
* получать, создавать, изменять и удалять пользователей;
* получать, создавать, изменять и удалять платежи пользователей;
* получать, создавать, изменять и удалять переводы пользователей;
* получать, фильтровать баланс пользователей;

### Используемые технологии:
* Django==3.2.6
* pytz==2021.1* 
* Python 3.7
* djangorestframework-queryfields
* django-filter
* drf-yasg

### Как запустить проект:
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
### Примеры запросов и ответов:
##### POST запрос на регистрацию пользователя:
```bash
/api/users/
```
```bash
{"username": "string"}
```
```bash
{ "id": 1,
  "username": "user1"}
```
##### GET запрос на получение списка пользователей:
```
/api/users/
```

```
{
    "count": 2,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "username": "user1"
        },
        {
            "id": 2,
            "username": "user2"
        }
    ]
}
```
##### DELETE запрос на удаление категории:
```
/api/v1/categories/{slug}/
```
##### GET запрос на получение списка жанров:
```
/api/v1/genres/
```
##### POST запрос на добавление жанры:
```
/api/v1/genres/
```
##### DELETE запрос на удаление жанры:
```
/api/v1/genres/{slug}/
```
##### GET запрос на получение списка произведений:
```
/api/v1/titles/
```
##### POST запрос на добавление произведения:
```
/api/v1/titles/
```
##### GET запрос на получение конкретного произведения:
```
/api/v1/titles/{title_id}/
```
##### PATCH запрос на изменения произведения:
```
/api/v1/titles/{title_id}/
```
##### DELETE запрос на удаление произведения:
```
/api/v1/titles/{title_id}/
```
##### GET запрос на получение списка отзывов:
```
/api/v1/titles/{title_id}/reviews/
```
##### POST запрос на добавление отзыва:
```
/api/v1/titles/{title_id}/reviews/
```
##### GET запрос на получение конкретного отзыва:
```
/api/v1/titles/{title_id}/reviews/{review_id}/
```
##### PATCH запрос на изменения отзыва:
```
/api/v1/titles/{title_id}/reviews/{review_id}/
```
##### DELETE запрос на удаление отзыва:
```
/api/v1/titles/{title_id}/reviews/{review_id}/
```
##### GET запрос на получение списка комментариев:
```
/api/v1/titles/{title_id}/reviews/{review_id}/comments/
```
##### POST запрос на добавление комментария:
```
/api/v1/titles/{title_id}/reviews/{review_id}/comments/
```
##### GET запрос на получение конкретного комментария:
```
/api/v1/titles/{title_id}/reviews/{review_id}/comments/{comment_id}/
```
##### PATCH запрос на изменения комментария:
```
/api/v1/titles/{title_id}/reviews/{review_id}/comments/{comment_id}/
```
##### DELETE запрос на удаление комментария:
```
/api/v1/titles/{title_id}/reviews/{review_id}/comments/{comment_id}/
```
##### GET запрос на получение списка пользователей:
```
/api/v1/users/
```
##### POST запрос на добавление пользователя:
```
/api/v1/users/
```
##### GET запрос на получение конкретного пользователя:
```
/api/v1/users/{username}/
```
##### PATCH запрос на изменения пользователя:
```
/api/v1/users/{username}/
```
##### DELETE запрос на удаление пользователя:
```
/api/v1/users/{username}/
```
##### GET запрос на получение данных своей учетной записи:
```
/api/v1/users/me/
```
##### PATCH запрос на изменение данных своей учетной записи:
```
/api/v1/users/me/
```
