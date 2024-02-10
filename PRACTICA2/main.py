import psycopg2
import connection as db
from create_table import *
from create import *
from read import *
from update import *
from delete import *

try:
    print("BBDD de Móviles. Que desea?")
    create_table()
    msg = '''1> Mirar listado
2> Añadir un registro
3> Editar un registro
4> Eliminar un registro
5> Eliminar Docker de la faz de la Tierra
6> Salir'''
    selector = 0

    while selector != 6:
        print(" ")
        print(msg)
        selector = int(input(">> "))
        print(" ")
        if selector == 1:
            print("ID   Marca   Modelo   Almacenamiento   Ram")
            read()
        elif selector == 2:
            print("Ingrese en orden: Marca Modelo Almacenamiento Ram")
            args = input(">> ")
            val = args.split(' ')
            create(val[0], val[1], int(val[2]), int(val[3]))
        elif selector == 3:
            print("Ingrese en orden: Id_a_modificar Campo_a_modificar Nuevo_valor")
            args = input(">> ")
            val = args.split(' ')
            if val[1] == "almacenamiento" or val[1] == "ram":
                val[2] = int(val[2])
            update(int(val[0]), val[1], val[2])
        elif selector == 4:
            print("Ingrese la ID a eliminar")
            args = int(input(">> "))
            deleteById(args)
        elif selector == 5:
            print("Todos odiamos Docker. Tiempo al tiempo, ya caerá")
    
    print("Gracias por usar nuestro servicio")
except (Exception, psycopg2.Error) as error:
    print("Error", error)
finally:
    db.conn.close()