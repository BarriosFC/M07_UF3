import connection as db

def deleteById(id):
    sql = f'''DELETE FROM moviles WHERE id={id}'''

    db.connection.execute(sql)

    db.conn.commit()
