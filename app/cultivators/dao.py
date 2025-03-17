from sqlalchemy.orm import joinedload
from sqlalchemy import event, delete, update

from app.dao.base import BaseDao
from app.database import async_session_maker
from app.ranks.models import Rank
from app.cultivators.models import Cultivator
from sqlalchemy.future import select


class CultivatorDAO(BaseDao):
    model = Cultivator

    @classmethod
    async def find_full_data(cls, cultivator_id: int):
        async with async_session_maker() as session:
            query = select(cls.model).options(joinedload(cls.model.rank)).filter_by(id=cultivator_id)
            result_cultivator = await session.execute(query)
            cultivator_info = result_cultivator.scalar_one_or_none()

            if not cultivator_info:
                return None

            cultivator_data = cultivator_info.to_dict()
            cultivator_data["rank"] = cultivator_info.rank.rank_name
            return cultivator_data

    @event.listens_for(Cultivator, "after_insert")
    def receive_after_insert(mapper, connection, target):
        rank_id = target.rank_id
        connection.execute(
            update(Rank)
            .where(Rank.id == rank_id)
            .values(count_cultivators=Rank.count_cultivators + 1)
        )

    @classmethod
    async def add_cultivator(cls, **cultivator_data: dict):
        async with async_session_maker() as session:
            async with session.begin():
                new_cultivator = Cultivator(**cultivator_data)
                session.add(new_cultivator)
                await session.flush()
                new_cultivator_id = new_cultivator.id
                await session.commit()
                return new_cultivator_id

    @event.listens_for(Cultivator, "after_delete")
    def receive_after_delete(mapper, connection, target):
        rank_id = target.rank_id
        connection.execute(
            update(Rank)
            .where(Rank.id == rank_id)
            .values(count_cultivators=Rank.count_cultivators - 1)
        )

    @classmethod
    async def delete_cultivator_by_id(cls, cultivator_id: int):
        async with async_session_maker() as session:
            async with session.begin():
                query = delete(cls.model).filter_by(id=cultivator_id)
                result = await session.execute(query)

                if result.rowcount == 0:
                    return None

                await session.commit()
                return cultivator_id
