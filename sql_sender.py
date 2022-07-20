import sqlite3
from os import getenv
from dotenv import load_dotenv
load_dotenv()


con = sqlite3.connect(getenv("DB_FILE"))
cur = con.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS products(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        price INTEGER)
    """)

cur.execute(f"INSERT INTO products (name, price) VALUES ('book', 30)")
cur.execute(f"INSERT INTO products (name, price) VALUES ('movie', 64)")
cur.execute(f"INSERT INTO products (name, price) VALUES ('lemon', 4)")
cur.execute(f"INSERT INTO products (name, price) VALUES ('glasses', 16)")
cur.execute(f"INSERT INTO products (name, price) VALUES ('burger', 9)")
cur.execute(f"INSERT INTO products (name, price) VALUES ('hat', 32)")
cur.execute(f"INSERT INTO products (name, price) VALUES ('bag', 15)")

con.commit()