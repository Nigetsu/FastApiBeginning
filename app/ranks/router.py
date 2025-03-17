from fastapi import APIRouter

from app.ranks.dao import RanksDAO
from app.ranks.schemas import CRankAdd, CRankUpdDesc


router = APIRouter(prefix="/ranks", tags=["Работа с рангами"])


@router.post("/add")
async def add_rank(rank: CRankAdd) -> dict:
    res = await RanksDAO.add(**rank.model_dump())
    if res:
        return {"message": "Ранг успешно добавлен!", "rank": rank}
    else:
        return {"message": "Ошибка при добавлении ранга!"}


@router.put("/update")
async def update_rank_description(rank: CRankUpdDesc) -> dict:
    res = await RanksDAO.update(filter_by={"rank_name": rank.rank_name},
                          rank_description=rank.rank_description)
    if res:
        return {"message": "Описание ранга успешно обновлено!", "rank": rank}
    else:
        return {"message": "Ошибка при обновлении описания ранга!"}


@router.delete("/delete/{rank_id}")
async def delete_rank(rank_id: int) -> dict:
    res = await RanksDAO.delete(id=rank_id)
    if res:
        return {"message": f"Ранг с ID {rank_id} удален!"}
    else:
        return {"message": "Ошибка при удалении ранга!"}