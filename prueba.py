#importacion del modulo
import psycopg2

#conexion BBDD
conexion=psycopg2.connect(user='postgres',password='postgres',host='127.0.0.1',port='5432',database='postgres')
# utilizar cursor
cursor=conexion.cursor()

# crear sentencia SQL
sql='Select * from emp where empno=7934;'

# utiliza metodo execute
cursor.execute(sql)

# mostrar resultado
registro=cursor.fetchall()

for empleado in registro:
    print(empleado)

# cerrar conexion
cursor.close()
conexion.close()