import json
from datetime import datetime
import copy



def crear_inventario (posible_inventario, varios_inventarios):
    while True:
        for element in posible_inventario:
            print (element)
        while True:
            nombre = input("\nEscriba el nombre de su empresa\n")
            if nombre in varios_inventarios:
                print("\nEl nombre introducido ya esta ocupado\n")
                continue
            varios_inventarios[nombre] = {}
            break
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
        
        if varios_inventarios[nombre] == {}:
            del varios_inventarios[nombre]

        print("\nTodos los datos correctos?\nEscriba si para guardar el evento, escriba cualquier otra cosa para reiniciar la operacion\n")
        fin = input()
        if fin == "si":
            return varios_inventarios
        else:
            del varios_inventarios[nombre]
            continue
    














#esta funcion, agrega un cliente al json clientes, o si el cliente ya ha retado recursos de una empresa, le permite al usuario rentar recursos
# de otra empresa simultaneamente    

def guardar_evento_cliente(dic_empresas, dic_cliente):
    
    try:
        with open('lista_asignacion.json', 'r', encoding='utf-8') as f:
            lista = json.load(f)
            cliente = "evento_" + str(comprobar_asignacion_evento(lista))
            print(f"Numero de evento asignado: {cliente[-1::]}")
            with open('lista_asignacion.json', 'w', encoding='utf-8') as g:
                json.dump(lista, g, ensure_ascii=False, indent=2)

    except:
        with open('lista_asignacion.json', 'w', encoding='utf-8') as f:
            cliente = "evento_1"
            json.dump([1], f, ensure_ascii=False, indent=2)
            print("Numero de evento asignado: 1")

    while True:
        clientes_copy = copy.deepcopy(dic_cliente)
        empresas_copy = copy.deepcopy(dic_empresas)
        
        while True:
            print("Seleccione el nombre de la empresa que quiere contratar\n")
            empresa = input ()
            if empresa in empresas_copy:
                while True:
                    fecha = introducir_fechas()

                    clientes_copy = copy.deepcopy(dic_cliente)
                    empresas_copy = copy.deepcopy(dic_empresas)                 
                    
                    if clientes_copy is None or clientes_copy == {}:
                        clientes_copy = {}
                        print(f"\nLa disponibilidad de los recursos para el periodo de tiempo seleccionado es:\n")
                        for i in empresas_copy[empresa].keys():
                            print (f"{i} : {empresas_copy[empresa][i]}")
                        break
                    else:
                        disponibilidad = comprobar_disponibilidad(clientes_copy, fecha, empresa, empresas_copy)
                        print(f"\nLa disponibilidad de los recursos para el periodo de tiempo seleccionado es:\n")
                        for i in disponibilidad.keys():
                            print (f"{i} : {disponibilidad[i]}")
                        if dic_empresas[empresa] != empresas_copy[empresa]:
                            completa_dispo = completa_disponibilidad(empresa, dic_cliente, fecha["fecha de inicio"], fecha["fecha de fin"])
                            print(f"\nLa empresa seleccionada estara completamente disponible durante ese mismo periodo de tiempo, desde {completa_dispo["fecha de inicio"]} {completa_dispo["fecha de fin"]}\n")
                            denuevo = input("\nQuiere seleccionar de nuevo la fecha de su evento?\nEscriba si, para confirmar, y cualquier otra cosa, para continuar\n")
                            if denuevo == "si":
                                continue
                            else:
                                empresas_copy[empresa] = disponibilidad
                                break
                        else:
                            break

                # if empresas_copy[empresa] == {}:
                #     print(f"La empresa {empresa}, no esta disponible durante el periodo de tiempo seleccionado")
                #     continue
                
            

                # if cliente not in clientes_copy: #verifica si el usuario, ya ha rentado recursos de otra empresa, de no ser asi, se creara un diccionario vacio para almacenar los datos de cliente
                clientes_copy[cliente] = {}
                clientes_copy[cliente][empresa] = {}

                print("\nADVERTENCIA\n")
                print("Rentar al menos una consola de sonido implica tener que rentar al menos un ingeniero de sonido\n")
                print("Rentar al menos una consola de luces tradicionales, implicara no poder rentar un a consola de luces inteligentes\n")
                print("No rentar la consola de luces inteligente, implicara no poder rentar luces con efectos")
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
                        clientes_copy[cliente][empresa][element] = input()
                        try:
                            clientes_copy[cliente][empresa][element] = int(clientes_copy[cliente][empresa][element])

                            if clientes_copy[cliente][empresa][element] > empresas_copy[empresa][element]:
                                print (f"La cantidad solicitada no esta disponible\n")
                                del clientes_copy[cliente][empresa][element]
                                continue
                            
                        except ValueError:
                            continue

                        
                        if element == "ingenieros de sonido":#aqui se comprueba la primera restriccion
                            if "consolas de sonido" in clientes_copy[cliente][empresa]:
                                if clientes_copy[cliente][empresa][element] < 1:
                                    print("\nDebe rentar al menos un ingeniero de sonido\n")
                                    continue

                        check = False
                        
                    if clientes_copy[cliente][empresa][element] <= 0:#si el cliente quiere una cantidad <=0, no se tendra en cuenta
                        del clientes_copy[cliente][empresa][element]

                clientes_copy[cliente][empresa]["periodo"] = fecha
                break

            elif empresa not in empresas_copy:
                        print("El nombre de esa empresa no fue encotrado\n")
                        continue
        print("\nTodos los datos correctos?\nEscriba si para guardar el evento, escriba cualquier otra cosa para reiniciar la operacion\n")
        fin = input()
        if fin == "si":
            return clientes_copy
        else:
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













