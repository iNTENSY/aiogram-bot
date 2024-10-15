# Aiogram Telegram Chatbot
___

Данный проект представляет собой интеграцию принципов чистой
архитектуры в проект с чат-ботом, основанным в мессенджере Телеграм.

Сам бот является простым. Основная его цель - получить файл с
электронной версией книги, которая присутствует в базе данных.
Технически, вместо базы данных можно использовать объектное хранилище (S3)
на ваше усмотрение.

### Технологический стек:
___

- Язык программирования: Python 3.11+
- База данных: PostgreSQL
- Контейнеризация: Docker
- Фреймворк для работы с Телеграм: aiogram 3.13.1
- Драйвер для PostgreSQL: Psycopg + Asyncpg
- Фреймворк для внедрения зависимостей: Dishka

### Запуск проекта используя контейнеризацию (Docker system)
___
1. Клонируйте репозиторий: `git clone https://github.com/iNTENSY/aiogram-bot.git`
2. Запустите Docker в вашей системе: `sudo systemctl start docker`
3. Установите файл с переменными окружения (`.env`) в каталоге `./doker`. <br>
Для примера используемых переменных окружения обратитесь в файл `.env.production.example`
4. Перейдите в каталог с конфигурационными файлами docker-compose и nginx: `cd ./docker`
5. Соберите контейнеры и запустите их с параметром -d: `sudo docker compose up --build`
6. Проверьте миграции внутри контейнера: `sudo docker compose exec backend alembic revision --autogenerate`
7. Примените миграции: `sudo docker compose exec backend alembic upgrade head`


### Контакты:
___

- Автор: Даценко Дмитрий Игоревич <br>
- Telegram: https://t.me/dmitriydatsenko <br>
- Электронная почта: dmitriydatsenko@inbox.ru <br>
- GitHub: https://github.com/iNTENSY
