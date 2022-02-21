from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from settings import config

engine = create_engine(config.CLICKHOUSE_DATABASE_URI, pool_pre_ping=True)
session = cs.make_session(engine)
