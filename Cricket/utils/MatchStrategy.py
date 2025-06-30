import random
from typing import List, Optional, Tuple
from abc import ABC

from enums.Enums import InningsType, MatchTypeEnums
from models.Match import InningsModel, MatchModel
from models.Team import TeamModel


class BaseMatchStrategy(ABC):
    def __init__(self) -> None:
        self.runs_weight: List[Tuple[int, float]] = [
            (1, 0.3),
            (1, 0.5),
            (2, 0.5),
            (3, 0.1),
            (4, 0.3),
            (5, 0.1),
            (6, 0.2),
        ]
        self.wickets_weight: List[Tuple[int, float]] = [(1, 0.2), (0, 0.8)]

    def _simulate_toss(self, match: MatchModel) -> Tuple[TeamModel, TeamModel]:
        toss_winner, decision = (
            random.choice([match.team1, match.team2]),
            random.choice([InningsType.BATTING, InningsType.BOWLING]),
        )
        if toss_winner == match.team1:
            if decision == InningsType.BATTING:
                batting_first = match.team1
                bowling_first = match.team2
            else:
                batting_first = match.team2
                bowling_first = match.team1
        else:
            if decision == InningsType.BATTING:
                batting_first = match.team2
                bowling_first = match.team1
            else:
                batting_first = match.team1
                bowling_first = match.team2
        return (batting_first, bowling_first)

    def _get_runs(self) -> int:
        return random.choices(
            [y for y, _ in self.runs_weight],
            weights=[x for _, x in self.runs_weight],
            k=1,
        )[0]

    def _get_wickets(self) -> int:
        return random.choices(
            [y for y, _ in self.wickets_weight],
            weights=[x for _, x in self.wickets_weight],
            k=1,
        )[0]

    def simulate_match(self, match: MatchModel) -> MatchModel:
        raise NotImplementedError


class T2OMatchStrategy(BaseMatchStrategy):
    def __init__(self) -> None:
        super().__init__()

    def simulate_innings(
        self, innings: InningsModel, target: Optional[int] = None
    ) -> InningsModel:
        innings_over = False
        for _ in range(20):
            if innings_over == True:
                break
            for _ in range(6):
                innings.total_runs += self._get_runs()
                innings.total_wickets += self._get_wickets()
                if innings.total_wickets == 10:
                    innings_over = True
                    break
                if target and innings.total_runs >= target:
                    innings_over = True
                    break
        return innings

    def simulate_match(self, match: MatchModel) -> MatchModel:
        batting_first, bowling_first = self._simulate_toss(match)
        innings1 = InningsModel(batting_team=batting_first, bowling_team=bowling_first)
        innings2 = InningsModel(batting_team=bowling_first, bowling_team=batting_first)
        self.simulate_innings(innings1)
        self.simulate_innings(innings2, target=innings1.total_runs + 1)
        winner = (
            batting_first
            if innings1.total_runs > innings2.total_runs
            else bowling_first
        )
        match.winning_team = winner.name
        match.innings = [innings1, innings2]
        return match


class MatchStrategyFactoryProvider:
    @staticmethod
    def get_matchstratgey(match_type: MatchTypeEnums) -> BaseMatchStrategy:
        match match_type:
            case MatchTypeEnums.T_20:
                return T2OMatchStrategy()
            case _:
                raise ValueError("Unsupported  Match Type  ...")
