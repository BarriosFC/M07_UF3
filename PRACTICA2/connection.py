import psycopg2

conn = psycopg2.connect(
    database='m7_uf3',
    user='postgres',
    password='postgres',
    host='localhost',
    port='5432'
)

connection = conn.cursor()

print(connection)

# ahora si que funciona. 
# estoy usando postgres modo consola, sin interfaz gráfica
# las capturas serán del modo consola