from core.Singleton import SingletonMeta
from models.Match import MatchModel
from repositories.Match import MatchRepo
from utils.MatchStrategy import MatchStrategyFactoryProvider


class MatchService(metaclass=SingletonMeta):
    def __init__(self) -> None:
        self._match_repo = MatchRepo()

    def add_match(self, match: MatchModel) -> None:
        self._match_repo.add_match(match)

    def get_match(self, match_id: str) -> MatchModel:
        return self._match_repo.get_match(match_id)

    def update_match(self, match: MatchModel) -> None:
        self._match_repo.update_match(match)

    def simulate_match(self, match_id: str) -> None:
        match = self.get_match(match_id)
        match_strategy = MatchStrategyFactoryProvider().get_matchstratgey(
            match.match_type
        )
        updated_match = match_strategy.simulate_match(match)
        self.update_match(updated_match)
