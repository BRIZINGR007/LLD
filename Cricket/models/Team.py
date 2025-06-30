from typing import Optional


class TeamModel:
    def __init__(self, name: str) -> None:
        self.name = name
        self.location: Optional[str] = None
