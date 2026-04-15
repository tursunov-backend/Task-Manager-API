# 🚀 Task Manager API

Zamonaviy va samarali **Task Manager REST API** — loyihalar va vazifalarni boshqarish uchun ishlab chiqilgan backend tizim.
**FastAPI + PostgreSQL + SQLAlchemy** asosida qurilgan.

---

## 📑 Mundarija

* [✨ Imkoniyatlar](#-imkoniyatlar)
* [🛠 Texnologiyalar](#-texnologiyalar)
* [📁 Loyiha tuzilmasi](#-loyiha-tuzilmasi)
* [🚀 Boshlash](#-boshlash)
* [🗄 Ma'lumotlar bazasi](#-malumotlar-bazasi)
* [🌐 API umumiy ko'rinishi](#-api-umumiy-korinishi)
* [⚠️ Eslatmalar](#️-eslatmalar)

---

## ✨ Imkoniyatlar

* 📁 Projects va 📝 Tasks uchun to‘liq CRUD
* 🔐 JWT asosida autentifikatsiya
* 📊 Task status boshqaruvi (`pending`, `in_progress`, `done`)
* 🎯 Priority tizimi (`low`, `medium`, `high`)
* 📄 Pagination (`skip`, `limit`)
* 🧱 Clean architecture (models / schemas / crud / routers)

---

## 🛠 Texnologiyalar

* ⚡ FastAPI
* 🐘 PostgreSQL
* 🧩 SQLAlchemy 2.0
* 📦 Pydantic v2
* 🔐 JWT (python-jose)
* 🔑 passlib (bcrypt)

---

## 📁 Loyiha tuzilmasi

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
├── .env.example
├── requirements.txt
└── README.md
```

---

## 🚀 Boshlash

```bash
uvicorn app.main:app --reload
```

---

## 🗄 Ma'lumotlar bazasi

### 📌 Sxema umumiy ko‘rinishi

```
users (foydalanuvchilar)
  id                INTEGER   PK
  username          VARCHAR(50)   UNIQUE
  hashed_password   VARCHAR(255)
  is_active         BOOLEAN   DEFAULT true
  created_at        TIMESTAMP

projects (loyihalar)
  id            INTEGER   PK
  title         VARCHAR(255)
  description   TEXT      (ixtiyoriy)
  author_id     INTEGER   FK → users.id  ON DELETE CASCADE
  created_at    TIMESTAMP

tasks (vazifalar)
  id            INTEGER   PK
  title         VARCHAR(255)
  description   TEXT      (ixtiyoriy)
  status        VARCHAR(20)   DEFAULT 'pending'
  priority      VARCHAR(10)   DEFAULT 'medium'
  due_date      DATE      (ixtiyoriy)
  project_id    INTEGER   FK → projects.id  ON DELETE CASCADE
  assignee_id   INTEGER   FK → users.id    (ixtiyoriy)
  created_at    TIMESTAMP
```

---

## 🌐 API umumiy ko‘rinishi

| Method | Endpoint             | Tavsif               |
| ------ | -------------------- | -------------------- |
| POST   | `/api/auth/register` | Ro'yxatdan o'tish    |
| POST   | `/api/auth/login`    | Login (token olish)  |
| GET    | `/api/users/me`      | Joriy user           |
| PATCH  | `/api/users/me`      | Profilni yangilash   |
| GET    | `/api/projects/me`   | Faqat o'z loyihalari |
| POST   | `/api/projects/`     | Loyiha yaratish      |
| GET    | `/api/projects/{id}` | Bitta loyiha         |
| PATCH  | `/api/projects/{id}` | Yangilash            |
| DELETE | `/api/projects/{id}` | O‘chirish            |
| GET    | `/api/tasks/`        | Tasklar ro‘yxati     |
| POST   | `/api/tasks/`        | Task yaratish        |
| GET    | `/api/tasks/{id}`    | Bitta task           |
| PATCH  | `/api/tasks/{id}`    | Yangilash            |
| DELETE | `/api/tasks/{id}`    | O‘chirish            |

---

## ⚠️ Eslatmalar

* 🔐 Authorization:

```
Authorization: Bearer <token>
```

* Status: `pending`, `in_progress`, `done`
* Priority: `low`, `medium`, `high`
* 🔁 Project o‘chirilganda → tasklar ham avtomatik o‘chadi (cascade)

---

## 👨‍💻 Muallif

**Abdujalol Tursunov** 🚀
