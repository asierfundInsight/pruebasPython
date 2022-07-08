#importacion del modulo
import psycopg2


try:
    #conexion BBDD
    conexion=psycopg2.connect(user='postgres',password='postgres',host='127.0.0.1',port='5432',database='postgres')

    # utilizar cursor
    cursor=conexion.cursor()

    # crear sentencia SQL
    update="update emp set ename ='ASIER' where ename ='Asier';"
    sql="Select 'departamento: ',deptno , ename, job, sal, empno from emp order by deptno;"
    sql1='Select deptno, ename, job, sal, empno from emp order by deptno;'
    sql2='Select deptno , ename, job, sal, empno from emp where empno=7934;'

    # utiliza metodo execute
    cursor.execute(update) 
    cursor.execute(sql)
    

    #guardar cambios
    conexion.commit()


    # mostrar resultado
    registro=cursor.fetchall()

    for empleado in registro:
        print(empleado)
    
    cursor.execute(sql2)
    verEmpleado=cursor.fetchall()
    print("\nNUEVO EMPLEADO: ", verEmpleado,"\n")

    
except(Exception,psycopg2.Error) as error:
    print("Error while fetching data from PostgreSQL", error)

finally:
    # closing database connection.
    if conexion:
        # cerrar conexion
        cursor.close()
        conexion.close()
        print("PostgreSQL connection is closed")