def comprobar_asignacion_evento(lista):
    if lista is None or lista == {} or lista == []:
        lista.append(1)
        return 1
    count = 1
    while True:
        if count in lista:
            count += 1
            continue
        else:
            lista.insert(count - 1, count)
            return count
        










def completa_disponibilidad(empresa, dic_clientes, fecha_inicio, fecha_fin):
    clientes_copy = copy.deepcopy(dic_clientes)
    lista = []
    for i in clientes_copy:
        for j in clientes_copy[i]:
            if j != empresa:
                continue
            else:
                lista.append(clientes_copy[i][j]["periodo"])
    
    for i in range(0, len(lista)+1):
        for j in range(i, len(lista)):
            if datetime.strptime(lista[j]["fecha de inicio"],"%Y-%m-%d %H:%M:%S") < datetime.strptime(lista[i]["fecha de inicio"],"%Y-%m-%d %H:%M:%S"):
                lista[j], lista[i] = lista[i], lista[j]
            elif datetime.strptime(lista[j]["fecha de inicio"],"%Y-%m-%d %H:%M:%S") == datetime.strptime(lista[i]["fecha de inicio"],"%Y-%m-%d %H:%M:%S"):
                if datetime.strptime(lista[j]["fecha de fin"],"%Y-%m-%d %H:%M:%S") < datetime.strptime(lista[i]["fecha de fin"],"%Y-%m-%d %H:%M:%S"):
                    lista[j], lista[i] = lista[i], lista[j]
                    
    dias = datetime.strptime(fecha_fin,"%Y-%m-%d %H:%M:%S") - datetime.strptime(fecha_inicio,"%Y-%m-%d %H:%M:%S")
    periodo_disponible = {}
    for i in range(0, len(lista)+1):
        for j in range(i, len(lista)):
            if dias <= datetime.strptime(lista[j]["fecha de inicio"],"%Y-%m-%d %H:%M:%S") - datetime.strptime(lista[i]["fecha de fin"],"%Y-%m-%d %H:%M:%S"):
                periodo_disponible["fecha de inicio"] = lista[i]["fecha de fin"]
                periodo_disponible["fecha de fin"] = "hasta " + lista[j]["fecha de inicio"]
                return periodo_disponible
    
    periodo_disponible["fecha de inicio"] = lista[j]["fecha de fin"]
    periodo_disponible["fecha de fin"] = "en adelante"
    return periodo_disponible