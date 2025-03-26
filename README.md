# ToDo List Application with Admin Panel

Простое веб-приложение для управления задачами с возможностью аутентификации пользователей и админ-панелью.

> [!CAUTION]
> Внутри происходит просто ужас, код и api можно приравнять к военному преступлению в программировании... в будущем переделаю(наверное)

## 🛠 Технологии
- **Backend**: FastAPI, SQLAlchemy, PostgreSQL
- **Frontend**: Jinja2, HTML/CSS, JavaScript
- **Аутентификация**: JWT

## 🌟 Возможности
- Регистрация и аутентификация пользователей
- Создание, удаление задач
- Отметка задач как выполненных
- Админ-панель:
  - Просмотр статистики
  - Управление пользователями
  - Просмотр всех задач в системе
    
- Основные эндпоинты:

  - `POST /api/v1/auth/login` - Авторизация
  - `POST /api/v1/auth/register` - Регистрация
  - `GET /api/v1/user/{username}` - Профиль пользователя
  - `PATCH /api/v1/user/{username}` - Изменение ролей пользователя
  - `DELETE /api/v1/user/{username}` - Удаление пользователя и его заметок
  - `POST /api/v1/user/{username}/ToDos/createToDo` - Cоздание заметки
  - `GET /api/v1/user/{username}/ToDos/{task_id}` - Получение заметки
  - `PATCH /api/v1/user/{username}/ToDos/{task_id}` - Изменения статуса заметки на выполнено
  - `DELETE /api/v1/user/{username}/ToDos/{task_id}` - Удаление заметки

POST /api/v1/todos - Создание задачи
## 🌟 Скриншоты интерфейса
- Главная страница
  
  ![Главная страница](https://github.com/awatdsu/ToDo_FastAPI/blob/main/assets/index.png)

- Страница входа

  ![Страница входа](https://github.com/awatdsu/ToDo_FastAPI/blob/main/assets/login.png)

- Страница профиля

  ![Страница профиля](https://github.com/awatdsu/ToDo_FastAPI/blob/main/assets/profile.png)

- Админ панель

  ![Админ панель](https://github.com/awatdsu/ToDo_FastAPI/blob/main/assets/admin.png)

- Админ панель, профиль пользователя

  ![Админ панель, профиль пользователя](https://github.com/awatdsu/ToDo_FastAPI/blob/main/assets/admin_profile.png)
