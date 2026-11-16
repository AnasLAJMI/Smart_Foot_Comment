from fastapi import FastAPI, HTTPException
from backend.app.database.connection import create_tables
from backend.app.services.match_service import (
   save_match,
    get_matches,
    get_match_by_id,
    update_match,
    delete_match
)
from ai_engine.commentary.commentary_engine import generate_match_commentary
from backend.app.schemas.event import EventCreate
from backend.app.services.event_service import (
    create_event,
    get_events_by_match
)
from backend.app.schemas.match import MatchCreate
# Create the FastAPI application
app = FastAPI(
    title="SmartFoot AI",
    description="Intelligent Football Commentary System",
    version="0.1.0"
)

@app.on_event("startup")
async def startup():
    create_tables()


# Main route
@app.get("/")
async def home():
    return {
        "project": "SmartFoot AI",
        "message": "Welcome to SmartFoot AI Backend!",
        "status": "running"
    }


# Health check route
@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "service": "backend"
    }

@app.post("/matches")
async def create_match_endpoint(match: MatchCreate):
    new_match = save_match(match)

    return {
        "message": "Match saved successfully",
        "match": new_match
    }
@app.get("/matches")
async def list_matches():
    matches = get_matches()

    return {
        "total": len(matches),
        "matches": matches
    }
@app.get("/matches/{match_id}")
async def get_match(match_id: int):
    match = get_match_by_id(match_id)

    if match is None:
        raise HTTPException(
            status_code=404,
            detail="Match not found"
        )

    return {"match": match}
@app.put("/matches/{match_id}")
async def update_match_endpoint(match_id: int, match: MatchCreate):

    updated_match = update_match(match_id, match)

    if updated_match is None:
        raise HTTPException(
            status_code=404,
            detail="Match not found"
        )

    return {
        "message": "Match updated successfully",
        "match": updated_match
    }
@app.delete("/matches/{match_id}")
async def delete_match_endpoint(match_id: int):

    deleted = delete_match(match_id)

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Match not found"
        )

    return {
        "message": "Match deleted successfully",
        "match_id": match_id
    }
@app.post("/matches/{match_id}/events")
async def create_event_endpoint(match_id: int, event: EventCreate):

    if event.match_id != match_id:
        raise HTTPException(
            status_code=400,
            detail="Match ID mismatch"
        )

    match = get_match_by_id(match_id)

    if match is None:
        raise HTTPException(
            status_code=404,
            detail="Match not found"
        )

    new_event = create_event(event)

    return {
        "message": "Event created successfully",
        "event": new_event
    }
@app.get("/matches/{match_id}/events")
async def list_match_events(match_id: int):

    match = get_match_by_id(match_id)

    if match is None:
        raise HTTPException(
            status_code=404,
            detail="Match not found"
        )

    events = get_events_by_match(match_id)

    return {
        "match_id": match_id,
        "total_events": len(events),
        "events": events
    }

@app.post("/matches/{match_id}/commentary")
async def generate_commentary_for_match(match_id: int, language: str = "ar"):

    # Get match events
    events = get_events_by_match(match_id)

    if not events:
        return {"message": "No events found for this match"}

    # Generate commentary for the latest event
    event = events[-1]

    commentary = generate_match_commentary(event, language)

    return {
        "match_id": match_id,
        "event": event,
        "language": language,
        "commentary": commentary
    }
