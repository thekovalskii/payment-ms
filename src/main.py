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
