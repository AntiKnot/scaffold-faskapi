from fastapi import APIRouter
from api.v1.files import file
from api.v1.foo import views

api_v1 = APIRouter()

api_v1.include_router(views.router, tags=['common view'])
api_v1.include_router(file.router, tags=['file'])
