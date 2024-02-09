import connection as db

def create_table():
    sql = '''CREATE TABLE IF NOT EXISTS moviles(
                    id SERIAL PRIMARY KEY,
                    marca VARCHAR(255) NOT NULL,
                    modelo VARCHAR(255) NOT NULL,
                    almacenamiento BIGINT NOT NULL,
                    ram BIGINT NOT NULL
    )'''

    db.execute(sql)

    db.conn.commit()

    print("Tabla creada correctamente")

# prints imaginarios porque no hay capturas