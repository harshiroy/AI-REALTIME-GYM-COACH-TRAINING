import sqlite3
import streamlit as st
from pathlib import Path


# --------------------------------------------------
# DB PATH
# --------------------------------------------------
_DB_PATH = str(Path(__file__).parent.parent.parent / "data.db")


# --------------------------------------------------
# CONNECTION (CACHED)
# --------------------------------------------------
@st.cache_resource
def _get_connection() -> sqlite3.Connection:
    conn = sqlite3.connect(_DB_PATH, check_same_thread=False)
    conn.row_factory = sqlite3.Row

    conn.execute("PRAGMA foreign_keys = ON")

    return conn


# --------------------------------------------------
# INIT DB
# --------------------------------------------------
def init_db() -> None:
    conn = _get_connection()

    with conn:
        # USERS TABLE
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
                id         INTEGER PRIMARY KEY AUTOINCREMENT,
                username   TEXT UNIQUE NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """
        )

        # EXERCISES TABLE
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS exercises (
                id            INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id       INTEGER NOT NULL,
                exercise_name TEXT    NOT NULL,
                reps          INTEGER NOT NULL DEFAULT 0,
                sets          INTEGER NOT NULL DEFAULT 0,
                duration      INTEGER NOT NULL DEFAULT 0,
                workout_date  DATE    DEFAULT (DATE('now')),
                created_at    TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

                FOREIGN KEY(user_id) REFERENCES users(id) ON DELETE CASCADE
            )
            """
        )

        # INDEX FOR PERFORMANCE
        conn.execute(
            """
            CREATE INDEX IF NOT EXISTS idx_exercise_lookup
            ON exercises(user_id, exercise_name, workout_date)
            """
        )


# --------------------------------------------------
# USER OPERATIONS
# --------------------------------------------------
def get_user(username: str) -> sqlite3.Row | None:
    conn = _get_connection()

    return conn.execute(
        "SELECT * FROM users WHERE username = ?", (username,)
    ).fetchone()


def create_user(username: str) -> sqlite3.Row:
    conn = _get_connection()

    with conn:
        conn.execute(
            "INSERT INTO users (username) VALUES (?)",
            (username.strip(),)
        )

    return get_user(username)


def get_or_create_user(username: str) -> sqlite3.Row:
    conn = _get_connection()
    username = username.strip()

    try:
        with conn:
            conn.execute(
                "INSERT INTO users (username) VALUES (?)",
                (username,)
            )
    except sqlite3.IntegrityError:
        # user already exists → safe fallback
        pass

    return get_user(username)


# --------------------------------------------------
# EXERCISE OPERATIONS
# --------------------------------------------------
def add_exercise(user_id: int, exercise_name: str, reps: int, sets: int, duration: int) -> None:
    conn = _get_connection()

    with conn:
        existing = conn.execute(
            """
            SELECT * FROM exercises 
            WHERE user_id = ?
              AND exercise_name = ?
              AND workout_date = DATE('now')
            """,
            (user_id, exercise_name),
        ).fetchone()

        if existing:
            conn.execute(
                """
                UPDATE exercises 
                SET reps = reps + ?, 
                    sets = sets + ?, 
                    duration = duration + ?
                WHERE id = ?
                """,
                (reps, sets, duration, existing["id"]),
            )
        else:
            conn.execute(
                """
                INSERT INTO exercises (
                    user_id, exercise_name, reps, sets, duration
                )
                VALUES (?, ?, ?, ?, ?)
                """,
                (user_id, exercise_name, reps, sets, duration),
            )


def get_user_exercises(user_id: int):
    conn = _get_connection()

    return conn.execute(
        """
        SELECT * FROM exercises 
        WHERE user_id = ?
        ORDER BY created_at DESC
        """,
        (user_id,),
    ).fetchall()


# --------------------------------------------------
# OPTIONAL: RESET USER DATA (HELPFUL FOR TESTING)
# --------------------------------------------------
def reset_user_data(user_id: int) -> None:
    conn = _get_connection()

    with conn:
        conn.execute(
            "DELETE FROM exercises WHERE user_id = ?",
            (user_id,)
        )