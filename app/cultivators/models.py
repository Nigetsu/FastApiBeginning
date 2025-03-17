from sqlalchemy import ForeignKey, Text
from sqlalchemy.orm import relationship, Mapped, mapped_column
from app.database import Base, str_uniq, int_pk
from datetime import date

from app.ranks.models import Rank
from app.position.models import Position


class Cultivator(Base):
    id: Mapped[int_pk]
    phone_number: Mapped[str_uniq]
    first_name: Mapped[str]
    last_name: Mapped[str]
    date_of_birth: Mapped[date]
    email: Mapped[str_uniq]
    address: Mapped[str] = mapped_column(Text, nullable=False)
    rank_id: Mapped[int] = mapped_column(ForeignKey("ranks.id"), nullable=False)
    rank: Mapped["Rank"] = relationship("Rank", back_populates="cultivators")
    position_id: Mapped[int | None] = mapped_column(ForeignKey("positions.id"), nullable=True)
    position: Mapped["Position"] = relationship("Position", back_populates="cultivators")


    def __str__(self):
        return (f"{self.__class__.__name__}(id={self.id}, "
                f"first_name={self.first_name!r},"
                f"last_name={self.last_name!r})")

    def __repr__(self):
        return str(self)

    def to_dict(self):
        return {
            "id": self.id,
            "phone_number": self.phone_number,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "date_of_birth": self.date_of_birth,
            "email": self.email,
            "address": self.address,
        }