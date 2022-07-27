from sys import argv
from db import Database
from os import getenv
import sqlite3


def main():

    def data_wrapper() -> list:
        dataset = []
        while True:
            try:
                data = input("""
                put 'name' 'type' for create data
                OR
                put 'exit()' for leave
                """)
                if data != "exit()":
                    dataset.append(data)
                    print(f"\nadded {data}")
                    continue
                break
            except Exception as e:
                print(e)      
        return dataset


    if argv[1] == "create-table" and argv[2]:
        table_name = argv[2]
        data = data_wrapper()
        db = Database(getenv(("DB_FILE")))
        db.create_table(table_name, *data)
        print(f"table {table_name!r} created")


    if argv[1] == "delete-table" and argv[2]:
        table_name = argv[2]
        db = Database(getenv("DB_FILE"))
        db.delete_table(table_name)
        print(f"table {table_name!r} deleted")
       

    if argv[1] == "display-data" and argv[2]:
        table_name = argv[2]
        db = Database(getenv("DB_FILE"))
        db_content = db.col_counter(table_name)
        for data in db_content:
            print(data)


    if (
        argv[1] == "insert-data"
        and argv[2]
    ):
        table_name = argv[2]
        data = data_wrapper()
        db = Database(getenv("DB_FILE"))
        db.insert_data(table_name, None, *data)
        print(f"added data to {table_name!r}")


    if (
        argv[1] == "delete-record"
        and argv[2]
        and argv[3]
    ):
        table_name = argv[2]
        _id = argv[3]
        db = Database(getenv("DB_FILE"))
        db.delete_single_record(table_name, _id)
        print(f"deleted data from {table_name!r}")
    
    if (
        argv[1] == "--delete-record"
        and argv[2]
        and argv[3]
        and len(argv) > 3
    ): 
        table_name = argv[2]
        ids = []
        for i in range(3, len(argv)):
            ids.append(argv[i])
        db = Database(getenv("DB_FILE"))
        db.delete_multiple_record(table_name, ids)
        print(f"deleted data from {table_name!r}")


    if argv[1] == "drc" and argv[2]:
        table_name = argv[2]
        db = Database(getenv("DB_FILE"))
        drc = db.row_counter(table_name)
        for all_rows in drc:
            for r in all_rows:
                print(f"the number of rows in {table_name!r} table is {r}")

        
if __name__ == "__main__":
    main()