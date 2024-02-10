import connection as db

def read():
    sql = '''SELECT * FROM moviles'''

    db.connection.execute(sql)

    db.conn.commit()

# funciona, pero no se ve, al menos no hasta que haga el main