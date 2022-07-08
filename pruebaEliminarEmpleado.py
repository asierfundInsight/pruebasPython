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
    codCiclo=input("INTRODUZCA un CODIGO DE CICLO PARA ELIMINAR:  ")
    

    datosTeclado = f"""'{codCiclo}'"""
    print(datosTeclado,"\n")
    
    # creo el select para ver la tabla y el delete para eliminar fila
    delete =f"""DELETE FROM ciclo where codciclo = {datosTeclado};"""
    sql3='Select * from ciclo;'

    # utiliza metodo execute
    cursor.execute(delete) 
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