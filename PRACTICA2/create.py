import connection as db

def create():
    sql = '''INSERT into moviles VALUES ("xiaomi", "note 9", 128, 6)'''

    db.connection.execute(sql)

    db.conn.commit()

    print("Añadido correctamente")

# prints imaginarios porque no hay capturas