import sqlite3


class Database:
    def __init__(self, path: str):
        self.path = path

    def create_table(self):
        with sqlite3.connect(self.path) as conn:
            conn.execute("""
            CREATE TABLE IF NOT EXISTS review(
                id INTEGER PRIMARY KEY,
                name TEXT,
                phone_number TEXT,
                visit_date DATE,
                food_rating INTEGER,
                cleanliness_rating INTEGER,
                extra_comments TEXT
            )
            """)

            conn.execute("""
            CREATE TABLE IF NOT EXISTS dishes(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            food_name TEXT NOT NULL,
            description TEXT,
            price INTEGER NOT NULL)
            """)
            conn.commit()

    def execute(self, query: str, params: tuple):
        with sqlite3.connect(self.path) as conn:
            conn.execute(query, params)
            conn.commit()

    def execute1(self, query: str, params: tuple = ()):
        with sqlite3.connect(self.path) as conn:
            cursor = conn.execute(query, params)
            conn.commit()
            return cursor
