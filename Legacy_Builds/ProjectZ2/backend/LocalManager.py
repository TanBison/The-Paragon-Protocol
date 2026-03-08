import sqlite3
import json
from datetime import datetime


class LocalManager:
    def __init__(self, db_name="project_z.db"):
        self.db_name = db_name
        self._create_table()

    def _create_table(self):
        """Creates the 'history' table if it doesn't exist."""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        # We save high-level stats in their own columns for easy sorting/graphing.
        # We save the complex dictionary in 'details' as a JSON string.
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT,
                duration_seconds INTEGER,
                score_percent REAL,
                total_reps INTEGER,
                details TEXT
            )
        ''')
        conn.commit()
        conn.close()

    def save_workout(self, workout_data, duration, score, total_reps):
        """Saves a new workout entry to the database."""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        # 1. Get Current Time
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # 2. Convert the Dictionary to a JSON String
        # This preserves all your sets, reps, and rest times exactly as they are.
        data_as_string = json.dumps(workout_data)

        # 3. Insert into Database
        cursor.execute('''
            INSERT INTO history (date, duration_seconds, score_percent, total_reps, details)
            VALUES (?, ?, ?, ?, ?)
        ''', (timestamp, duration, score, total_reps, data_as_string))

        conn.commit()
        conn.close()
        print(f"--- [LocalManager] Saved Workout to {self.db_name} ---")

    def delete_workout(self, workout_id):
        """Deletes a single workout by its ID."""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM history WHERE id = ?", (workout_id,))
        conn.commit()
        conn.close()
        print(f"--- [LocalManager] Deleted Workout ID: {workout_id} ---")