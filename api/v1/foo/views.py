from typing import List
from typing import Optional

from fastapi import APIRouter
from fastapi import Path
from fastapi import Query

from models.schemas import Item
from models.schemas import UserIn
from utils.partial_func import util_Query

router = APIRouter()


@router.get('/')
def read_root():
    return {'Hello': 'World'}


@router.get('/items/{item_id}')
def read_item(*,
              item_id: int = Path(..., title='The ID of the item to get'),
              q: Optional[str] = Query(None, alias='item-query')):
    return {'item_id': item_id, 'q': q}


@router.post('/items/', response_model=Item)
async def create_item(item: Item):
    return item


@router.get('/items/')
async def read_items(q: Optional[str] = util_Query(regex='^fixedquery$')):
    results = {'items': [{'item_id': 'Foo'}, {'item_id': 'Bar'}]}
    if q:
        results.update({'q': q})
    return results


@router.get('/items/', response_model=List[Item])
async def read_items():
    items = [
        {
            'name': 'Foo',
            'description': 'There comes my hero'
        },
        {
            'name': 'Red',
            'description': "It's my aeroplane"
        },
    ]
    return items


@router.put('/items/{item_id}')
async def update_item(item_id: int = Path(...,
                                          title='The ID of the item to get',
                                          ge=0,
                                          le=1000),
                      q: Optional[str] = None,
                      item: Optional[Item] = None):
    results = {'item_id': item_id}
    if q:
        results.update({'q': q})
    if item:
        results.update({'item': item})
    return results


# Don't do this in production!
@router.post('/user/', response_model=UserIn)
async def create_user(user: UserIn):
    return user
