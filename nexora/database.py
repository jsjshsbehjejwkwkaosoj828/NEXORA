"""SQLite persistence layer for NEXORA."""
from __future__ import annotations

import sqlite3
from pathlib import Path
from typing import Any


class Database:
    """Small, explicit data-access layer backed by SQLite."""

    def __init__(self, path: str | Path = "nexora.db") -> None:
        self.path = str(path)
        self.initialize()

    def connect(self) -> sqlite3.Connection:
        connection = sqlite3.connect(self.path)
        connection.row_factory = sqlite3.Row
        connection.execute("PRAGMA foreign_keys = ON")
        return connection

    def initialize(self) -> None:
        with self.connect() as connection:
            connection.executescript("""
                CREATE TABLE IF NOT EXISTS tasks (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    details TEXT NOT NULL DEFAULT '',
                    completed INTEGER NOT NULL DEFAULT 0,
                    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
                );
                CREATE TABLE IF NOT EXISTS notes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    body TEXT NOT NULL DEFAULT '',
                    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
                );
                CREATE TABLE IF NOT EXISTS focus_sessions (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    duration_minutes INTEGER NOT NULL,
                    completed_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
                );
            """)

    def add_task(self, title: str, details: str = "") -> int:
        title = title.strip()
        if not title:
            raise ValueError("Task title cannot be empty.")
        with self.connect() as db:
            cursor = db.execute(
                "INSERT INTO tasks(title, details) VALUES (?, ?)", (title, details.strip())
            )
            return int(cursor.lastrowid)

    def list_tasks(self, include_completed: bool = True) -> list[dict[str, Any]]:
        query = "SELECT * FROM tasks"
        if not include_completed:
            query += " WHERE completed = 0"
        query += " ORDER BY completed ASC, id DESC"
        with self.connect() as db:
            return [dict(row) for row in db.execute(query).fetchall()]

    def set_task_completed(self, task_id: int, completed: bool = True) -> None:
        with self.connect() as db:
            db.execute("UPDATE tasks SET completed = ? WHERE id = ?", (int(completed), task_id))

    def delete_task(self, task_id: int) -> None:
        with self.connect() as db:
            db.execute("DELETE FROM tasks WHERE id = ?", (task_id,))

    def add_note(self, title: str, body: str = "") -> int:
        title = title.strip()
        if not title:
            raise ValueError("Note title cannot be empty.")
        with self.connect() as db:
            cursor = db.execute(
                "INSERT INTO notes(title, body) VALUES (?, ?)", (title, body.strip())
            )
            return int(cursor.lastrowid)

    def list_notes(self) -> list[dict[str, Any]]:
        with self.connect() as db:
            rows = db.execute("SELECT * FROM notes ORDER BY id DESC").fetchall()
            return [dict(row) for row in rows]

    def delete_note(self, note_id: int) -> None:
        with self.connect() as db:
            db.execute("DELETE FROM notes WHERE id = ?", (note_id,))

    def log_focus_session(self, duration_minutes: int) -> None:
        if duration_minutes <= 0:
            raise ValueError("Focus duration must be positive.")
        with self.connect() as db:
            db.execute(
                "INSERT INTO focus_sessions(duration_minutes) VALUES (?)",
                (duration_minutes,),
            )

    def summary(self) -> dict[str, int]:
        with self.connect() as db:
            tasks = db.execute(
                "SELECT COUNT(*) total, COALESCE(SUM(completed), 0) done FROM tasks"
            ).fetchone()
            sessions = db.execute(
                "SELECT COUNT(*) count, COALESCE(SUM(duration_minutes), 0) minutes "
                "FROM focus_sessions"
            ).fetchone()
            return {
                "tasks_total": int(tasks["total"]),
                "tasks_completed": int(tasks["done"]),
                "focus_sessions": int(sessions["count"]),
                "focus_minutes": int(sessions["minutes"]),
            }
