from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from settings import config

Base = cs.get_declarative_base(metadata=sqlalchemy.MetaData(bind=engine))
