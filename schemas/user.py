from datetime import date
from pydantic import BaseModel 

class User(BaseModel):
 Name:str
 Address:str
 DOB:date
