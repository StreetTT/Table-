import mysql.connector as sql
from os import environ as os


def SQLCommand(command, transaction=False):
    db_name = "Table-"
    config = {"host": os.get("HOST"),
              "user": os.get("TABLEMINUS_DB_USER"),
              "password": os.get("TABLEMINUS_DB_PASS")}
    conn = sql.connect(**config)
    c = conn.cursor()
    c.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
    config.update({"database": db_name})
    conn = sql.connect(**config)
    c = conn.cursor()
    if transaction:
        command = "BEGIN TRANSACTION;" + command + ";COMMIT;"
    c.execute(command)
    data = c.fetchall()
    conn.commit()
    conn.close()
    output = []
    if not data:
        return
    else:
        for i in data:
            if len(i) > 1:
                output.append(i[:-1])
            else:
                output.append(i[0])
        return output

SQLCommand("""SHOW TABLES""")