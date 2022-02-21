from collections.abc import Sequence
from typing import NewType

ConnectionOptions = dict[str, str]
Address = tuple[str, int]
Server = tuple[Address, ConnectionOptions]


def broadcast_message(message: str, servers: Sequence[Server]) -> None:

    def send(server: Server, msg: str):
        return 'ack'

    list([send(s, 'restart') for s in servers])


# in BaseCase can use there basic Type
UserId = NewType('UserId', int)
some_id = UserId(524313)
