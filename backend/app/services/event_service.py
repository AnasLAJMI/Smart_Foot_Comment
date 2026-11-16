from backend.app.database.connection import get_connection


def create_event(event):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO events (
            match_id,
            event_type,
            minute,
            description
        )
        VALUES (?, ?, ?, ?)
    """, (
        event.match_id,
        event.event_type,
        event.minute,
        event.description
    ))

    connection.commit()
    event_id = cursor.lastrowid
    connection.close()

    return {
        "id": event_id,
        "match_id": event.match_id,
        "event_type": event.event_type,
        "minute": event.minute,
        "description": event.description
    }


def get_events_by_match(match_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT * FROM events
        WHERE match_id = ?
        ORDER BY minute ASC
    """, (match_id,))

    rows = cursor.fetchall()
    events = [dict(row) for row in rows]

    connection.close()

    return events