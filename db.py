import sqlite3
from sys import argv
from os import getenv
from dotenv import load_dotenv
load_dotenv()


class Database:
    def __init__(self, db_name):
        self.db_name = db_name
        self.con = sqlite3.connect(db_name)
        self.cur = self.con.cursor()

    def __repr__(self):
        return self.db_name

    def close(self):
        self.con.close()

    def delete_table(self, table_name):
        self.cur.execute(f"DROP TABLE {table_name}")

    def create_table(self, table_name, *data):
        self.cur.execute(f"""
            CREATE TABLE IF NOT EXISTS {table_name}(
                {','.join([d for d in data])}
            )
        """)
        self.con.commit()

    def insert_data(self, table_name, *data):
        self.cur.execute(f"""
            INSERT INTO {table_name}
            VALUES(
                {','.join(['?' for _ in data])}
            )
        """, data)
        self.con.commit()

    def delete_single_record(self, table_name, _id):
        self.cur.execute(f"""
            DELETE FROM {table_name}
            WHERE ID={_id}
        """)
        self.con.commit()

    def delete_multiple_record(self, table_name, ids):
        self.cur.executemany(f"""
            DELETE FROM {table_name}
            WHERE ID=?
        """, ids)

    def row_counter(self, table_name):
        self.cur.execute(F"""
            SELECT COUNT(*)
            FROM {table_name}
        """)
        return self.cur.fetchall()