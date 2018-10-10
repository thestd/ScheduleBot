# Розклад-бот для студентів та викладачів

Частина університетів України використовує електронний розклад від ПП "Політек-софт".
Розклад працює в формі веб-сайту, що є не дуже зручно для використання студентами та викладачами.
В 2017 році студент ПНУ ім. В. Стефаника Тимур Фараджев запустив першу версію свого бота (з використанням РНР) в Телеграмі,
мета якого - зручний доступ до розкладу. Бот зберігав дані про користувача, через що не виникало потреби 
щораз вводити групу/факультет/ім'я викладача та дати для отримання розкладу. 

З дозволу автора, ідея була імплементована по-новому з використанням _Python_, _PostgreSQL_ та бібліотеки 
_Python-telegram-bot_.

На разі створено 2 боти на основі даного коду для ПНУ ім. В. Стефаника (t.me/std_pnu_rozklad) та
ІФНТУНГ (t.me/std_nafta_bot).


## Створення власного розклад-бота

1. Клонуйте даний код на свій сервер.
2. Створіть бота та отримайте токен за допомогою Bot Father (t.me/BotFather)
3. в `config/settings.py` змініть `BOT_TOKEN` на власний
4. Змініть посилання на сайт з розкладом (`SCHEDULE_HOST`)
5. В якості Системи керування базою даних використовується PostgreSQL. Інсталюйте її на свій сервер
    та створіть користувача і базу даних. Змініть параметри в блоці `DATABASE` на відповідні.
    
    Створення БД з користувачем:
    ```postgresql
    CREATE DATABASE <database_name>;
    CREATE USER <database_user> WITH PASSWORD '<database_password>';
    ALTER ROLE <database_user> SET client_encoding TO 'utf8'; 
    ALTER ROLE <database_user> SET default_transaction_isolation TO 'read committed'; 
    ALTER ROLE <database_user> SET timezone TO 'UTC'; 
    ALTER USER <database_user> CREATEDB; 
    GRANT ALL PRIVILEGES ON DATABASE <database_name> TO <database_user>;
    ```
6. Створіть віртуальне середовище (virtualenv) та інсталюйте залежності 
    ```
    pip install -r requirements.txt
    ```
    Активуйте його
    ```
    source <your_venv>/bin/activate
    ```
7. Запустіть код на виконання. За замовчуванням бот працює по схемі _polling_. В `config/settings.py`
є налаштування для запуску бота в режимі _webhook_




