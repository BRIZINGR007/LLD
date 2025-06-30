from typing import Any

from enums.Enums import MatchTypeEnums
from models.Match import MatchModel
from models.Team import TeamModel
from services.Match import MatchService
from services.Team import TeamService


class Main:
    def __call__(self) -> Any:
        team_service: TeamService = TeamService()
        match_service: MatchService = MatchService()
        team1 = TeamModel(name="CSK")
        team2 = TeamModel(name="KKR")
        team_service.add_team(team1)
        team_service.add_team(team2)
        match_1 = MatchModel(
            match_id="M_1", team1=team1, team2=team2, match_type=MatchTypeEnums.T_20
        )
        match_service.add_match(match_1)
        match_service.simulate_match(match_id=match_1.match_id)
        updated_match = match_service.get_match(match_id="M_1")
        print(
            f"Winner  of  the  {updated_match.match_id}  is  {updated_match.winning_team}"
        )
        print(f"\n\n Updated  Match : {updated_match}")


Main()()
