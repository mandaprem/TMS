from pydantic import BaseModel

class userSchema(BaseModel):
    # id :int
    user_name:str
    email:str
    password:str

class userRersponseSchema(BaseModel):
    id : int
    user_name : str
    email : str

class loginSchema(BaseModel):
    user_name :str
    password : str