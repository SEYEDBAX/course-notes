برای درک کامل فرآیند درخواست (Request) در یک اپلیکیشن FastAPI، نیاز است که کل مسیر را از لحظه‌ای که یک درخواست توسط کلاینت (مانند مرورگر یا یک کلاینت HTTP) ایجاد می‌شود تا زمانی که این درخواست توسط سرور پردازش شده و پاسخی به کلاینت ارسال می‌شود، بررسی کنیم. این فرآیند شامل مراحل مختلفی است که در ادامه به تفصیل شرح داده شده است:

### ۱. ارسال درخواست توسط کلاینت
وقتی یک کاربر (کلاینت) تصمیم می‌گیرد به سروری درخواست ارسال کند، معمولاً از طریق یک مرورگر یا یک کلاینت HTTP مانند `curl` یا `Postman`، یک درخواست HTTP (مانند GET، POST، PUT، DELETE) ایجاد می‌کند. این درخواست حاوی اطلاعات زیر است:

- **URL:**
 آدرس سروری که درخواست به آن ارسال می‌شود. به عنوان مثال: 
 `http://example.com/api/v1/users`
- **HTTP Method:**
 نوع عملیاتی که قرار است انجام شود، مانند GET، POST، PUT، DELETE.
- **Headers:**
 مجموعه‌ای از کلید-مقدارهایی که اطلاعات اضافی درباره درخواست ارائه می‌دهند، مانند 
 `Content-Type`, `Authorization`, `User-Agent`.
- **Query Parameters:**
پارامترهایی که به صورت کلید-مقدار در URL ارسال می‌شوند. به عنوان مثال:
 `http://example.com/api/v1/users?id=123`
- **Body:**
 (درخواست‌های POST و PUT) حاوی داده‌هایی است که قرار است به سرور ارسال شود، مانند JSON, XML یا فرم داده‌ها.

#### مثال
فرض کنید کلاینت یک درخواست GET به آدرس زیر ارسال می‌کند:
```
GET /api/v1/users?id=123 HTTP/1.1
Host: example.com
User-Agent: Mozilla/5.0
Accept: application/json
```

### ۲. دریافت درخواست توسط وب سرور
وب سرور (مانند Nginx یا Apache) اولین موجودیتی است که این درخواست را دریافت می‌کند. وظیفه وب سرور این است که درخواست را به سرور برنامه‌نویسی (مثلاً Uvicorn در مورد FastAPI) که وظیفه اجرای منطق برنامه را دارد، ارسال کند.

- **وب سرور** می‌تواند برای مسیریابی درخواست‌ها، کش کردن محتوا، لود بالانسینگ و اعمال SSL/TLS استفاده شود.

### ۳. پردازش درخواست توسط سرور ASGI (مثل Uvicorn)
Uvicorn یک سرور ASGI است که برای اجرای برنامه‌های FastAPI استفاده می‌شود. ASGI (Asynchronous Server Gateway Interface) پروتکلی است که برای تعامل بین وب سرور و اپلیکیشن‌های پایتونی مدرن طراحی شده است.

وقتی Uvicorn درخواست را دریافت می‌کند:
1. درخواست را به یک شیء `ASGI Scope` تبدیل می‌کند. این شیء حاوی اطلاعاتی مانند مسیر، روش HTTP، هدرها، آدرس IP کلاینت، و موارد دیگر است.
2. درخواست را به اپلیکیشن FastAPI ارسال می‌کند.

### ۴. رسیدن درخواست به اپلیکیشن FastAPI
FastAPI درخواست را از طریق ASGI دریافت می‌کند و به کمک `Request Object` آن را مدیریت می‌کند. FastAPI درخواست را به روش زیر پردازش می‌کند:

1. **مسیریابی (Routing):** FastAPI با استفاده از مسیرها (routes) و پارامترهای مسیر، بررسی می‌کند که کدام تابع (endpoint) باید این درخواست را مدیریت کند. 
   
   اگر هیچ مسیری با درخواست مطابقت نداشته باشد، FastAPI خطای ۴۰۴ (Not Found) را بازمی‌گرداند.

