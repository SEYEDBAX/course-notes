### آموزش SQLAlchemy برای مبتدیان (پایگاه داده PostgreSQL)

SQLAlchemy یک کتابخانه‌ی قدرتمند برای کار با پایگاه داده‌ها در پایتون است. اگر شما تازه با SQL آشنا شده‌اید و سینتکس پایه‌ی آن را یاد گرفته‌اید، این جزوه به شما کمک می‌کند تا با SQLAlchemy شروع کنید و از آن برای ارتباط با پایگاه داده PostgreSQL استفاده کنید.

#### 1. نصب SQLAlchemy و PostgreSQL Driver

ابتدا باید SQLAlchemy و PostgreSQL Driver را نصب کنید. برای نصب، دستور زیر را در ترمینال وارد کنید:

```bash
pip install sqlalchemy psycopg2
```

`psycopg2` یک درایور برای ارتباط پایتون با PostgreSQL است.

#### 2. ساختار اولیه SQLAlchemy

SQLAlchemy شامل دو بخش اصلی است:

- **Core**: این بخش به شما امکان استفاده از دستورات SQL به صورت مستقیم را می‌دهد.
- **ORM (Object Relational Mapper)**: به شما این امکان را می‌دهد که داده‌های پایگاه داده را به عنوان اشیاء پایتون مدیریت کنید.

در این جزوه، بیشتر بر روی ORM تمرکز می‌کنیم.

#### 3. اتصال به پایگاه داده

ابتدا باید به پایگاه داده‌ی PostgreSQL خود متصل شوید. فرض کنیم پایگاه داده‌ی شما `mydatabase` نام دارد.

```python
from sqlalchemy import create_engine

# ساخت Engine برای اتصال به پایگاه داده
engine = create_engine('postgresql+psycopg2://username:password@localhost/mydatabase')
```

در اینجا باید `username` و `password` خود را به جای مقادیر مربوطه قرار دهید.

#### 4. ساخت یک مدل ساده

ORM به شما امکان می‌دهد تا یک جدول در پایگاه داده را به یک کلاس پایتون نگاشت کنید. بیایید یک جدول برای کاربران بسازیم.

```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# تعریف مدل User
class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

# ساخت جداول در پایگاه داده
Base.metadata.create_all(engine)
```

در اینجا ما یک مدل به نام `User` ایجاد کردیم که نمایانگر جدول `users` در پایگاه داده است.

#### 5. ایجاد یک نشست (Session)

برای تعامل با پایگاه داده، نیاز به یک نشست داریم.

```python
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()
```

#### 6. افزودن داده‌ها به پایگاه داده

برای افزودن رکورد جدید به جدول `users` می‌توانید از کد زیر استفاده کنید:

```python
new_user = User(name='John Doe', age=30)
session.add(new_user)
session.commit()
```

در اینجا یک کاربر جدید با نام "John Doe" و سن ۳۰ به جدول اضافه می‌شود.

#### 7. خواندن داده‌ها از پایگاه داده

برای خواندن داده‌ها از پایگاه داده، می‌توانید از دستورات زیر استفاده کنید:

```python
users = session.query(User).all()
for user in users:
    print(user.name, user.age)
```

این کد تمام کاربران موجود در جدول را بازیابی و چاپ می‌کند.

#### 8. به‌روزرسانی داده‌ها

برای به‌روزرسانی یک رکورد، باید آن را پیدا کرده و مقدار آن را تغییر دهید:

```python
user_to_update = session.query(User).filter_by(name='John Doe').first()
user_to_update.age = 31
session.commit()
```

در اینجا، سن کاربر "John Doe" به ۳۱ تغییر می‌کند.

#### 9. حذف داده‌ها

برای حذف یک رکورد از جدول:

```python
user_to_delete = session.query(User).filter_by(name='John Doe').first()
session.delete(user_to_delete)
session.commit()
```

این کد کاربر "John Doe" را از جدول حذف می‌کند.

#### 10. پایان نشست

در نهایت، پس از اتمام کار با پایگاه داده، نشست را باید ببندید:

```python
session.close()
```


### 11. فیلتر کردن داده‌ها

SQLAlchemy ابزارهای متنوعی برای فیلتر کردن و جستجوی داده‌ها در اختیار شما قرار می‌دهد. به عنوان مثال، می‌توانید از دستور `filter()` برای پیدا کردن کاربران بر اساس شرایط خاص استفاده کنید.

