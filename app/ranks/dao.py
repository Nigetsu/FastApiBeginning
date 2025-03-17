from app.dao.base import BaseDao
from app.ranks.models import Rank

class RanksDAO(BaseDao):
    model = Rank