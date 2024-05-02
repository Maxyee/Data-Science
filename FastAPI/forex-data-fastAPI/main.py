import requests
import httpx
import aiohttp
from pprint import PrettyPrinter
from fastapi import FastAPI
from fastapi import APIRouter, Request

pp = PrettyPrinter()
app = FastAPI()


@app.get("/")
async def root(request: Request):
    url = "https://marketdata.tradermade.com/api/v1/live"
    currency = "USDJPY,GBPUSD,UK100"
    api_key = "q_csXrJmlzDRc-8kkAkN"
    querystring = {"currency":currency,"api_key":api_key}
    response = requests.get(url, params=querystring)
    result = response.json()
    result1 = pp.pprint(response.json())
    print(result)
    return {'data': result}


@app.get("/daily")
async def daily():
    url = "https://marketdata.tradermade.com/api/v1/historical" 
    date = "2021-03-15"
    currency = "EURUSD"
    api_key = "q_csXrJmlzDRc-8kkAkN"
    querystring = {"currency":currency,"date":date, "api_key":api_key}
    response = requests.get(url, params=querystring)
    result = response.json()
    print(result)
    return {'data': result}


@app.get("/min_hour")
async def min_hour():
    fx = ["EURUSD", "USDJPY"]
    dates = ["2021-03-15-13:00"]
    array = []
    api_key = "q_csXrJmlzDRc-8kkAkN"
    url = "https://marketdata.tradermade.com/api/v1/minute_historical"
    for i in fx:
        for date in dates: 
            querystring = {"currency":i,"date_time":date, "api_key":api_key}
            response = requests.get(url, params=querystring)
            array.append(response.json())
    result = array
    print(result)
    return {'data': result}

@app.get("/time_series")
async def time_series():
    url = "https://marketdata.tradermade.com/api/v1/timeseries?"
    currency="USDJPY"
    api_key = "q_csXrJmlzDRc-8kkAkN"
    start_date="2021-03-01"
    end_date="2021-03-22"
    format="split"
    interval="daily"
    querystring = {"currency":currency,"start_date":start_date, "api_key":api_key, 
                   "end_date":end_date, "format":format, "interval": interval}
    response = requests.get(url, params=querystring)
    result = response.json()
    print(result)
    return {'data': result}






