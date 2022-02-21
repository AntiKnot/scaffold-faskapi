from typing import List
from typing import Optional
from typing import Set
from pydantic import EmailStr
from pydantic import HttpUrl
from pydantic.main import BaseModel


class Image(BaseModel):
    url: HttpUrl
    name: str  #


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    tags: Set[str] = set()
    images: Optional[List[Image]] = None


class UserBase(BaseModel):
    username: str
    email: EmailStr
    full_name: Optional[str] = None


# in django framework this called serializer deserializer
class UserIn(UserBase):
    password: str


class UserOut(UserBase):
    pass


class UserInDB(UserBase):
    hashed_password: str


class BaseItem(BaseModel):
    description: str
    type: str


class CarItem(BaseItem):
    type = 'car'


class PlaneItem(BaseItem):
    type = 'plane'
    size: int
