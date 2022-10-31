from typing import Union, List

from pydantic import BaseModel


class UserSchemaOutput(BaseModel):
    email: str
    name: str

    class Config:
        orm_mode = True


class UserListSchema(BaseModel):
    users: Union[List[UserSchemaOutput], None] = None


class UserSchemaInput(UserSchemaOutput):
    password: str