#### مثال: فیلتر کردن کاربران بر اساس سن

```python
young_users = session.query(User).filter(User.age < 30).all()
for user in young_users:
    print(user.name, user.age)
```

در این مثال، کاربرانی که سن آن‌ها کمتر از ۳۰ است فیلتر و چاپ می‌شوند.

#### مثال: جستجو با استفاده از فیلترهای چندگانه

می‌توانید چندین فیلتر را به صورت همزمان اعمال کنید:

```python
filtered_users = session.query(User).filter(User.age > 25, User.name.like('%John%')).all()
for user in filtered_users:
    print(user.name, user.age)
```

این کد کاربرانی که سن آن‌ها بیشتر از ۲۵ و نامشان شامل "John" است را پیدا می‌کند.

### 12. مرتب‌سازی داده‌ها

SQLAlchemy به شما امکان می‌دهد تا داده‌ها را بر اساس فیلدهای مختلف مرتب کنید.

#### مثال: مرتب‌سازی کاربران بر اساس سن

```python
sorted_users = session.query(User).order_by(User.age).all()
for user in sorted_users:
    print(user.name, user.age)
```

در اینجا کاربران بر اساس سن مرتب می‌شوند.

### 13. رابطه‌ها (Relationships)

یکی از قابلیت‌های قدرتمند ORM در SQLAlchemy، ایجاد روابط بین جداول مختلف است. فرض کنید می‌خواهید یک جدول جدید برای سفارشات (`orders`) بسازید که با کاربران (`users`) مرتبط باشد.

#### تعریف مدل Order

```python
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
    description = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship("User", back_populates="orders")
```

در اینجا یک جدول `orders` ایجاد کردیم که یک رابطه‌ی `ForeignKey` با `users` دارد.

#### اضافه کردن رابطه به مدل User

حالا باید رابطه‌ی معکوس را در مدل `User` تعریف کنیم:

```python
User.orders = relationship("Order", back_populates="user")
```

این کد مشخص می‌کند که هر کاربر می‌تواند چندین سفارش داشته باشد.

#### اضافه کردن سفارش به یک کاربر

برای اضافه کردن یک سفارش به کاربر، می‌توانید از رابطه‌ی تعریف شده استفاده کنید:

```python
new_order = Order(description="Laptop", user=new_user)
session.add(new_order)
session.commit()
```

### 14. انجام تراکنش‌های پیچیده

SQLAlchemy به صورت پیش‌فرض عملیات‌ها را در تراکنش‌ها انجام می‌دهد. با این حال، شما می‌توانید تراکنش‌ها را به صورت دستی مدیریت کنید تا مطمئن شوید که عملیات‌ها به درستی انجام می‌شوند.

#### استفاده از تراکنش‌ها

```python
try:
    new_user = User(name='Alice', age=25)
    session.add(new_user)
    
    new_order = Order(description="Phone", user=new_user)
    session.add(new_order)
    
    session.commit()  # همه تغییرات با هم ثبت می‌شوند
except:
    session.rollback()  # در صورت بروز خطا، همه تغییرات لغو می‌شوند
    raise
```

در اینجا اگر خطایی در حین افزودن داده‌ها رخ دهد، تمام تغییرات قبلی لغو خواهند شد.

### 15. بهینه‌سازی کوئری‌ها با Join

برای بهینه‌سازی کوئری‌ها و ارتباط بین جداول مختلف می‌توانید از `join` استفاده کنید. به عنوان مثال، فرض کنید می‌خواهید اطلاعات کاربران و سفارشات آن‌ها را با هم بازیابی کنید.

#### استفاده از Join برای کوئری‌ها

```python
users_with_orders = session.query(User).join(Order).all()
for user in users_with_orders:
    print(user.name, user.orders)
```

این کد اطلاعات کاربران را همراه با سفارشات مرتبط آن‌ها برمی‌گرداند.

### 16. شمارش تعداد رکوردها

SQLAlchemy ابزارهایی برای شمارش رکوردها در اختیار شما قرار می‌دهد. برای مثال، می‌توانید تعداد کاربران را به راحتی شمارش کنید.

#### مثال: شمارش تعداد کاربران

```python
user_count = session.query(User).count()
print(f"Number of users: {user_count}")
```

### 17. استفاده از توابع تجمعی (Aggregations)

SQLAlchemy همچنین از توابع تجمعی مثل `sum()`، `avg()`، `max()` و `min()` پشتیبانی می‌کند.

