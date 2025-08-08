import sqlite3
from datetime import datetime
from typing import List, Dict, Optional


class SQLiteDatabase:
    """
    SQLite-based database handler for storing and retrieving math operations.
    """

    def __init__(self, db_path: str = "math_ops.db") -> None:
        self.db_path = db_path
        self.conn = sqlite3.connect(self.db_path, check_same_thread=False)
        self.cursor = self.conn.cursor()
        self._create_table()

    def _create_table(self) -> None:
        """
        Creates the operations table if it doesn't already exist.
        """
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS operations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                operation TEXT NOT NULL,
                x INTEGER NOT NULL,
                y INTEGER,
                result INTEGER NOT NULL,
                timestamp TEXT NOT NULL
            )
        """)
        self.conn.commit()

    def save_operation(self, op: str, x: int, y: Optional[int], result: int) -> None:
        """
        Saves a new math operation into the database.

        Args:
            op: Type of operation (e.g. 'power', 'fibonacci')
            x: First input value
            y: Optional second input value
            result: Result of the operation
        """
        timestamp = datetime.utcnow().isoformat()
        self.cursor.execute("""
            INSERT INTO operations (operation, x, y, result, timestamp)
            VALUES (?, ?, ?, ?, ?)
        """, (op, x, y, result, timestamp))
        self.conn.commit()

    def get_all_operations(self) -> List[Dict[str, object]]:
        """
        Retrieves all operations from the database in reverse chronological order.

        Returns:
            A list of dictionaries representing each operation.
        """
        self.cursor.execute("""
            SELECT operation, x, y, result, timestamp
            FROM operations
            ORDER BY timestamp DESC
        """)
        rows = self.cursor.fetchall()

        return [
            {
                "operation": row[0],
                "x": row[1],
                "y": row[2],
                "result": row[3],
                "timestamp": row[4]
            }
            for row in rows
        ]
