from fastapi import APIRouter
from config.db import conn
from models.index import users
from schemas.index import User

user = APIRouter()

@user.get('/')
async def read_data():
    return conn.execute(users.select()).fetchall()

@user.get('/{id}')
async def read_data(id:int):
    return conn.execute(users.select().where(users.c.id==id)).fetchall()


@user.post('/')
async def write_data():
    return conn.execute(users.insert().values(
        Name=user.name,
        Address=user.address,
        DOB=user.dob,
    ))
    return conn.execute(users.select()).fetchall()

@user.put('/{id}')
async def update_data(id:int,user:User):
    return conn.execute(users.update(
        Name=user.name,
        Address=user.address,
        DOB=user.dob, 
    ).where(users.c.id==id))
    return conn.execute(users.select()).fetchall()

@user.delete('/')
async def delete_data():
    conn.execute(users.delete().where(users.c.id==id))
    return conn.execute(users.select()).fetchall()