from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from app.config.settings import settings

engine = create_async_engine(settings.sqlalchemy__database_url, echo=True)

session_maker = async_sessionmaker(bind=engine, autoflush=False, expire_on_commit=False)
