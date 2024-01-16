from pydantic import BaseModel



class ResponseUserModel(BaseModel):
    username : str
    email : str
    phone : str
    password: str
    

class UserResponse(BaseModel):
    id: int
    username: str
   