from fastapi import APIRouter

from app.position.dao import PositionDAO
from app.position.schemas import UPositionAdd, UPositionUpd


router = APIRouter(prefix="/position", tags=["Работа с должностями"])


@router.post("/add")
async def add_position(position: UPositionAdd) -> dict:
    res = await PositionDAO.add(**position.model_dump())
    if res:
        return {"message": "Должность успешно добавлен!", "position": position}
    else:
        return {"message": "Ошибка при добавлении должности!"}


@router.put("/update")
async def update_position_description(position: UPositionUpd) -> dict:
    res = await PositionDAO.update(filter_by={"position_name": position.position_name},
                          position_description=position.position_description)
    if res:
        return {"message": "Описание должности успешно обновлено!", "position": position}
    else:
        return {"message": "Ошибка при обновлении описания должности!"}


@router.delete("/delete")
async def delete_position(position_id: int) -> dict:
    res = await PositionDAO.delete(id=position_id)
    if res:
        return {"message": f"Должность с ID {position_id} удален!"}
    else:
        return {"message": "Ошибка при удалении должности!"}
