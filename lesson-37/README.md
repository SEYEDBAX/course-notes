### جزوه‌ای کامل در مورد انواع متدهای احراز هویت

احراز هویت (Authentication) فرآیندی است که در آن اعتبار کاربران بررسی می‌شود تا دسترسی به منابع یا سرویس‌ها امکان‌پذیر باشد. روش‌های مختلفی برای احراز هویت وجود دارد که هر یک دارای مزایا و معایب خود هستند.

#### انواع متدهای احراز هویت

1. **احراز هویت بر اساس رمز عبور (Password-based Authentication):**
   - این روش رایج‌ترین روش احراز هویت است. کاربر یک نام کاربری و رمز عبور وارد می‌کند که سرور آن را با اطلاعات ذخیره شده تطبیق می‌دهد. اگر مطابقت داشت، کاربر مجاز به دسترسی است.
   - مزایا: سادگی و گستردگی استفاده
   - معایب: آسیب‌پذیری در برابر حملات مانند brute-force و social engineering

2. **احراز هویت دو مرحله‌ای (Two-Factor Authentication یا 2FA):**
   - این روش علاوه بر رمز عبور، یک عامل دوم برای تایید هویت کاربر نیاز دارد. معمولاً این عامل دوم یک کد ارسال شده به تلفن همراه یا ایمیل است.
   - مزایا: امنیت بالاتر نسبت به روش‌های تک‌عاملی
   - معایب: نیاز به ابزار یا کد اضافی

3. **احراز هویت چندعاملی (Multi-Factor Authentication یا MFA):**
   - این روش شامل چندین عامل احراز هویت است که معمولاً شامل رمز عبور، کد تأیید و چیزی است که کاربر دارد (مانند توکن سخت‌افزاری).
   - مزایا: امنیت بسیار بالا
   - معایب: پیچیدگی و افزایش نیاز به منابع

4. **احراز هویت مبتنی بر توکن (Token-based Authentication):**
   - در این روش، پس از احراز هویت اولیه، به کاربر توکن داده می‌شود که در درخواست‌های بعدی به سرور ارائه می‌شود. این توکن‌ها معمولاً دارای زمان انقضا هستند.
   - **JWT** (JSON Web Token) یکی از روش‌های محبوب در احراز هویت مبتنی بر توکن است که در ادامه به طور مفصل‌تر توضیح داده خواهد شد.

5. **احراز هویت با استفاده از OAuth:**
   - OAuth یک پروتکل باز برای احراز هویت و مجوز دسترسی است که معمولاً برای مجوز دادن به برنامه‌ها برای دسترسی به منابع یک کاربر استفاده می‌شود (مثلاً دسترسی به اطلاعات از طریق حساب کاربری Google یا Facebook).

6. **احراز هویت زیستی (Biometric Authentication):**
   - در این روش، از ویژگی‌های زیستی کاربران مانند اثر انگشت، چهره یا عنبیه برای احراز هویت استفاده می‌شود.
   - مزایا: سختی در جعل و امنیت بالا
   - معایب: نیاز به تجهیزات خاص و احتمال خطا در تشخیص

---

### JSON Web Token (JWT)

**JWT** یک استاندارد باز برای تبادل امن اطلاعات به صورت توکن‌های متنی است که در قالب JSON کدگذاری می‌شوند. این روش به ویژه در برنامه‌های وب برای احراز هویت استفاده می‌شود.

#### ساختار JWT

یک توکن JWT از سه بخش اصلی تشکیل شده است:

1. **Header (سرآیند):**
   - شامل اطلاعات مربوط به نوع توکن و الگوریتم رمزنگاری است. مثلاً:
     ```json
     {
       "alg": "HS256",
       "typ": "JWT"
     }
     ```

2. **Payload (محتوا):**
   - شامل داده‌های کاربر یا کلایم‌هایی (claims) است که باید به سرور ارسال شود. مثلاً:
     ```json
     {
       "sub": "1234567890",
       "name": "John Doe",
       "admin": true
     }
     ```

