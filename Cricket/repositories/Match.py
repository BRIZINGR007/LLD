from typing import Dict
from models.Match import MatchModel


class MatchRepo:
    def __init__(self) -> None:
        self.matches: Dict[str, MatchModel] = {}

    def add_match(self, match: MatchModel) -> None:
        self.matches[match.match_id] = match

    def get_match(self, match_id: str) -> MatchModel:
        return self.matches[match_id]

    def update_match(self, match: MatchModel) -> None:
        self.add_match(match)
