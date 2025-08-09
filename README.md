# Фінальний проєкт: Мікросервіс для аналізу творів мистецтва

Мікросервіс на **FastAPI** для демонстрації архітектури аналізу арт-даних із використанням AI.  
Сервіс підключається до **PostgreSQL** через **SQLAlchemy** та надає REST API.

## Стек технологій
- **Мова:** Python 3.9+
- **Фреймворк:** FastAPI
- **Сервер:** Uvicorn (ASGI)
- **База даних:** PostgreSQL
- **ORM:** SQLAlchemy
- **Драйвер БД:** Psycopg2
- **Валідація:** Pydantic
- **Залежності:** pip, venv
- **Документація API:** Swagger UI (автоматично)

---

## Необхідне ПЗ
- [Git](https://git-scm.com/downloads)
- [Python 3.9+](https://www.python.org/downloads/)
- [PostgreSQL](https://www.postgresql.org/download/)

---

## Покроковий запуск

### 1) Клонування репозиторію
```bash
git clone https://github.com/KubriakZahoor107/Python51.git
cd Python51
2) Налаштування бази даних
sql
Копировать
Редактировать
CREATE USER myuser WITH PASSWORD 'your_password';
CREATE DATABASE artculture_db OWNER myuser;
3) Віртуальне середовище та залежності
macOS / Linux:

bash
Копировать
Редактировать
python3 -m venv .venv
source .venv/bin/activate
Windows:

bash
Копировать
Редактировать
python -m venv .venv
.venv\Scripts\activate
Встановіть залежності:

bash
Копировать
Редактировать
pip install -r requirements.txt
Створіть .env:

env
Копировать
Редактировать
DATABASE_URL="postgresql://myuser:your_password@localhost:5432/artculture_db"
4) Запуск сервісу
bash
Копировать
Редактировать
uvicorn main:app --reload --reload-exclude .venv
Сервіс буде доступний за адресою:
http://127.0.0.1:8000
http://127.0.0.1:8000/docs

Приклад використання (ID = 9)
GET /art-terms — Try it out → Execute → знайти "id": 9

GET /ai/analyze-artwork/9 — Try it out → Execute → оригінальний і AI-згенерований опис

Примітка про AI
Для демонстрації роботи сервісу я імітував відповідь від AI.
Підключення реальної моделі: main.py → analyze_artwork.
Це дозволило сконцентруватися на архітектурі сервісу та його взаємодії з базою даних.

Архітектура та опис компонентів
FastAPI (Рівень API)
Роль: Основний фреймворк, що створює веб-сервер та API-ендпоінти.

Взаємодія: Керує всім процесом, викликаючи необхідні функції та валідуючи дані за допомогою Pydantic.

SQLAlchemy (Рівень доступу до даних)
Роль: "Перекладач" між об'єктами Python та реляційною базою PostgreSQL.

Взаємодія: Через db: Session надсилає запити до бази для читання/запису.

PostgreSQL (Рівень даних)
Роль: Надійна реляційна база для зберігання всіх даних.

Взаємодія: Виконує SQL-запити, які для неї генерує SQLAlchemy.

Uvicorn (Веб-сервер)
Роль: ASGI-сервер, який є "двигуном" для FastAPI-застосунку.

Взаємодія: Приймає з'єднання і передає їх на обробку у FastAPI.

Схема роботи запиту /ai/analyze-artwork/9
Uvicorn приймає запит.

FastAPI отримує, валідує id=9 і викликає функцію.

SQLAlchemy робить запит до PostgreSQL.

PostgreSQL знаходить дані і повертає їх.

SQLAlchemy перетворює відповідь у Python-об'єкт.

Код імітує роботу AI, генеруючи новий опис.

FastAPI віддає результат у форматі JSON.
