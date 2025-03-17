from pydantic import BaseModel

class RBCultivator(BaseModel):
    id: int | None = None

    def to_dict(self) -> dict:
        return self.model_dump(exclude_none=True)