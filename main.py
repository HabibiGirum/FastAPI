from uuid import uuid4
from fastapi import  FastAPI
from typing import List, Union

from models import Gender, Role, User

app = FastAPI()

db: List[User] =[
    User(
        id=uuid4(),
        first_name='Habtamu',
        last_name='Girum',
        middle_name='sefefe',
        gender=Gender.male,
        roles=[Role.admin]
    )
]


@app.get('/')
def read_root():
    return {"Hello": "World"}

@app.get("/api/v1/users")
async def get_user():
    return db