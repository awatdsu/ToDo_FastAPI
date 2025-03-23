from pydantic import BaseModel, Field, ConfigDict, UUID4
from datetime import datetime

class TTask(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    title: str = Field(default=..., min_length=1, max_length=100, description="Заголовок заметки, от 1 до 100 символов")
    description: str = Field(default=..., min_length=1, max_length=500, description="Текст заметки, от 1 до 500 символов")
    id: UUID4

class TTaskResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    title: str = Field(default=..., min_length=1, max_length=100, description="Заголовок заметки, от 1 до 100 символов")
    description: str = Field(default=..., min_length=1, max_length=500, description="Текст заметки, от 1 до 500 символов")
    is_completed: bool
    created_at: datetime
    id: UUID4
