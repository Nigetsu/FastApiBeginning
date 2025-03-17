from sqlalchemy import text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database import Base, str_uniq, int_pk, str_null_true



class Rank(Base):
    id: Mapped[int_pk]
    rank_name: Mapped[str_uniq]
    rank_description: Mapped[str_null_true]
    count_cultivators: Mapped[int] = mapped_column(server_default=text('0'))

    cultivators: Mapped[list["Cultivator"]] = relationship("Cultivator", back_populates="rank")

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, rank_name={self.rank_name!r})"

    def __repr__(self):
        return str(self)