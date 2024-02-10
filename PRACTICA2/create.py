import connection as db

def create(marca, modelo, almacenamiento, ram):
    sql = f'''INSERT INTO moviles (marca, modelo, almacenamiento, ram) 
            VALUES ('{marca}', '{modelo}', {almacenamiento}, {ram})'''

    db.connection.execute(sql)

    db.conn.commit()

create("samsung", "galaxy z", 256, 8)