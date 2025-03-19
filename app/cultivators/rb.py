class RBCultivator:
    def __init__(self,
                 cultivator_id: int | None,
                 rank_id: int | None,
                 position_id: int | None):
        self.id = cultivator_id
        self.rank_id = rank_id
        self.position_id = position_id

    def to_dict(self) -> dict:
        return {key: value for key, value in {
            "cultivator_id": self.id,
            "rank_id": self.rank_id,
            "position_id": self.position_id
        }.items() if value is not None}