3. **Signature (امضا):**
   - برای اطمینان از تغییرناپذیری محتوا، امضای دیجیتال بر روی header و payload اعمال می‌شود. این امضا با استفاده از کلید مخفی و الگوریتم رمزنگاری مشخص شده در header ایجاد می‌شود.

   امضا به شکل زیر تولید می‌شود:
   ```
   HMACSHA256(
     base64UrlEncode(header) + "." + base64UrlEncode(payload),
     secret
   )
   ```

#### فرآیند احراز هویت با JWT

1. **ورود کاربر:** کاربر اطلاعات ورود (مانند نام کاربری و رمز عبور) را به سرور ارسال می‌کند.
2. **تولید توکن JWT:** در صورت موفقیت‌آمیز بودن احراز هویت، سرور یک توکن JWT تولید کرده و به کاربر ارسال می‌کند.
3. **ذخیره توکن:** توکن JWT معمولاً در کلاینت (مرورگر یا موبایل) در مکان‌هایی مانند `localStorage` یا `sessionStorage` ذخیره می‌شود.
4. **استفاده از توکن:** در درخواست‌های بعدی، کاربر توکن JWT خود را به سرور ارسال می‌کند (معمولاً در قسمت `Authorization` هدر HTTP).
5. **بررسی توکن توسط سرور:** سرور امضای توکن JWT را بررسی می‌کند تا از تغییرناپذیری آن مطمئن شود و در صورت معتبر بودن، دسترسی لازم را به کاربر می‌دهد.

---

### مثال با کد پایتون برای JWT

ابتدا برای استفاده از JWT در پایتون، باید کتابخانه `PyJWT` را نصب کنیم:
```bash
pip install PyJWT
```

سپس کد زیر را برای ایجاد و تایید یک JWT می‌نویسیم:

```python
import jwt
import datetime

# کلید مخفی برای امضای توکن
SECRET_KEY = "my_secret_key"

# ایجاد JWT
def create_jwt():
    payload = {
        "sub": "1234567890",
        "name": "John Doe",
        "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=30)  # انقضای ۳۰ دقیقه
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    return token

# تایید JWT
def verify_jwt(token):
    try:
        decoded_token = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return decoded_token
    except jwt.ExpiredSignatureError:
        return "Signature has expired."
    except jwt.InvalidTokenError:
        return "Invalid token."

# استفاده از JWT
token = create_jwt()
print("Token:", token)

decoded_token = verify_jwt(token)
print("Decoded Token:", decoded_token)
```

---

### پیاده‌سازی JWT در FastAPI

برای پیاده‌سازی JWT در FastAPI، ابتدا نیاز به نصب کتابخانه‌های زیر داریم:

```bash
pip install fastapi
pip install uvicorn
pip install pyjwt
```

سپس کد زیر برای پیاده‌سازی JWT در FastAPI نوشته می‌شود:

```python
from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
import jwt
import datetime

app = FastAPI()

SECRET_KEY = "my_secret_key"
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# ایجاد JWT
def create_jwt(data: dict):
    payload = {
        **data,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    return token

# تایید JWT
def verify_jwt(token: str):
    try:
        decoded_token = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return decoded_token
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")

# روت احراز هویت
@app.post("/token")
def login():
    # به عنوان مثال یک توکن با نام کاربر تولید می‌شود
    token = create_jwt({"sub": "user1"})
    return {"access_token": token, "token_type": "bearer"}

# روت محافظت شده
@app.get("/protected")
def protected_route(token: str = Depends(oauth2_scheme)):
    decoded_token = verify_jwt(token)
    return {"message": "You are authenticated", "user": decoded_token["sub"]}

# برای اجرا از دستور زیر استفاده کنید:
# uvicorn myapp:app --reload
```

در این کد، از JWT برای محافظت از مسیر `/protected` استفاده شده است. زمانی که کاربر به `/token` مراجعه می‌کند، یک توکن JWT دریافت می‌کند و این توکن باید برای دسترسی به مسیر محافظت شده ارائه شود.