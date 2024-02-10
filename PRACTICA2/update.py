import connection as db

def update(id, col, value):
    sql = f'''UPDATE moviles SET {col} = '{value}' WHERE id = {id}'''

    db.connection.execute(sql)

    db.conn.commit()

    print(f"Modificado correctamente. Nuevo valor de {col}: {value}")