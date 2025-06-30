from core.Singleton import SingletonMeta
from models.Team import TeamModel
from repositories.Team import TeamRepo


class TeamService(metaclass=SingletonMeta):
    def __init__(self) -> None:
        self.team_repo = TeamRepo()

    def add_team(self, team: TeamModel) -> None:
        self.team_repo.add_team(team)

    def get_team(self, team_id: str) -> TeamModel:
        return self.team_repo.get_team(team_id)
