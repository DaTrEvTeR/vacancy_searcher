from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession


class Base(AsyncAttrs, DeclarativeBase):
    __abstract__ = True

    async def create(self, db: AsyncSession) -> None:
        """Add object to db and refresh it"""
        db.add(self)
        try:
            await db.commit()
            await db.refresh(self)
        except Exception as e:
            await db.rollback()
            raise e

    @classmethod
    async def read_one(cls, db: AsyncSession, **filters) -> "Base":
        """Reads an object by data. Returns the retrieved object"""
        statement = select(cls).filter_by(**filters)
        result = await db.execute(statement)
        return result.unique().scalar_one_or_none()

    @classmethod
    async def read_all(cls, db: AsyncSession, **filters) -> list["Base"]:
        """Reads all objects with optional filtering. Returns the retrieved objects collection"""
        statement = select(cls).filter_by(**filters)
        result = await db.execute(statement)
        return list(result.unique().scalars().all())

    async def update(self, db: AsyncSession, **new_data) -> None:
        """Update object data, commt to db and refresh it"""
        for k, v in new_data.items():
            if hasattr(self, k):
                setattr(self, k, v)
            else:
                raise AttributeError(f"Model {type(self)} has no attribute {k}")
        db.add(self)
        try:
            await db.commit()
            await db.refresh(self)
        except Exception as e:
            await db.rollback()
            raise e

    async def delete(self, db: AsyncSession) -> None:
        """Delete object from db"""
        await db.delete(self)
        try:
            await db.commit()
        except Exception as e:
            await db.rollback()
            raise e