#### مثال: محاسبه‌ی میانگین سن کاربران

```python
from sqlalchemy import func

average_age = session.query(func.avg(User.age)).scalar()
print(f"Average age: {average_age}")
```

### 18. مدیریت لاگ‌ها (Logging)

برای مشاهده و بررسی کوئری‌هایی که SQLAlchemy به پایگاه داده ارسال می‌کند، می‌توانید لاگ‌ها را فعال کنید.

#### فعال کردن لاگ SQLAlchemy

```python
import logging

logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)
```

این کد تمام کوئری‌های SQL را که به پایگاه داده ارسال می‌شوند، در کنسول چاپ می‌کند.

### 19. پیکربندی SQLAlchemy با فایل تنظیمات

در پروژه‌های بزرگ، معمولاً اطلاعات اتصال به پایگاه داده و تنظیمات SQLAlchemy را در یک فایل تنظیمات جداگانه قرار می‌دهند. این کار به منظور جداسازی منطق برنامه از پیکربندی و تسهیل مدیریت پروژه انجام می‌شود.

#### ایجاد یک فایل تنظیمات

می‌توانید اطلاعات اتصال و تنظیمات دیگر را در یک فایل `config.py` قرار دهید:

```python
# config.py
DATABASE_URL = 'postgresql+psycopg2://username:password@localhost/mydatabase'
```

سپس در کد اصلی پروژه، این فایل را وارد کنید:

```python
# main.py
from sqlalchemy import create_engine
from config import DATABASE_URL

engine = create_engine(DATABASE_URL)
```

این روش اجازه می‌دهد که به راحتی تنظیمات پایگاه داده را در یک مکان مدیریت کنید.

### 20. استفاده از Migrations برای تغییرات پایگاه داده

با گذشت زمان، ممکن است نیاز داشته باشید که ساختار پایگاه داده را تغییر دهید (مثلاً اضافه کردن ستون جدید یا تغییر نام یک جدول). برای این کار از ابزارهایی مانند **Alembic** که یک ابزار مدیریت Migration برای SQLAlchemy است، استفاده می‌شود.

#### نصب Alembic

برای استفاده از Alembic، ابتدا باید آن را نصب کنید:

```bash
pip install alembic
```

#### راه‌اندازی Alembic

پس از نصب، دستور زیر را برای راه‌اندازی Alembic در پروژه اجرا کنید:

```bash
alembic init alembic
```

این دستور پوشه‌ای به نام `alembic` ایجاد می‌کند که شامل تنظیمات مورد نیاز برای اجرای Migration است.

#### تنظیمات Alembic

در فایل `alembic.ini`، رشته اتصال به پایگاه داده را تنظیم کنید:

```ini
# در فایل alembic.ini
sqlalchemy.url = postgresql+psycopg2://username:password@localhost/mydatabase
```

#### ایجاد یک Migration

برای ایجاد یک Migration جدید (مثلاً افزودن ستون جدید به جدول)، دستور زیر را اجرا کنید:

```bash
alembic revision --autogenerate -m "Add new column to users"
```

این دستور یک فایل Migration ایجاد می‌کند که تغییرات را ذخیره می‌کند.

#### اجرای Migration

پس از ایجاد فایل Migration، می‌توانید تغییرات را در پایگاه داده اعمال کنید:

```bash
alembic upgrade head
```

این دستور تغییرات تعریف شده در Migration را به پایگاه داده اعمال می‌کند.

### 21. مدیریت ارتباطات پیچیده بین جداول (Many-to-Many)

گاهی اوقات نیاز به تعریف ارتباط چند به چند (Many-to-Many) بین جداول دارید. برای مثال، فرض کنید هر کاربر می‌تواند چندین کتاب داشته باشد و هر کتاب هم می‌تواند توسط چندین کاربر خوانده شود.

#### ایجاد یک جدول میانی برای رابطه چند به چند

برای ایجاد یک رابطه چند به چند، نیاز به یک جدول میانی دارید:

```python
from sqlalchemy import Table, ForeignKey

# جدول میانی بین User و Book
user_books = Table('user_books', Base.metadata,
    Column('user_id', ForeignKey('users.id'), primary_key=True),
    Column('book_id', ForeignKey('books.id'), primary_key=True)
)

class Book(Base):
    __tablename__ = 'books'
    
    id = Column(Integer, primary_key=True)
    title = Column(String)

    users = relationship("User", secondary=user_books, back_populates="books")

User.books = relationship("Book", secondary=user_books, back_populates="users")
```

