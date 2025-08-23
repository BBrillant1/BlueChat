import sqlite3
from datetime import datetime
class Database:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file, check_same_thread=False)
        self.create_tables()
    def create_tables(self):
        c = self.conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS messages(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        sender TEXT,
                        message TEXT,
                        timestamp TEXT)''')
        c.execute('''CREATE TABLE IF NOT EXISTS drafts(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        message TEXT,
                        timestamp TEXT)''')
        self.conn.commit()
    def save_message(self, sender, message):
        c = self.conn.cursor()
        c.execute("INSERT INTO messages (sender, message, timestamp) VALUES (?, ?, ?)",
                  (sender, message, datetime.now().isoformat()))
        self.conn.commit()
    def save_draft(self, message):
        c = self.conn.cursor()
        c.execute("INSERT INTO drafts (message, timestamp) VALUES (?, ?)",
                  (message, datetime.now().isoformat()))
        self.conn.commit()