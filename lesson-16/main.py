from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from datetime import datetime


app = FastAPI(
    title="FastAPI Demo",
    description="A sample API built with FastAPI",
    version="1.0.0",
    docs_url="/api/docs",
    redoc_url=None,
)

@app.get("/")
async def root():
    """
    Returns a welcome message.
    """
    return {"message": "Welcome to the FastAPI Demo API!"}

@app.get("/calculate/{num1}/{num2}")
async def calculate(num1: int, num2: int):
    """
    Calculates the sum, difference, product, and quotient of two numbers.
    """
    sum_result = num1 + num2
    difference_result = num1 - num2
    product_result = num1 * num2
    quotient_result = num1 / num2 if num2 != 0 else "undefined"
    return {"sum": sum_result, "difference": difference_result, "product": product_result, "quotient": quotient_result}

@app.get("/time-info")
async def time_info():
    """
    Returns information about the current UTC time.
    """
    now = datetime.utcnow()
    return {
        "year": now.year,
        "month": now.month,
        "day": now.day,
        "hour": now.hour,
        "minute": now.minute,
        "second": now.second,
    }

@app.get("/status/{status_code}")
async def custom_status(status_code: int):
    """
    Returns a custom status response with the specified status code.
    """
    message = f"Custom status response with status code: {status_code}"
    return JSONResponse(status_code=status_code, content={"message": message, "code": status_code})

@app.get("/double/{number}")
async def double(number: int):
    """
    Returns the double of the input number.
    """
    double_result = number * 2
    return {"result": double_result}

@app.get("/reverse/{text}")
async def reverse(text: str):
    """
    Reverses the input text.
    """
    reversed_text = text[::-1]
    return {"reversed": reversed_text}

@app.get("/uppercase/{text}")
async def uppercase(text: str):
    """
    Returns the uppercase version of the input text.
    """
    uppercase_text = text.upper()
    return {"uppercase": uppercase_text}

@app.get("/sample-response")
async def sample_response():
    return {"message": "This is a sample response"}

@app.get("/show-time")
async def show_time():
    return {"current_time": datetime.utcnow().isoformat()}

@app.get("/show-user-agent")
async def show_user_agent(request: Request):
    user_agent = request.headers.get('user-agent')
    return {"user_agent": user_agent}

@app.get("/show-headers")
async def show_headers(request: Request):
    headers = dict(request.headers)
    return {"headers": headers}

@app.get("/method-get")
async def method_get():
    return {"method": "GET"}

@app.post("/method-post")
async def method_post():
    return {"method": "POST"}

@app.put("/method-put")
async def method_put():
    return {"method": "PUT"}

@app.delete("/method-delete")
async def method_delete():
    return {"method": "DELETE"}

@app.patch("/method-patch")
async def method_patch():
    return {"method": "PATCH"}

@app.options("/method-options")
async def method_options():
    return {"method": "OPTIONS"}

@app.head("/method-head")
async def method_head():
    return {"method": "HEAD"}

@app.trace("/method-trace")
async def method_trace():
    return {"method": "TRACE"}

@app.get("/greet/{name}")
async def greet(name: str):
    return {"message": f"Hello, {name}!"}

@app.get("/calculate/{num1}/{num2}")
async def calculate(num1: int, num2: int):
    return {"sum": num1 + num2, "difference": num1 - num2, "product": num1 * num2, "quotient": num1 / num2 if num2 != 0 else "undefined"}

@app.get("/echo/{word}")
async def echo(word: str):
    return {"echo": word}

@app.get("/headers")
async def get_headers(request: Request):
    return {"headers": dict(request.headers)}

@app.post("/json")
async def receive_json(data: dict):
    return {"received_data": data}

@app.get("/user-info")
async def user_info(request: Request):
    headers = dict(request.headers)
    return {"user_agent": headers.get("user-agent"), "host": headers.get("host")}

@app.get("/time-info")
async def time_info():
    now = datetime.utcnow()
    return {"year": now.year, "month": now.month, "day": now.day, "hour": now.hour, "minute": now.minute, "second": now.second}

@app.get("/status/{status_code}")
async def custom_status(status_code: int):
    return JSONResponse(status_code=status_code, content={"status": "custom status response", "code": status_code})

@app.get("/double/{number}")
async def double(number: int):
    return {"result": number * 2}

@app.get("/reverse/{text}")
async def reverse(text: str):
    return {"reversed": text[::-1]}

@app.get("/uppercase/{text}")
async def uppercase(text: str):
    return {"uppercase": text.upper()}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=9090)