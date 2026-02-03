import json
from datetime import datetime
import copy



def crear_inventario (posible_inventario, varios_inventarios):
    for element in posible_inventario:
        print (element)

    nombre = input("\nescriba el nombre de su empresa\n")
    varios_inventarios[nombre] = {}

    print ("")
    for element in posible_inventario:
        check = True
        while check:
            print (f"seleccione la cantidad de {element} que posee")
            varios_inventarios[nombre][element] = input()
            try:
                varios_inventarios[nombre][element] = int(varios_inventarios[nombre][element])
                check = False
            except ValueError:
                check = True
        if varios_inventarios[nombre][element] <= 0:
            del varios_inventarios[nombre][element]

    
    # print ("")
    # print(f"{nombre} :\n")
    # for i in varios_inventarios[nombre].keys():
    #     print (f"{i} : {varios_inventarios[nombre][i]}")
    if varios_inventarios[nombre] == {}:
        return
    return varios_inventarios
    
    














#esta funcion, agrega un cliente al json clientes, o si el cliente ya ha retado recursos de una empresa, le permite al usuario rentar recursos
# de otra empresa simultaneamente    

def guardar_evento_cliente(dic_empresas, dic_cliente):
    
    while True:
        clientes_copy = copy.deepcopy(dic_cliente)
        empresas_copy = copy.deepcopy(dic_empresas)
        try:
            cliente = "evento_" + str(len(dic_cliente) + 1)
            print(f"Numero de evento asignado: {str(len(dic_cliente) + 1)}")
        except:
            cliente = "evento_1"
        print("Seleccione el nombre de la empresa que quiere contratar\n")
        empresa = input ()
        if empresa in empresas_copy:

            fecha = introducir_fechas()

            disponibilidad = comprobar_disponibilidad(clientes_copy, fecha, empresa, empresas_copy)

            empresas_copy[empresa] = disponibilidad

            if empresas_copy[empresa] == {}:
                print(f"La empresa {empresa}, no esta disponible durante el periodo de tiempo seleccionado")
                continue
            
            print(f"\nLa disponibilidad de los recursos para el periodo de tiempo seleccionado es:\n")
            for i in disponibilidad.keys():
                print (f"{i} : {disponibilidad[i]}")


            if cliente not in clientes_copy: #verifica si el usuario, ya ha rentado recursos de otra empresa, de no ser asi, se creara un diccionario vacio para almacenar los datos de cliente
                clientes_copy[cliente] = {}
            clientes_copy[cliente][empresa] = {}

            print("\nADVERTENCIA\n")
            print("Rentar al menos una consola de sonido implica tener que rentar al menos un ingeniero de sonido\n")
            print("Rentar al menos una consola de luces tradicionales, implicara no poder rentar un a consola de luces inteligentes\n")
            print("No rentar la consola de luces inteligente, implicara no poder rentar lues con efectos")
            for element in empresas_copy[empresa]:#este for espara pasar por cada recurso de la empresa seleccionada, y que el cliente seleccione la cantidad del recurso que desea rentar
                if element == "consola de luces inteligente": #aqui se comprueba la segunda restriccion
                    if "consola de luces tradicionales" in clientes_copy[cliente][empresa]:
                        continue
                if element == "luces con efectos":#aqui e comprueba la tercera restriccion
                    if "consola de luces inteligente" not in clientes_copy[cliente][empresa]:
                        continue
                check = True
                while check:
                    print (f"\nEscriba la cantidad de {element} que desea rentar. ({empresas_copy[empresa][element]} disponible)")
                    print("Escriba 'atras' para cancelar la operacion\n")
                    clientes_copy[cliente][empresa][element] = input()
                    if clientes_copy[cliente][empresa][element] == "atras":
                        check = False
                    try:
                        clientes_copy[cliente][empresa][element] = int(clientes_copy[cliente][empresa][element])

                        if clientes_copy[cliente][empresa][element] > empresas_copy[empresa][element]:
                            print (f"La cantidad solicitada no esta disponible\n")
                            del clientes_copy[cliente][empresa][element]
                            continue
                        
                    except ValueError:
                        continue

#se guarda la cantidad de recursos que el cliente solicita en un diccionario
                    
                    if element == "ingenieros de sonido":#aqui se comprueba la primera restriccion
                        if "consolas de sonido" in clientes_copy[cliente][empresa]:
                            if clientes_copy[cliente][empresa][element] < 1:
                                print("\nDebe rentar al menos un ingeniero de sonido\n")
                                continue

                    check = False

                if clientes_copy[cliente][empresa][element] == "atras":
                    break
                if clientes_copy[cliente][empresa][element] <= 0:#si el cliente quiere una cantidad <=0, no se tendra en cuenta
                    del clientes_copy[cliente][empresa][element]
            if clientes_copy[cliente][empresa][element] == "atras":
                break
            clientes_copy[cliente][empresa]["periodo"] = fecha
            return clientes_copy

        elif empresa not in empresas_copy:
                    print("El nombre de esa empresa no fue encotrado\n")
                    continue
        
















def introducir_fechas():
    while True:
        print("Escrba la fecha de inicio de su evento (dia, mes, ano, de la forma DD, MM, YYYY), separado por '-' :")
        inicio = input()
        print("Escrba la fecha de fin de su evento (dia, mes, ano, de la forma DD, MM, YYYY), separado por '-' :")
        fin = input()


        try:
            inicio = datetime.strptime(inicio,"%d-%m-%Y")
            fin = datetime.strptime(fin,"%d-%m-%Y")
        except:
            print("Fecha invalida")
            continue
        
        if inicio > fin:
            print("la fecha de inicio es posterior a la fecha de fin")
        else:
            break            
    inicio = str(inicio)
    fin = str(fin)
    periodo = {"fecha de inicio" : inicio, "fecha de fin" : fin}

    return periodo
















def comprobar_disponibilidad(dic_cliente, fecha, empresa, dic_empresas):
    for cliente in dic_cliente.keys():
        if empresa in dic_cliente[cliente].keys():
            if datetime.strptime((fecha["fecha de fin"]),"%Y-%m-%d %H:%M:%S") < datetime.strptime(dic_cliente[cliente][empresa]["periodo"]["fecha de inicio"],"%Y-%m-%d %H:%M:%S"):
                continue
            if datetime.strptime(fecha["fecha de inicio"],"%Y-%m-%d %H:%M:%S") > datetime.strptime(dic_cliente[cliente][empresa]["periodo"]["fecha de fin"],"%Y-%m-%d %H:%M:%S"):
                continue
            else:
                for j in dic_cliente[cliente][empresa].keys():
                    if j == "periodo":
                        continue
                    dic_empresas[empresa][j] -= dic_cliente[cliente][empresa][j]
                    if dic_empresas[empresa][j] == 0:
                        del dic_empresas[empresa][j]

    return dic_empresas[empresa]