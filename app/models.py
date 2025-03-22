"""
Модели бд
"""
import uuid
import datetime

from sqlalchemy import String, text, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.asyncio import AsyncAttrs

class Base(AsyncAttrs, DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4) 
    username: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    first_name: Mapped[str] = mapped_column(String(50), nullable=False)
    last_name: Mapped[str] = mapped_column(String(50), nullable=False)
    created_at: Mapped[datetime.datetime]   = mapped_column(server_default=text("TIMEZONE('utc',now())"))
    password: Mapped[str] = mapped_column(String(256), nullable=False)

    is_user: Mapped[bool] = mapped_column(default=True, server_default=text('true'), nullable=False)
    is_admin: Mapped[bool] = mapped_column(default=False, server_default=text('false'), nullable=False)
    is_super_admin: Mapped[bool] = mapped_column(default=False, server_default=text('false'), nullable=False)

    tasks: Mapped[list["Task"]] = relationship("Task", back_populates="owner")

    def __repr__(self) -> str:
        return f"<User(id={self.id}, username={self.username}, tasks={self.tasks})>"

class Task(Base):
    __tablename__ = "tasks"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    owner_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id"))
    created_at: Mapped[datetime.datetime]   = mapped_column(server_default=text("TIMEZONE('utc',now())"))
    title: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str] = mapped_column(String(500), nullable=False)
    is_completed: Mapped[bool] = mapped_column(default=False)

    owner: Mapped["User"] = relationship("User", back_populates="tasks")

    def __repr__(self) -> str:
        return f"<User(id={self.id}, title={self.title}, description={self.description}, is_completed={self.is_completed}, owner_id={self.owner_id}, owner={self.owner})>"
