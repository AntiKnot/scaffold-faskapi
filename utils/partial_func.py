from functools import partial
from typing import List
from typing import Optional

from fastapi import Header
from fastapi import Query

util_Query = partial(Query, None, min_length=3, max_length=50)
util_Header = partial(Header, None, convert_underscores=False)


class UtilCookies:
    Cache_Control: Optional[str] = Header(None)
    Content_Type: Optional[str] = Header(None)
    Accept_Encoding: Optional[str] = Header(None)
    x_token: Optional[List[str]] = Header(None)
    ...
