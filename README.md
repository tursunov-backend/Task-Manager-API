# ✅ Task Manager API

Vazifalar va loyihalarni boshqarish uchun ishlab chiqarishga tayyor REST API — **FastAPI**, **PostgreSQL** va **SQLAlchemy** asosida qurilgan.

---

## Mundarija

* [Imkoniyatlar](#imkoniyatlar)
* [Texnologiyalar](#texnologiyalar)
* [Loyiha tuzilmasi](#loyiha-tuzilmasi)
* [Boshlash](#boshlash)

  * [Talablar](#talablar)
  * [O'rnatish](#ornatish)
  * [Muhit o'zgaruvchilari](#muhit-ozgaruvchilari)
  * [Ilovani ishga tushirish](#ilovani-ishga-tushirish)
* [Ma'lumotlar bazasi](#malumotlar-bazasi)
* [API umumiy ko'rinishi](#api-umumiy-korinishi)
* [Ishlab chiqish](#ishlab-chiqish)
* [Eslatmalar](#eslatmalar)

---

## Imkoniyatlar

* **Loyihalar** va **Vazifalar** uchun to'liq CRUD amaliyoti
* **Foydalanuvchilar** va autentifikatsiya (JWT)
* Vazifalarni **holat bo'yicha boshqarish** (pending, in_progress, done)
* **Ustuvorlik darajasi** (low, medium, high)
* Pydantic v2 orqali avtomatik validatsiya
* Swagger UI va ReDoc avtomatik hujjatlar
* Toza arxitektura: models / schemas / crud / routers

---

## Texnologiyalar

| Qatlam             | Texnologiya       |
| ------------------ | ----------------- |
| Freymvork          | FastAPI           |
| Dasturlash tili    | Python 3.11+      |
| ORM                | SQLAlchemy 2.0    |
| Ma'lumotlar bazasi | PostgreSQL        |
| DB drayveri        | psycopg2          |
| Validatsiya        | Pydantic v2       |
| Auth               | JWT (python-jose) |
| Hash               | passlib (bcrypt)  |
| Server             | Uvicorn           |

---

## Loyiha tuzilmasi

```
task-manager-api/
├── app/
│   ├── main.py
│   ├── config.py
│   ├── database.py
│   ├── dependencies.py
│
│   ├── models/
│   │   ├── user.py
│   │   ├── project.py
│   │   └── task.py
│
│   ├── schemas/
│   │   ├── user.py
│   │   ├── project.py
│   │   └── task.py
│
│   ├── crud/
│   │   ├── user.py
│   │   ├── project.py
│   │   └── task.py
│
│   └── routers/
│       ├── auth.py
│       ├── users.py
│       ├── projects.py
│       └── tasks.py
```

---

## Boshlash

### Talablar

* Python 3.11+
* PostgreSQL 14+

---

### O'rnatish

```bash
git clone https://github.com/your-username/task-manager-api.git
cd task-manager-api

python -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
```

---

### Ilovani ishga tushirish

```bash
uvicorn app.main:app --reload
```

---

## Ma'lumotlar bazasi

Jadvallar avtomatik yaratiladi:

```python
Base.metadata.create_all(bind=engine)
```

---

### Sxema

```
users
  id
  username
  hashed_password
  is_active
  created_at

projects
  id
  title
  description
  author_id   FK → users.id
  created_at

tasks
  id
  title
  description
  status
  priority
  due_date
  project_id   FK → projects.id
  assignee_id  FK → users.id
  created_at
```

---

### Munosabatlar

* User → Project (1)
* Project → Task (1)
* User → Task (assigned)

---

## API umumiy ko'rinishi

| Method | Endpoint             |
| ------ | -------------------- |
| POST   | `/api/auth/register` |
| POST   | `/api/auth/login`    |
| GET    | `/api/users/me`      |
| PATCH  | `/api/users/me`      |
| GET    | `/api/projects/me`   |
| POST   | `/api/projects/`     |
| GET    | `/api/projects/{id}` |
| PATCH  | `/api/projects/{id}` |
| DELETE | `/api/projects/{id}` |
| GET    | `/api/tasks/`        |
| POST   | `/api/tasks/`        |
| GET    | `/api/tasks/{id}`    |
| PATCH  | `/api/tasks/{id}`    |
| DELETE | `/api/tasks/{id}`    |

---

## Ishlab chiqish

```bash
pip install black ruff

ruff check .
black .
```

---

## Eslatmalar

* Pagination: `skip`, `limit`
* PATCH → partial update
* Auth header:

```text
Authorization: Bearer <token>
```

* Task status: `pending`, `in_progress`, `done`
* Task priority: `low`, `medium`, `high`
* Project o‘chsa → tasklar ham o‘chadi (cascade)

---

## 👨‍💻 Muallif

**Abdujalol Tursunov**
