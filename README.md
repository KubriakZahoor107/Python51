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
