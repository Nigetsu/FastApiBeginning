from datetime import datetime, date
import re
from pydantic import BaseModel, Field, EmailStr, field_validator, ConfigDict


class CCultivator(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    phone_number: str = Field(..., description="Номер телефона в международном формате, начинающийся с '+'")
    first_name: str = Field(..., min_length=1, max_length=50, description="Имя пользователя, от 1 до 50 символов")
    last_name: str = Field(..., min_length=1, max_length=50, description="Фамилия пользователя, от 1 до 50 символов")
    date_of_birth: date = Field(..., description="Дата рождения пользователя в формате ГГГГ-ММ-ДД")
    email: EmailStr = Field(..., description="Электронная почта пользователя")
    address: str = Field(..., min_length=10, max_length=200, description="Адрес пользователя, не более 200 символов")
    rank_id: int = Field(..., ge=1, description="id ранга культиватора")
    position_id: int = Field(..., ge=1, description="id должности культиватора")
    rank: str | None = Field(..., description="Название ранга")
    position: str | None = Field(..., description="Название должности")

    @field_validator("phone_number")
    def validate_phone_number(cls, value):
        if not re.match(r'^\+\d{1,15}$', value):
            raise ValueError('Номер телефона должен начинаться с "+" и содержать от 1 до 15 цифр')
        return value

    @field_validator("date_of_birth")
    def validate_date_of_birth(cls, value):
        if value and value >= datetime.now().date():
            raise ValueError('Дата рождения должна быть в прошлом')
        return value


class CCultivatorAdd(BaseModel):
    phone_number: str = Field(..., description="Номер телефона в международном формате, начинающийся с '+'")
    first_name: str = Field(..., min_length=1, max_length=50, description="Имя пользователя, от 1 до 50 символов")
    last_name: str = Field(..., min_length=1, max_length=50, description="Фамилия пользователя, от 1 до 50 символов")
    date_of_birth: date = Field(..., description="Дата рождения пользователя в формате ГГГГ-ММ-ДД")
    email: EmailStr = Field(..., description="Электронная почта пользователя")
    address: str = Field(..., min_length=10, max_length=200, description="Адрес пользователя, не более 200 символов")
    rank_id: int = Field(..., ge=1, description="ID ранга пользователя")
    position_id: int | None = Field(default=None, ge=1, description="ID должности пользователя")

    @field_validator("phone_number")
    def validate_phone_number(cls, values: str) -> str:
        if not re.match(r'^\+\d{1,15}$', values):
            raise ValueError('Номер телефона должен начинаться с "+" и содержать от 1 до 15 цифр')
        return values

    @field_validator("date_of_birth")
    def validate_date_of_birth(cls, values: date):
        if values and values >= datetime.now().date():
            raise ValueError('Дата рождения должна быть в прошлом')
        return values


class CCultivatorUpd(BaseModel):
    id: int
    phone_number: str = Field(..., description="Номер телефона в международном формате, начинающийся с '+'")
    email: EmailStr = Field(..., description="Электронная почта пользователя")

    @field_validator("phone_number")
    def validate_phone_number(cls, values: str) -> str:
        if not re.match(r'^\+\d{1,15}$', values):
            raise ValueError('Номер телефона должен начинаться с "+" и содержать от 1 до 15 цифр')
        return values