این کد یک رابطه چند به چند بین کاربران و کتاب‌ها تعریف می‌کند.

#### افزودن داده‌ها به رابطه چند به چند

برای افزودن داده به این رابطه، می‌توانید به سادگی لیست اشیاء را به کاربر یا کتاب اختصاص دهید:

```python
new_book = Book(title="Python 101")
new_user.books.append(new_book)
session.commit()
```

این کد یک کتاب جدید به لیست کتاب‌های کاربر اضافه می‌کند.

### 22. مدل‌های پیچیده‌تر و Inheritance

SQLAlchemy همچنین از وراثت (Inheritance) بین مدل‌ها پشتیبانی می‌کند. این ویژگی زمانی مفید است که بخواهید چندین کلاس با رفتارهای مشترک را از یک مدل پایه به ارث ببرید.

#### ایجاد مدل با استفاده از وراثت

```python
class Employee(Base):
    __tablename__ = 'employees'

    id = Column(Integer, primary_key=True)
    name = Column(String)

class Manager(Employee):
    __tablename__ = 'managers'
    
    id = Column(Integer, ForeignKey('employees.id'), primary_key=True)
    department = Column(String)
```

در اینجا `Manager` از `Employee` به ارث می‌برد و ویژگی‌های جدیدی مانند `department` اضافه می‌کند. این ویژگی به شما امکان می‌دهد تا ساختارهای داده پیچیده‌تری را مدیریت کنید.

### 23. کار با معاملات بزرگ و Batch Processing

گاهی اوقات نیاز به اجرای معاملات بزرگ دارید که شامل تعداد زیادی رکورد است. SQLAlchemy ابزارهایی برای مدیریت این نوع پردازش‌ها به صورت بهینه ارائه می‌دهد.

#### افزودن دسته‌ای داده‌ها (Bulk Insert)

برای افزودن تعداد زیادی رکورد به صورت دسته‌ای (بدون اینکه هر رکورد به صورت جداگانه commit شود):

```python
session.bulk_save_objects([
    User(name='User1', age=22),
    User(name='User2', age=25),
    User(name='User3', age=30),
])
session.commit()
```

این روش باعث می‌شود که پردازش سریع‌تر انجام شود زیرا هر رکورد به صورت جداگانه commit نمی‌شود.

### 24. ارتباط با سایر پایگاه‌های داده

SQLAlchemy از پایگاه‌های داده مختلفی مانند MySQL، SQLite و Oracle پشتیبانی می‌کند. برای تغییر پایگاه داده، فقط باید درایور و رشته اتصال (Connection String) مربوطه را تنظیم کنید.

#### مثال: اتصال به پایگاه داده MySQL

```python
engine = create_engine('mysql+pymysql://username:password@localhost/mydatabase')
```

با این کار می‌توانید پروژه خود را به راحتی به پایگاه داده دیگری انتقال دهید بدون نیاز به تغییرات بزرگ در کد.

### 25. مزایا و چالش‌های استفاده از SQLAlchemy

#### مزایا:

- **مستقل از پایگاه داده**: می‌توانید به راحتی بین پایگاه‌های داده مختلف جا‌به‌جا شوید.
- **کدنویسی کمتر**: بسیاری از عملیات‌های پیچیده پایگاه داده را می‌توان با نوشتن کدهای کمتر انجام داد.
- **پشتیبانی از ORM و Core**: انعطاف‌پذیری در استفاده از ORM یا SQL خام به شما این امکان را می‌دهد که از هر دو جهان بهترین بهره را ببرید.

#### چالش‌ها:

- **پیچیدگی در کوئری‌های بزرگ**: در پروژه‌های پیچیده، کوئری‌های SQLAlchemy ممکن است نسبت به کوئری‌های دستی SQL پیچیده‌تر شوند.
- **عملکرد**: در برخی موارد، استفاده از ORM می‌تواند به کاهش سرعت کوئری‌ها منجر شود، مخصوصاً زمانی که از بسیاری از روابط پیچیده استفاده می‌کنید.

---

این مطالب تکمیلی به شما کمک می‌کند که درک عمیق‌تری از SQLAlchemy پیدا کنید و پروژه‌های پیچیده‌تری را با این ابزار مدیریت کنید.