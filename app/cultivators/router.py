from fastapi import APIRouter
from fastapi.params import Depends

from app.cultivators.dao import CultivatorDAO
from app.cultivators.rb import RBCultivator
from app.cultivators.schemas import CCultivators, CCultivatorAdd, CCultivatorUpd

router = APIRouter(prefix="/cultivators", tags=["Работа с культиваторами"])


@router.get("/", summary="Получить всех культиваторов")
async def get_all_cultivators(request_body: RBCultivator = Depends()) -> list[CCultivators]:
    return await CultivatorDAO.find_all(**request_body.to_dict())


@router.get("/{id}", summary="Получить культиватора по id")
async def get_cultivator_by_id(cultivator_id: int) -> CCultivators | dict:
    res = await CultivatorDAO.find_full_data(cultivator_id)
    if res is None:
        return {"message": f"Культиватор с ID {cultivator_id} не найден!"}
    return res


@router.get("/by_filter", summary="Получить культиватора по фильтру")
async def get_cultivator_by_filter(request_body: RBCultivator = Depends()) -> CCultivators:
    res = await CultivatorDAO.find_one_or_none_by_id(**request_body.to_dict())
    if res is None:
        return {"message": "Культиватор с указанными вами параметрами не найден!"}
    return res


@router.post("/add", summary="Добавить культиватора")
async def add_cultivator(cultivator: CCultivatorAdd) -> dict:
    res = await CultivatorDAO.add_cultivator(**cultivator.model_dump())
    if res:
        return {"message": "Культиватор успешно добавлен!", "cultivator": cultivator}
    else:
        return {"message": "Ошибка при добавлении культиватора!"}


@router.put("/update", summary="Обновить данные культиватора")
async def update_cultivator_description(cultivator: CCultivatorUpd) -> dict:
    res = await CultivatorDAO.update(filter_by={"id": cultivator.id},
                                     phone_number=cultivator.phone_number,
                                     email=cultivator.email)
    if res:
        return {"message": "Успешно обновлено!", "cultivator": cultivator}
    else:
        return {"message": "Ошибка при обновлении!"}


@router.delete("/delete/{user_id}", summary="Удалить культиватора по id")
async def delete_cultivator_by_id(cultivator_id: int) -> dict:
    res = await CultivatorDAO.delete_cultivator_by_id(cultivator_id=cultivator_id)
    if res:
        return {"message": f"Культиватор с ID {cultivator_id} удален!"}
    else:
        return {"message": "Ошибка при удалении культиватора!"}