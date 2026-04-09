import sqlite3

def initialize_db():
    connection = sqlite3.connect("expanses.db")

    cur = sqlite3.cursor()

    cur.execute(
    """
    CREATE TABLE IF NOT EXISTS expanses(
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    date DATE, 
    description TEXT,
    amount INTEGER NOT NULL
    )
    """)

    conn.commit
    con.close


