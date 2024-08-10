from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from models import Weather
from api import api_get_weather

app = FastAPI()



@app.get("/")
async def index():
    return {"message": "Hello to my weather API!"}


@app.get("/weather/")
async def get_weather(city: str = None, is_json: bool = False):
    response = await api_get_weather(city)
    weather = Weather(**response)

    if is_json:
        return {
            "weather": weather
        }
    
    return HTMLResponse(content=f"<h1>Weather for {weather.location.name}/{weather.location.country} is {weather.current.temp_c}</h1>")