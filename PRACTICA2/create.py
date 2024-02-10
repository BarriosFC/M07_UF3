import connection as db

def create():
    sql = '''INSERT into public.moviles VALUES ( ,"xiaomi", "note 9", 128, 6)'''

    db.connection.execute(sql)

    db.conn.commit()

    print("Añadido correctamente")

create()