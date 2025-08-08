import sqlite3
from typing import Any


def fetch_all_operations(db_path: str = "math_ops.db") -> None:
    """
    Connects to the SQLite database and prints all rows from the operations table.
    """
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM operations")
        rows = cursor.fetchall()

        print(f"Found {len(rows)} operation(s):\n")

        for row in rows:
            print(f"ID: {row[0]}, Operation: {row[1]}, x: {row[2]}, y: {row[3]}, "
                  f"Result: {row[4]}, Timestamp: {row[5]}")

    except sqlite3.Error as e:
        print(f"[ERROR] SQLite error: {e}")

    finally:
        if conn:
            conn.close()


if __name__ == "__main__":
    fetch_all_operations()
