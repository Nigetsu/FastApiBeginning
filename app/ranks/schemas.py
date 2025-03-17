from pydantic import BaseModel, Field


class CRankAdd(BaseModel):
    rank_name: str = Field(..., description="Название ранга")
    rank_description: str = Field(None, description="Описание ранга")
    count_cultivators: int = Field(0, description="Количество пользователей")

class CRankUpdDesc(BaseModel):
    rank_name: str = Field(..., description="Название ранга")
    rank_description: str = Field(None, description="Новое описание ранга")
