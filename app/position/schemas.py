from pydantic import BaseModel, Field


class UPositionAdd(BaseModel):
    position_name: str = Field(..., description="Название должности")
    position_description: str = Field(None, description="Описание должности")

class UPositionUpd(BaseModel):
    position_name: str = Field(..., description="Название должности")
    position_description: str = Field(None, description="Описание должности")