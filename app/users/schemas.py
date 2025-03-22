from pydantic import BaseModel, Field, ConfigDict


class UUser(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    username: str = Field(default=..., min_length=4, max_length=50, description="Юзернейм пользователя")
    first_name: str = Field(default=..., min_length=1, max_length=50, description="Имя пользователя, от 1 до 50 символов")
    last_name: str = Field(default=..., min_length=1, max_length=50, description="Фамилия пользователя, от 1 до 50 символов")

class SUserRegister(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    username: str = Field(default=..., min_length=4, max_length=50, description="Юзернейм пользователя")
    first_name: str = Field(default=..., min_length=1, max_length=50, description="Имя пользователя, от 1 до 50 символов")
    last_name: str = Field(default=..., min_length=1, max_length=50, description="Фамилия пользователя, от 1 до 50 символов")
    password: str = Field(...,min_length=8, max_length=50, description="Пароль, от 8 до 50 символов")

class SUserAuth(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    username: str = Field(..., description="Юзернейм пользователя")
    password: str = Field(..., min_length=8, max_length=50, description="Пароль, от 8 до 50 символов")