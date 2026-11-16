from pydantic import BaseModel, Field


class EventCreate(BaseModel):
    match_id: int
    event_type: str
    minute: int = Field(ge=0, le=130)
    description: str
from enum import Enum
from pydantic import BaseModel, Field


class EventType(str, Enum):
    GOAL = "Goal"
    YELLOW_CARD = "Yellow Card"
    RED_CARD = "Red Card"
    SUBSTITUTION = "Substitution"
    SHOT = "Shot"
    PASS = "Pass"


class EventCreate(BaseModel):
    match_id: int
    event_type: EventType
    minute: int = Field(ge=0, le=130)
    description: str