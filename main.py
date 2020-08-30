from typing import Optional

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()


app.mount('/static', StaticFiles(directory='static'), name='static')

templates = Jinja2Templates(directory='html')


@app.get('/')
async def index_page(request: Request):
    return templates.TemplateResponse('base.html', {'request': request})


@app.get('/index')
async def index_page(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})


@app.get('/api/sqldata/demo/')
async def create_data_api(request: Request):
    from src.handlers import create_data_sql

    field_list = [
        "id", "name", "datetime"
    ]
    value_list = [("1", "名称", "2020-05-01"), ("2", "名称2", "2020-06-01")]

    result = await create_data_sql(field_list, value_list)

    return {'data': result, 'code': 0}


@app.get('/api/jsondata/demo/')
async def create_data_api(request: Request):
    from src.handlers import do_create_fake_data

    count = int(request.query_params.get('count', 10))

    field_list = [
        {"name": "id"},
        {"name": "name"},
        {"name": "datetime", "format": "YYYY-MM-DD HH:MM:SS"},
        {"name": "cellphone"},
        {"name": "email", "domain": "abstack.com"},
        {"name": "price", 'digits': 2, 'decimal': 1}
    ]
    result = await do_create_fake_data(field_list, count=count)

    return {'data': result, 'count': count, 'code': 0}

