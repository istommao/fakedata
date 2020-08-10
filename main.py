from typing import Optional

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()


app.mount('/static', StaticFiles(directory='static'), name='static')

templates = Jinja2Templates(directory='html')


@app.get('/')
async def index_page(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})


@app.get('/api/jsondata/demo/')
async def create_data_api(request: Request):
    from src.handlers import do_create_fake_data

    field_list = [
        {"name": "id"},
        {"name": "name"},
        {"name": "datetime", "format": "YYYY-MM-DD HH:MM:SS"},
        {"name": "cellphone"},
        {"name": "email", "domain": "abstack.com"},
        {"name": "price", 'digits': 2, 'decimal': 1}
    ]
    result = await do_create_fake_data(field_list, count=100)

    return result
