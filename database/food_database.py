import sqlite3

class DishesDatabase:
    def __init__(self, path: str):
        self.path = path

    def create_dishes_table(self):
        with sqlite3.connect(self.path) as conn:
            curs = conn.cursor()
            curs.execute("""
            CREATE TABLE IF NOT EXISTS dishes(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            food_name TEXT NOT NULL,
            description TEXT,
            price REAL NOT NULL)
            """)
            conn.commit()

    def execute(self, query: str, params: tuple):
        with sqlite3.connect(self.path) as conn:
            conn.execute(query, params)
            conn.commit()