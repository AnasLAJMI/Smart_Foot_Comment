from backend.app.schemas.event import EventType


def classify_event(event_type: str):
    try:
        return EventType(event_type)
    except ValueError:
        return None


def normalize_event(event):
    return {
        "match_id": event["match_id"],
        "event_type": classify_event(event["event_type"]),
        "minute": event["minute"],
        "description": event["description"]
    }