import sqlite3
from sqlite3 import Error


def create_connection(database):
    try:
        conn = sqlite3.connect(database, isolation_level=None, check_same_thread=False)
        conn.row_factory = lambda c, r: dict(zip([col[0] for col in c.description], r))

        return conn
    except Error as e:
        print(e)

def add_sale(c, data):
    sql = '''INSERT INTO sales(id,name,quantity,price,type)
                VALUES (?,?,?,?,?)'''
    c.execute(sql, data)

def select_sale(c, id):
    sql = '''SELECT * FROM sales where id = ?'''
    c.execute(sql, [id])
    rows = c.fetchall()
    return rows

def main():
    database = "./sales.db"
    conn = create_connection(database)
    if conn is not None:
        print("Connection established!")
    else:
        print("Connection not established!")

if __name__ == '__main__':
    main()
