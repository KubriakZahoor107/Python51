# Фінальний проєкт: Мікросервіс для аналізу творів мистецтва

Мікросервіс на **FastAPI** для демонстрації архітектури аналізу арт‑даних із використанням AI.  
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
CREATE USER myuser WITH PASSWORD 'your_password';
CREATE DATABASE artculture_db OWNER myuser;
3) Віртуальне середовище та залежності
macOS / Linux:
python3 -m venv .venv
source .venv/bin/activate
Windows:
python -m venv .venv
.venv\Scripts\activate
Встановіть залежності:
pip install -r requirements.txt
Створіть .env:
DATABASE_URL="postgresql://myuser:your_password@localhost:5432/artculture_db"
4) Запуск сервісу
uvicorn main:app --reload --reload-exclude .venv
http://127.0.0.1:8000
http://127.0.0.1:8000/docs

Приклад використання (ID = 9)
GET /art-terms — Try it out → Execute → знайти "id": 9

GET /ai/analyze-artwork/9 — Try it out → Execute → оригінальний і AI‑згенерований опис

Примітка про AI
Для демонстрації роботи сервісу я імітував відповідь від AI. Підключення реальної моделі: main.py → analyze_artwork.
Це дозволило сконцентруватися на архітектурі сервісу та його взаємодії з базою даних.
Архітектура та опис компонентів
Цей проєкт побудований за класичною трирівневою архітектурою, яка є стандартом для сучасних веб-сервісів.

Компоненти та їх взаємодія:
FastAPI (Рівень API):

Роль: Основний фреймворк, що створює веб-сервер та API-ендпоінти. Він приймає HTTP-запити ззовні (у нашому випадку, від Swagger UI) і повертає відповіді у форматі JSON.

Взаємодія: FastAPI керує всім процесом, викликаючи необхідні функції та валідуючи дані за допомогою Pydantic.

SQLAlchemy (Рівень доступу до даних):

Роль: Це "перекладач" між об'єктами Python та реляційною базою даних PostgreSQL. Завдяки SQLAlchemy, ми працюємо з Python-класами, а не пишемо сирі SQL-запити.

Взаємодія: FastAPI через сесію SQLAlchemy (db: Session) надсилає запити до бази даних для читання інформації.

PostgreSQL (Рівень даних):

Роль: Надійна реляційна база даних, де фізично зберігаються всі дані.

Взаємодія: Виконує SQL-запити, які для неї генерує SQLAlchemy, і повертає дані.

Uvicorn (Веб-сервер):

Роль: Високопродуктивний ASGI-сервер, який є "двигуном" для нашого FastAPI-застосунку. Він приймає вхідні з'єднання і передає їх на обробку в FastAPI.

Схема роботи запиту:
Коли Ви будете тестувати ендпоінт /ai/analyze-artwork/9:

Uvicorn приймає запит.

FastAPI отримує запит, валідує id=9 і викликає відповідну функцію.

Функція через SQLAlchemy робить запит до PostgreSQL.

PostgreSQL знаходить дані і повертає їх.

SQLAlchemy перетворює відповідь бази даних у Python-об'єкт.

Код імітує роботу AI, генеруючи новий опис.

FastAPI бере фінальний результат, перетворює його в JSON і віддає у відповідь.
