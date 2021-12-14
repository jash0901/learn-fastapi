from sqlalchemy import Table,Column
from sqlalchemy.sql.sqltypes import Date
from config.db import meta

users=Table(
    'users',meta,
    Column('id','Integer',primary_key=True),
    Column('Name',str(255)),
    Column('Address',str(255)),
    Column('DOB',Date)

)