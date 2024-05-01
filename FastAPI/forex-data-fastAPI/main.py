import requests
import httpx
import aiohttp
from pprint import PrettyPrinter
from fastapi import FastAPI
from fastapi import APIRouter, Request

pp = PrettyPrinter()
app = FastAPI()


# @app.get("/")
# async def slow_route():
#     async with aiohttp.ClientSession() as session:
#         async with session.get("https://marketdata.tradermade.com/api/v1/live") as resp:
#             data = await resp.json()
#             # do something with data
#             return data

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




@app.get('/get_data')
def first_data():
    api_url = "https://marketdata.tradermade.com/api/v1/live"
    all_data = requests.get(api_url).json()
    data1 = all_data[0]
    return {'user': data1}

@app.get('/get_data_2')
async def second_data():
    api_url = "https://marketdata.tradermade.com/api/v1/live"
    async with httpx.AsyncClient() as client:
        response = await client.get(api_url)
        all_data = response.json()
        data2 = all_data[1]
        return {'data': data2}



@app.post("/")
async def post():
    return {"message" : "hello from post method route"}


@app.put("/")
async def put():
    return {"message": "hello from put method route"}

