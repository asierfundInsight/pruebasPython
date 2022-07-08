#importacion del modulo
import psycopg2


#codciclo="BBB"
#denciclo="INSERT POR VARIABLE"
#grado="PRUEBA2"

def selectCiclo():

    sql="SELECT * from ciclo"

    cursor.execute(sql)

    conexion.commit()

    registro=cursor.fetchall()
    for ciclo in registro:
        print(ciclo)
#_______________________________

def insertarNuevo():

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
#____________________________________________________________________________________

def updateCiclo():

    sql1="select codciclo from ciclo;"
    cursor.execute(sql1)
    registro=cursor.fetchall()
    for ciclo in registro:
        print("existentes: ",ciclo)


    codCiclo=input("INTRODUZCA un CODIGO DE CICLO EXISTENTE:  ")
    codCicloNuevo=input("INTRODUZCA un CODIGO DE CICLO NUEVO PARA ACTUALIZAR:  ")


    datosTeclado = f"""'{codCiclo}'"""
    datosTeclado2 = f"""'{codCicloNuevo}'"""
    update=f"""update ciclo set codciclo ={datosTeclado2} where codciclo ={datosTeclado};"""

    cursor.execute(update)
    cursor.execute(sql1)

    conexion.commit()

    registro=cursor.fetchall()
    for ciclo in registro:
        print("actualizados: ",ciclo)

#____________________________________________________________________________________

def eliminarCiclo():
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
#________________________________________________________________________________

try:
    #conexion BBDD
    conexion=psycopg2.connect(user='postgres',password='postgres',host='127.0.0.1',port='5432',database='postgres')
    
   # utilizar cursor
    cursor=conexion.cursor()

    def seleccion(argument):
        switcher = {
            "0": "SELECT",
            "1": "INSERT",
            "2": "UPDATE",
            "3": "DELETE",
        }
        return switcher.get(argument, "INDICA un NÚMERO ENTRE 0-3")
    print("-----------")

    seguir = 'y'
    while seguir != ('n' or 'N'):
        # nos pide por teclado la opcion solamente si seguir es =y o Y, en caso de ser N cierra el programa

        argument=input("indique que opción quiere: \n 0-SELECT\n 1-INSERT\n 2-UPDATE\n 3-DELETE\n --elegiste: ")

        if argument=="0":
            print("-----------")
            selectCiclo()
            print(" ")
            seguir=input("DESEA CONTINUAR ?-- INDIQUE Y/y para seguir o N/n para salir:  ")
            print("-----------")
        elif argument=="1":
            print("-----------")
            insertarNuevo()
            seguir=input("DESEA CONTINUAR ?-- INDIQUE Y/y para seguir o N/n para salir:  ")
            print("-----------")
        elif argument=="2":
            print("-----------")
            print(" ")
            updateCiclo()
            seguir=input("DESEA CONTINUAR ?-- INDIQUE Y/y para seguir o N/n para salir:  ")
            print("-----------")
        elif argument=="3":
            print("-----------")
            eliminarCiclo()
            seguir=input("DESEA CONTINUAR ?-- INDIQUE Y/y para seguir o N/n para salir:  ")
            print("-----------")
        else:
            print("\n-------ERROR, debe indique un valor entre 0-3------- ") 
            argument=input("indique que opción quiere VALOR NUMERICO: \n 0-SELECT\n 1-INSERT\n 2-UPDATE\n 3-DELETE\n --elegiste: ")
            print("-----------")                
            
    
except(Exception,psycopg2.Error) as error:
    print("Error Except: ", error)

finally:
    # closing database connection.
    if conexion:
        # cerrar conexion
        cursor.close()
        conexion.close()
        print("PostgreSQL connection is closed")

