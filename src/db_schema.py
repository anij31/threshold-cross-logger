"""
Initializes database schema creation for sensors project.
Run this once at the start to set up the database
"""

import sqlite3
from pathlib import Path
from typing import Union

DB_FILE: Path = Path(__file__).parent / "sensors.db"

def create_schema(db_path: Union[Path, str] = DB_FILE) -> None:
    """
    Creates initial database schema for the sensors project.
    - sensors table: stores metadata for each sensor.
    """
    db_path = Path(db_path)
    db_path.parent.mkdir(parents=True, exist_ok=True)
    
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS sensors (
            sensor_id INTEGER PRIMARY KEY,        -- will store hash based IDs
            sensor_name TEXT NOT NULL UNIQUE,
            sensor_type TEXT NOT NULL,
            created_at TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%SZ', 'now'))
        )
        """)

        conn.commit()
    
    print(f"Database schema created successfully in {db_path.resolve()}")


if __name__ == "__main__":
    create_schema()

