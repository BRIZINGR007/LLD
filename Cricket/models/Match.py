from typing import List, Optional
from enums.Enums import MatchTypeEnums
from models.Team import TeamModel


class InningsModel:
    def __init__(self, batting_team: TeamModel, bowling_team: TeamModel) -> None:
        self.batting_team = batting_team
        self.bowling_team = bowling_team
        self.total_runs = 0
        self.total_wickets = 0

    def __str__(self) -> str:
        return f"Innings(Batting: {self.batting_team.name}, Bowling: {self.bowling_team.name}, Runs: {self.total_runs}, Wickets: {self.total_wickets})"

    def __repr__(self) -> str:
        return self.__str__()


class MatchModel:
    def __init__(
        self,
        match_id: str,
        team1: TeamModel,
        team2: TeamModel,
        match_type: MatchTypeEnums,
    ) -> None:
        self.match_id = match_id
        self.team1 = team1
        self.team2 = team2
        self.innings: List[InningsModel] = []
        self.match_type = match_type
        self.winning_team: Optional[str] = None

    def __str__(self) -> str:
        innings_info = ""
        if self.innings:
            innings_info = "\nInnings:\n"
            for i, inning in enumerate(self.innings, 1):
                innings_info += f"  {i}. {inning}\n"
        else:
            innings_info = "\nNo innings played yet\n"

        return f"""Match Details:
            Match ID: {self.match_id}
            Match Type: {self.match_type.value if hasattr(self.match_type, 'value') else self.match_type}
            Team 1: {self.team1.name}
            Team 2: {self.team2.name}
            Winner: {self.winning_team if self.winning_team else 'TBD'}{innings_info}
        """

    def __repr__(self) -> str:
        return self.__str__()
