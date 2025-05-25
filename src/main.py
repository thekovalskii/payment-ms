import requests
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

from .redis_manager import Order


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:3000'],
    allow_methods=['*'],
    allow_headers=['*']
)


@app.get('/orders/{pk}')
def get(pk: str):
    return Order.get(pk=pk) 


@app.post('/orders')
async def create(request: Request):
    body = await request.json()

    req = requests.get('http://localhost:8000/products/%s' % body['id'])
    product = req.json()

    order = Order(
        product_id=body['id'],
        price=product['price'],
        fee=0.2 * product['price'],
        total=1.2 * product['price'],
        quantity=body['quantity'],
        status='pending'
    )
    order.save()

    return order
