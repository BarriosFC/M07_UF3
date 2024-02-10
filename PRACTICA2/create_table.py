import connection as db

def create_table():
    sql_drop = '''DROP TABLE IF EXISTS moviles'''

    sql_create = '''CREATE TABLE IF NOT EXISTS moviles(
                    id SERIAL PRIMARY KEY,
                    marca VARCHAR(255) NOT NULL,
                    modelo VARCHAR(255) NOT NULL,
                    almacenamiento BIGINT NOT NULL,
                    ram BIGINT NOT NULL
    )'''

    db.connection.execute(sql_drop)
    db.connection.execute(sql_create)

    db.conn.commit()

    print("Tabla creada correctamente")
