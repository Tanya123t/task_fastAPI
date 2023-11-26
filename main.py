from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def f_index():
    return {"Павленко Татьяна Александровна"}

@app.get('/tools')
async def f_indexT():
    return "низкие навыки программирования"

@app.get('/users')
async def f_indexU():
    return "89635311774"