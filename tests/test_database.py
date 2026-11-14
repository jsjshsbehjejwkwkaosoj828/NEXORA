"""Tests for NEXORA's local persistence layer."""
import pytest
from nexora.database import Database


@pytest.fixture
def db(tmp_path):
    return Database(tmp_path / "test.sqlite3")


def test_task_lifecycle(db):
    task_id = db.add_task("Ship the first version", "Review the basics")
    assert len(db.list_tasks()) == 1
    db.set_task_completed(task_id)
    assert db.list_tasks()[0]["completed"] == 1
    assert db.list_tasks(include_completed=False) == []
    db.delete_task(task_id)
    assert db.list_tasks() == []


def test_note_lifecycle(db):
    note_id = db.add_note("Idea", "A useful thought")
    assert db.list_notes()[0]["body"] == "A useful thought"
    db.delete_note(note_id)
    assert db.list_notes() == []


def test_empty_titles_are_rejected(db):
    with pytest.raises(ValueError):
        db.add_task("   ")
    with pytest.raises(ValueError):
        db.add_note("")


def test_focus_summary(db):
    db.log_focus_session(25)
    summary = db.summary()
    assert summary["focus_sessions"] == 1
    assert summary["focus_minutes"] == 25
