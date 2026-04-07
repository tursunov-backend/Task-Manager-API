# ✅ Task Manager API

Vazifalar va loyihalarni boshqarish uchun ishlab chiqarishga tayyor REST API — **FastAPI**, **PostgreSQL** va **SQLAlchemy** asosida qurilgan.

---

## Mundarija

- [Imkoniyatlar](#imkoniyatlar)
- [Texnologiyalar](#texnologiyalar)
- [Loyiha tuzilmasi](#loyiha-tuzilmasi)
- [Boshlash](#boshlash)
  - [Talablar](#talablar)
  - [O'rnatish](#ornatish)
  - [Muhit o'zgaruvchilari](#muhit-ozgaruvchilari)
  - [Ilovani ishga tushirish](#ilovani-ishga-tushirish)
- [Ma'lumotlar bazasi](#malumotlar-bazasi)
- [API umumiy ko'rinishi](#api-umumiy-korinishi)
- [Ishlab chiqish](#ishlab-chiqish)
- [Eslatmalar](#eslatmalar)

---

## Imkoniyatlar

- **Loyihalar** va **Vazifalar** uchun to'liq CRUD amaliyoti
- **Foydalanuvchilar** va autentifikatsiya (JWT)
- Vazifalarni **holat bo'yicha filtrlash** (bajarilmoqda, tugallangan, kutilmoqda)
- **Ustuvorlik darajasi** (past, o'rta, yuqori)
- Pydantic v2 orqali avtomatik so'rov/javob validatsiyasi
- Avtomatik interaktiv hujjatlar (Swagger UI va ReDoc)
- Toza kod arxitekturasi: models / schemas / crud / routers

---

## Texnologiyalar

| Qatlam | Texnologiya |
|---|---|
| Freymvork | FastAPI 0.111 |
| Dasturlash tili | Python 3.11+ |
| ORM | SQLAlchemy 2.0 |
| Ma'lumotlar bazasi | PostgreSQL |
| DB drayveri | psycopg2-binary |
| Validatsiya | Pydantic v2 |
| Autentifikatsiya | JWT (python-jose) |
| Sozlamalar | pydantic-settings |
| Server | Uvicorn |

---

## Loyiha tuzilmasi

```
task-manager-api/
├── app/
│   ├── main.py              # Ilova kirish nuqtasi, routerlarni ro'yxatdan o'tkazish
│   ├── config.py            # .env faylidan yuklangan sozlamalar
│   ├── database.py          # Engine, SessionLocal, Base
│   ├── dependencies.py      # Umumiy FastAPI dependency'lar (get_db, get_current_user)
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py          # Foydalanuvchi ORM modeli
│   │   ├── project.py       # Loyiha ORM modeli
│   │   └── task.py          # Vazifa ORM modeli
│   │
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── user.py          # UserCreate / UserUpdate / UserResponse
│   │   ├── project.py       # ProjectCreate / ProjectUpdate / ProjectResponse
│   │   └── task.py          # TaskCreate / TaskUpdate / TaskResponse
│   │
│   ├── crud/
│   │   ├── __init__.py
│   │   ├── user.py          # Foydalanuvchi DB amaliyotlari
│   │   ├── project.py       # Loyiha DB amaliyotlari
│   │   └── task.py          # Vazifa DB amaliyotlari
│   │
│   └── routers/
│       ├── __init__.py
│       ├── auth.py          # /auth endpointlari (login, register)
│       ├── users.py         # /users endpointlari
│       ├── projects.py      # /projects endpointlari
│       └── tasks.py         # /tasks endpointlari
│
├── .env.example
├── requirements.txt
└── README.md
```

---

## Boshlash

### Talablar

- Python 3.11+
- PostgreSQL 14+

### O'rnatish

```bash
# 1. Repozitoriyani klonlash
git clone https://github.com/foydalanuvchi/task-manager-api.git
cd task-manager-api

# 2. Virtual muhit yaratish va faollashtirish
python -m venv venv
source venv/bin/activate        # Linux / macOS
venv\Scripts\activate           # Windows

# 3. Kerakli paketlarni o'rnatish
pip install -r requirements.txt
```

### Muhit o'zgaruvchilari

Namuna faylni nusxalab, o'z qiymatlaringizni kiriting:

```bash
cp .env.example .env
```

| O'zgaruvchi | Tavsif | Standart qiymat |
|---|---|---|
| `DATABASE_URL` | PostgreSQL ulanish manzili | `postgresql://postgres:password@localhost:5432/taskdb` |
| `SECRET_KEY` | JWT token uchun maxfiy kalit | — |
| `ACCESS_TOKEN_EXPIRE_MINUTES` | Token amal qilish muddati | `30` |

**`.env` fayli namunasi:**
```env
DATABASE_URL=postgresql://postgres:sizningparolingiz@localhost:5432/taskdb
SECRET_KEY=juda_maxfiy_kalit
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### Ilovani ishga tushirish

```bash
# Ishlab chiqish rejimi (avtomatik qayta yuklash bilan)
uvicorn app.main:app --reload

# Maxsus host/port bilan
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

Ilova quyidagi manzillarda mavjud bo'ladi:

| Interfeys | URL |
|---|---|
| API asosi | http://localhost:8000 |
| Swagger UI | http://localhost:8000/docs |
| ReDoc | http://localhost:8000/redoc |
| Holat tekshiruvi | http://localhost:8000/ |

---

## Ma'lumotlar bazasi

Jadvallar ishga tushirishda avtomatik ravishda yaratiladi:

```python
Base.metadata.create_all(bind=engine)
```

### Sxema umumiy ko'rinishi

```
users (foydalanuvchilar)
  id                INTEGER   PK
  username          VARCHAR(50)   UNIQUE
  email             VARCHAR(100)  UNIQUE
  hashed_password   VARCHAR(255)
  is_active         BOOLEAN   DEFAULT true
  created_at        TIMESTAMP

projects (loyihalar)
  id            INTEGER   PK
  title         VARCHAR(255)
  description   TEXT      (ixtiyoriy)
  owner_id      INTEGER   FK → users.id  ON DELETE CASCADE
  created_at    TIMESTAMP

tasks (vazifalar)
  id            INTEGER   PK
  title         VARCHAR(255)
  description   TEXT      (ixtiyoriy)
  status        VARCHAR(20)   DEFAULT 'pending'   -- pending / in_progress / done
  priority      VARCHAR(10)   DEFAULT 'medium'    -- low / medium / high
  due_date      DATE      (ixtiyoriy)
  project_id    INTEGER   FK → projects.id  ON DELETE CASCADE
  assignee_id   INTEGER   FK → users.id    (ixtiyoriy)
  created_at    TIMESTAMP
```

### Munosabatlar

- `Foydalanuvchi` → `Loyiha` : bir-ko'pga (bir foydalanuvchining ko'p loyihasi bor)
- `Loyiha` → `Vazifa` : bir-ko'pga (bir loyihada ko'p vazifa bor)
- Loyihani o'chirish undagi barcha vazifalarni kaskad tarzda o'chiradi

---

## API umumiy ko'rinishi

| Metod | Endpoint | Tavsif |
|--------|----------|--------|
| POST | `/auth/register` | Ro'yxatdan o'tish |
| POST | `/auth/login` | Tizimga kirish (token olish) |
| GET | `/users/me` | Joriy foydalanuvchi ma'lumotlari |
| PATCH | `/users/me` | Profilni yangilash |
| GET | `/projects/` | Loyihalar ro'yxati (qidiruv, sahifalash) |
| POST | `/projects/` | Loyiha yaratish |
| GET | `/projects/{id}` | ID bo'yicha loyiha olish |
| PATCH | `/projects/{id}` | Loyihani yangilash |
| DELETE | `/projects/{id}` | Loyihani o'chirish |
| GET | `/projects/{id}/tasks` | Loyihadagi barcha vazifalar |
| GET | `/tasks/` | Vazifalar ro'yxati (filtrlash, sahifalash) |
| POST | `/tasks/` | Vazifa yaratish |
| GET | `/tasks/{id}` | ID bo'yicha vazifa olish |
| PATCH | `/tasks/{id}` | Vazifani yangilash |
| DELETE | `/tasks/{id}` | Vazifani o'chirish |

To'liq so'rov/javob tafsilotlari uchun [API_DOCS.md](./API_DOCS.md) ga qarang.

---

## Ishlab chiqish

### Kod uslubi

Loyiha standart Python konventsiyalariga amal qiladi. Tavsiya etilgan vositalar:

```bash
pip install ruff black

ruff check .      # linting (xatolarni tekshirish)
black .           # formatlash
```

### Yangi resurs qo'shish

1. `app/models/` ichiga ORM modeli qo'shish
2. Uni `app/models/__init__.py` ga ro'yxatdan o'tkazish
3. `app/schemas/` ichiga Pydantic sxemalari qo'shish
4. `app/crud/` ichiga CRUD funksiyalari qo'shish
5. `app/routers/` ichiga router qo'shish
6. Routerni `app/main.py` da ro'yxatdan o'tkazish

---

## Eslatmalar

- Barcha ro'yxat endpointlari `skip` va `limit` parametrlarini qo'llab-quvvatlaydi (`limit` maksimumi: 100)
- `PATCH` endpointlari qisman yangilashni amalga oshiradi — faqat ko'rsatilgan maydonlar o'zgartiriladi
- Himoyalangan endpointlarga kirish uchun `Authorization: Bearer <token>` sarlavhasi talab qilinadi
- Vazifa holatlari: `pending` (kutilmoqda), `in_progress` (bajarilmoqda), `done` (tugallangan)
- Vazifa ustuvorliklari: `low` (past), `medium` (o'rta), `high` (yuqori)
- Loyihani o'chirish undagi barcha vazifalarni kaskad tarzda o'chiradi
