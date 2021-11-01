import logging
import sqlite3
import typing as t

from pathlib import Path

from .utils import is_platform_windows


logger_log = logging.getLogger("xleapp.logfile")


def open_sqlite_db_readonly(path: t.Union[Path, str]) -> sqlite3.Connection:
    """Opens an sqlite db in read-only mode, so original db
    (and -wal/journal are intact)
    """
    if isinstance(path, str):
        path = Path(path)

    if is_platform_windows and path.drive.startswith("\\\\?\\"):
        path = Path(path)

    try:
        db = sqlite3.connect(
            f"file:{path.resolve()}?mode=ro",
            uri=True,
        )
        cursor = db.cursor()
        # This will fail if not a database file
        cursor.execute("PRAGMA page_count").fetchone()
        db.row_factory = sqlite3.Row
    except sqlite3.DatabaseError:
        raise sqlite3.DatabaseError(f"File {path!r} failed to open as a database!")

    return db


def does_column_exist_in_db(
    db: sqlite3.Connection,
    table_name: str,
    col_name: str,
) -> bool:
    """Checks if a specific col exists"""
    col_name = col_name.lower()
    try:
        db.row_factory = sqlite3.Row  # For fetching columns by name
        query = f"pragma table_info('{table_name}');"
        cursor = db.cursor()
        cursor.execute(query)
        all_rows = cursor.fetchall()
        for row in all_rows:
            if row["name"].lower() == col_name:
                return True
    except sqlite3.Error as ex:
        logger_log.error(f"Query error, query={query} Error={str(ex)}")
    return False


def does_table_exist(db: sqlite3.Connection, table_name: str) -> bool:
    """Checks if a table with specified name exists in an sqlite db"""
    try:
        query = (
            "SELECT name FROM sqlite_master WHERE type='table' AND name= %(table_name)s"
        )

        params = {"table_name": table_name}

        cursor = db.execute(query, params)
        for _ in cursor:
            return True
    except sqlite3.Error as ex:
        logger_log.error(f"Query error, query={query} Error={str(ex)}")
    return False
