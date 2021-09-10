### Описание:
Проект сервиса API для Avito.

Создана документация http://127.0.0.1:8000/redoc/.

В качестве отправителя платежа берется текущий пользователь. 
Аутентификацию не добавляла, т.к. если интегрировать в систему стоить взять существующий способ аутентификации.

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
{   "count": 2,
    "next": null,
    "previous": null,
    "results": [
        {   "id": 1,
            "username": "user1"  },
            
        {   "id": 2,
            "username": "user2"  }    ]}
```
##### GET запрос на получение баланса пользователя:
```
/api/users/{user_id}/balance/
```
```
{   "count": 12,
    "next": null,
    "previous": null,
    "results": [
        
        {   "id": 12,
            "balance": 1200,
            "sum_rub": 100,
            "created": "2021-09-10 - 17:30:31",
            "currency": "RUR",
            "operation": "transfer from user1",
            "owner": 1
        },
```
##### POST запрос на пополнение счета:
```
/api/users/{user_id}/refill/
```
```
{"sum": 1000}
```
```
{   "id": 10,
    "date": "2021-09-10 - 19:11:50",
    "sum": 1000,
    "operation": "refill",
    "currency": "RUR",
    "balance": 2300,
    "sender": 1,
    "receiver": 1   }
```
##### POST запрос на перевод между пользователями:
```
/api/users/{user_id}/transfer/
```
```
{   "sum": 100,
    "receiver": 2 }
```
```
 {  "id": 11,
    "date": "2021-09-10 - 19:13:20",
    "sum": 100,
    "operation": "transfer",
    "currency": "RUR",
    "balance": 2200,
    "sender": 1,
    "receiver": 1  }
```
##### POST запрос на снятие со счета:
```
/api/users/{user_id}/withdraw/
```
```
{   "sum": 100   }
```
```
 {  "id": 12,
    "date": "2021-09-10 - 19:24:28",
    "sum": 100,
    "operation": "withdraw",
    "currency": "RUR",
    "balance": 2100,
    "sender": 1,
    "receiver": 1   }
```
##### DELETE запрос на удаление платежа:
```
/api/users/{user_id}/transfer/{id}/
```

### Описания ошибок:
* Попытка снятия, перевода со счета суммы превышающей баланс
```
"Недостаточно средств на счете."
```
* Неверно введенная сумма - отрицательная либо 0.
```
"Сумма должна быть больше 0"
```
* Не указан получатель средств либо такого пользователя нет.
```
"Получателя не существует, проверьте номер получателя."
```
* Отправитель и получатель совпадают.
```
"Получатель и отправитель совпадают, проверьте получателя."
```
