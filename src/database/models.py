"""
Модели бд
"""
import uuid
import datetime

from sqlalchemy import ForeignKey, String, text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4) 
    username: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    created_at: Mapped[datetime.datetime]   = mapped_column(server_default=text("TIMEZONE('utc',now())"))
    hashed_password: Mapped[str] = mapped_column(String(128), nullable=False)


    tasks: Mapped[list["Task"]] = relationship("Task", back_populates="owner")

    def __repr__(self) -> str:
        return f"<User(id={self.id}, username={self.username}, tasks={self.tasks})>"

class Task(Base):
    __tablename__ = "tasks"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    owner_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id"), UUID(as_uuid=True))
    created_at: Mapped[datetime.datetime]   = mapped_column(server_default=text("TIMEZONE('utc',now())"))
    title: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str] = mapped_column(String(500), nullable=False)
    is_completed: Mapped[bool] = mapped_column(default=False)

    owner: Mapped["User"] = relationship("User", back_populates="tasks")

    def __repr__(self) -> str:
        return f"<User(id={self.id}, title={self.title}, description={self.description}, is_completed={self.is_completed}, owner_id={self.owner_id}, owner={self.owner})>"
    