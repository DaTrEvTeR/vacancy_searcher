import uuid

from sqlalchemy import (
    BOOLEAN,
    INTEGER,
    String,
    Enum,
    ForeignKey,
    UUID,
    PrimaryKeyConstraint,
    select,
)
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Mapped, relationship, mapped_column

from app.config.enums import ExperienceEnum
from app.db.base_model import Base


class User(Base):
    # table metadata
    __tablename__ = "users"
    # model attrs
    id: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    # relationships
    filters: Mapped[list["Filter"]] = relationship(
        "Filter", back_populates="user", lazy="joined", cascade="all, delete-orphan"
    )


class Filter(Base):
    # table metadata
    __tablename__ = "filters"
    # model attrs
    id: Mapped[uuid.UUID] = mapped_column(UUID, primary_key=True, default=uuid.uuid4)
    title: Mapped[str] = mapped_column(String(32), nullable=False)
    experience: Mapped[ExperienceEnum] = mapped_column(Enum(ExperienceEnum), nullable=False)
    only_remote: Mapped[bool] = mapped_column(BOOLEAN, default=False)
    active: Mapped[bool] = mapped_column(BOOLEAN, default=True)
    # relationships
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    user: Mapped["User"] = relationship("User", back_populates="filters", lazy="selectin")
    sites: Mapped[list["Site"]] = relationship(secondary="sites_filters", back_populates="filters", lazy="selectin")

    @classmethod
    async def get_user_filters_ids(cls, db: AsyncSession, user_id: int) -> list[uuid.UUID]:
        statement = select(cls.id).filter(cls.user_id == user_id)
        result = await db.execute(statement)
        return list(result.unique().scalars().all())


class Site(Base):
    # table metadata
    __tablename__ = "sites"
    # model attrs
    site_name: Mapped[str] = mapped_column(String(32), primary_key=True)
    # relationships
    filters: Mapped[list["Filter"]] = relationship(secondary="sites_filters", back_populates="sites", lazy="selectin")


class SiteFilter(Base):
    # table metadata
    __tablename__ = "sites_filters"
    __table_args__ = (PrimaryKeyConstraint("site_name", "filter_id"),)
    # model attrs
    last_sent_link: Mapped[str] = mapped_column(String(), nullable=True)
    # relationships
    site_name: Mapped[str] = mapped_column(ForeignKey("sites.site_name", ondelete="CASCADE"), nullable=False)
    filter_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("filters.id", ondelete="CASCADE"), nullable=False)
