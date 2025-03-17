from app.dao.base import BaseDao
from app.position.models import Position


class PositionDAO(BaseDao):
    model = Position