2. **وابستگی‌ها (Dependencies):** قبل از اجرای endpoint، FastAPI وابستگی‌های مربوطه را که با `Depends` تعریف شده‌اند، حل می‌کند. این وابستگی‌ها می‌توانند شامل احراز هویت، بررسی‌های دسترسی، و موارد دیگر باشند.
   
   اگر در این مرحله خطایی رخ دهد (مانند عدم احراز هویت)، FastAPI خطای مناسبی (مثلاً ۴۰۱ Unauthorized) را بازمی‌گرداند.

3. **اجرای فانکشن:** اگر مسیر و وابستگی‌ها به درستی تشخیص داده شوند، FastAPI تابع مربوطه را اجرا می‌کند و داده‌های ورودی (مانند پارامترهای مسیر، کوئری، و بدنه درخواست) را به عنوان آرگومان‌های تابع ارسال می‌کند.

### ۵. ایجاد پاسخ (Response) و ارسال به کلاینت
پس از اجرای تابع، FastAPI یک `Response Object` ایجاد می‌کند که حاوی اطلاعات زیر است:
- **Status Code:**
 کد وضعیت HTTP که نشان‌دهنده موفقیت یا شکست درخواست است (مثلاً ۲۰۰ برای موفقیت یا ۴۰۰ برای خطای کاربر).
- **Headers:**
 هدرهای HTTP که ممکن است در پاسخ به کلاینت ارسال شوند.
- **Body:**
 محتوای پاسخ که می‌تواند JSON، HTML یا هر فرمت دیگری باشد.

#### مثال
اگر فانکشنی که توسط FastAPI فراخوانی شده، لیستی از کاربران را بازگرداند، پاسخ ممکن است به صورت زیر باشد:
```json
{
    "users": [
        {"id": 123, "name": "John Doe"},
        {"id": 124, "name": "Jane Doe"}
    ]
}
```
این پاسخ همراه با هدرها و کد وضعیت ۲۰۰ به Uvicorn ارسال می‌شود.

### ۶. ارسال پاسخ به وب سرور و کلاینت
Uvicorn پاسخ ایجاد شده توسط FastAPI را دریافت می‌کند و آن را به وب سرور (مثلاً Nginx) ارسال می‌کند. سپس وب سرور این پاسخ را به کلاینت ارسال می‌کند.

### ۷. دریافت پاسخ توسط کلاینت
کلاینت پس از دریافت پاسخ، محتوای آن را پردازش می‌کند و نتیجه را به کاربر نمایش می‌دهد. اگر پاسخ شامل خطا باشد (مانند ۴۰۴ یا ۵۰۰)، کلاینت می‌تواند این خطا را به شیوه‌ای مناسب مدیریت کند (مثلاً نمایش پیام خطا به کاربر).

### ۸. مدیریت خطاها
اگر در هر یک از مراحل فوق خطایی رخ دهد، FastAPI آن را مدیریت می‌کند. این خطاها می‌توانند شامل موارد زیر باشند:
- **۴۰۴ Not Found:**
 اگر مسیریابی موفقیت‌آمیز نباشد.
- **۴۰۰ Bad Request:**
 اگر داده‌های ورودی نامعتبر باشند.
- **۵۰۰ Internal Server Error:**
 اگر خطایی در اجرای منطق برنامه رخ دهد.

FastAPI به‌طور خودکار خطاهای مناسب را ایجاد کرده و به همراه پیام‌های مربوطه به کلاینت بازمی‌گرداند.

### **جمع‌بندی**
فرآیند درخواست HTTP در FastAPI شامل چندین مرحله است که هر کدام نقش مهمی در مدیریت و پاسخ‌دهی به درخواست‌ها دارند. از لحظه‌ای که درخواست توسط کلاینت ارسال می‌شود تا زمانی که سرور پاسخ می‌دهد، چندین گام از جمله مسیریابی، مدیریت وابستگی‌ها، و ایجاد پاسخ مناسب انجام می‌شود. FastAPI با استفاده از قابلیت‌های ASGI و Pydantic این فرآیندها را به صورت بهینه و قابل اعتماد انجام می‌دهد.