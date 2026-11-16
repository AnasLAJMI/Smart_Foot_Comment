
def get_matches():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM matches")

    rows = cursor.fetchall()

    matches = [dict(row) for row in rows]

    connection.close()

    return matches

def create_match(match):
    return {
        "home_team": match.home_team,
        "away_team": match.away_team,
        "competition": match.competition,
        "minute": match.minute
    }

from backend.app.database.connection import get_connection


def save_match(match):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO matches (home_team, away_team, competition, minute)
        VALUES (?, ?, ?, ?)
    """, (
        match.home_team,
        match.away_team,
        match.competition,
        match.minute
    ))

    connection.commit()

    match_id = cursor.lastrowid

    connection.close()

    return {
        "id": match_id,
        "home_team": match.home_team,
        "away_team": match.away_team,
        "competition": match.competition,
        "minute": match.minute
    }

def get_match_by_id(match_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM matches WHERE id = ?",
        (match_id,)
    )

    row = cursor.fetchone()

    connection.close()

    if row is None:
        return None

    return dict(row)

def update_match(match_id, match):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        UPDATE matches
        SET home_team = ?,
            away_team = ?,
            competition = ?,
            minute = ?
        WHERE id = ?
    """, (
        match.home_team,
        match.away_team,
        match.competition,
        match.minute,
        match_id
    ))

    connection.commit()

    if cursor.rowcount == 0:
        connection.close()
        return None

    cursor.execute(
        "SELECT * FROM matches WHERE id = ?",
        (match_id,)
    )

    updated_match = dict(cursor.fetchone())

    connection.close()

    return updated_match
def delete_match(match_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM matches WHERE id = ?",
        (match_id,)
    )

    connection.commit()

    deleted = cursor.rowcount > 0

    connection.close()

    return deleted