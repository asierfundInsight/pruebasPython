#importacion del modulo
import psycopg2


#codciclo="BBB"
#denciclo="INSERT POR VARIABLE"
#grado="PRUEBA2"
try:
    #conexion BBDD
    conexion=psycopg2.connect(user='postgres',password='postgres',host='127.0.0.1',port='5432',database='postgres')

    # utilizar cursor
    cursor=conexion.cursor()

    # preguntar por consola los datos
    codCiclo=input("INTRODUZCA un (CODIGO CICLO) 4 caracteres max: ")
    denCiclo=input("INTRODUZCA un (DESCRIPCION CICLO): ")
    grado=input("INTRODUZCA un (GRADO) 8 caracteres max: ")
    
    # agrupo los 3 datos en una tuple(se identifica como tuple automaticamente)    
    datoInsert = codCiclo,denCiclo,grado
    
    # creo el insert y el select para moficar datos y verlo
    insert = f"""INSERT INTO ciclo VALUES{datoInsert};"""
    sql3='Select * from ciclo;'

    # utiliza metodo execute
    cursor.execute(insert) 
    cursor.execute(sql3)
    
    #guardar cambios
    conexion.commit()

    # mostrar resultado
    registro=cursor.fetchall()

    for ciclo in registro:
        print(ciclo)
    
    cursor.execute(sql3)
    
except(Exception,psycopg2.Error) as error:
    print("Error while fetching data from PostgreSQL", error)

finally:
    # closing database connection.
    if conexion:
        # cerrar conexion
        cursor.close()
        conexion.close()
        print("PostgreSQL connection is closed")