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
                visit_date DATA,
                food_rating INTEGER,
                cleanliness_rating INTEGER,
                extra_comments TEXT
            )
            """)
            conn.commit()

    def execute(self, query: str, params: tuple):
        with sqlite3.connect(self.path) as conn:
            conn.execute(query, params)
            conn.commit()