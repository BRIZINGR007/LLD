from typing import Dict
from models.Team import TeamModel


class TeamRepo:
    def __init__(self) -> None:
        self.teams: Dict[str, TeamModel] = {}

    def add_team(self, team: TeamModel) -> None:
        self.teams[team.name] = team

    def get_team(self, name: str) -> TeamModel:
        return self.teams[name]
