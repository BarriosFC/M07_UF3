import connection as db

def read():
    sql = '''SELECT * FROM moviles'''

    db.connection.execute(sql)

    db.conn.commit()

    rows = db.connection.fetchall()

    if len(rows) == 0:
        print("No hay registros")
    else:
        for row in rows:
            print(row)