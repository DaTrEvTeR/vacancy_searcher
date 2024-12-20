from uuid import uuid4

from sqlalchemy import INTEGER, UUID, ForeignKey, String, Enum
from sqlalchemy.orm import Mapped, relationship, mapped_column

from app.config.enums import ExperienceEnum
from app.db.base_model import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(INTEGER, primary_key=True)

    filters: Mapped[list["Filter"]] = relationship("Filter", back_populates="user")


class Filter(Base):
    __tablename__ = "filters"

    id: Mapped[UUID] = mapped_column(UUID, primary_key=True, default=uuid4)

    user_id: Mapped[User] = mapped_column(
        ForeignKey(User.id, ondelete="CASCADE"), nullable=False
    )
    user: Mapped[User] = relationship(User, back_populates="filters", lazy="joined")

    title: Mapped[str] = mapped_column(String(30))
    experience: Mapped[ExperienceEnum] = mapped_column(
        Enum(ExperienceEnum), nullable=True
    )
    abroad: Mapped[bool]
    only_remote: Mapped[bool]

    sites: Mapped[list["Site"]] = relationship(
        secondary="sites_filters", back_populates="filters", lazy="joined"
    )


class Site(Base):
    __tablename__ = "sites"

    site: Mapped[str] = mapped_column(String(30), primary_key=True)

    filters: Mapped[list["Filter"]] = relationship(
        secondary="sites_filters", back_populates="sites", lazy="joined"
    )


class SiteFilter(Base):
    __tablename__ = "sites_filters"

    id: Mapped[UUID] = mapped_column(UUID, primary_key=True, default=uuid4)

    site_id: Mapped[Site] = mapped_column(
        ForeignKey(Site.site, ondelete="CASCADE"), nullable=False
    )
    filter_id: Mapped[Filter] = mapped_column(
        ForeignKey(Filter.id, ondelete="CASCADE"), nullable=False
    )
