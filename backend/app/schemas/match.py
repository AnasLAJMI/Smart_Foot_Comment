
from pydantic import BaseModel, Field


class MatchCreate(BaseModel):
    home_team: str
    away_team: str
    competition: str
    minute: int = Field(ge=0, le=130)
