from sqlalchemy.orm import Mapped, relationship
from app.database import Base, str_uniq, int_pk, str_null_true



class Position(Base):
    id: Mapped[int_pk]
    position_name: Mapped[str_uniq]
    position_description: Mapped[str_null_true]

    cultivators: Mapped["Cultivator"] = relationship("Cultivator", back_populates="position")

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, rank_name={self.rank_name!r})"

    def __repr__(self):
        return str(self)