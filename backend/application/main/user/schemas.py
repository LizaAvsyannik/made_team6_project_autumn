from pydantic import BaseModel
from typing import Union, List


class UserSchemaOutput(BaseModel):
    email: str
    name: str

    class Config:
        orm_mode = True


class UserListSchema(BaseModel):
    users: Union[List[UserSchemaOutput], None] = None


class UserSchemaInput(UserSchemaOutput):
    password: str
