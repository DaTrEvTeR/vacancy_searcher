import logging

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from app.config.settings import settings

logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)

engine = create_async_engine(settings.sqlalchemy__database_url, echo=False)

session_maker = async_sessionmaker(bind=engine, autoflush=False, expire_on_commit=False)
