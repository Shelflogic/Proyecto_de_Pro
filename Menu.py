from Funciones import crear_inventario
from Funciones import guardar_evento_cliente
import json




def menu(posible_inventario, varios_inventarios, dic_clientes):
    check = True
    print ("")
    while check:
        print ("Seleccioe una opcion:\n    1- para anadir una nueva empresa\n    2- contratar empresa\n    3- ver empresas disponibles\n    4- ver eventos\n    5- cancelar eventos\n    6- eliminar un inventario de una empresa (SOLO si este no va a ser rentado)\n    7- Para ver detalles de un evento en especifico\n    8- salir")
        seleccionador = input()














        if seleccionador == "1":
            print ("")
            try:
                with open('inventarios.json', 'r', encoding='utf-8') as f:
                    azul = crear_inventario(posible_inventario, json.load(f))
                    with open('inventarios.json', 'w', encoding='utf-8') as archivo:
                        json.dump(azul, archivo, ensure_ascii=False, indent=2)
                        check = False
                
            except:
                with open('inventarios.json', 'w', encoding='utf-8') as archivo:
                    json.dump(crear_inventario(posible_inventario, varios_inventarios), archivo, ensure_ascii=False, indent=2)
                    check = False
            # except json.JSONDecodeError:
            #     print("Error: JSON inválido")
            #     check = False













            
        elif seleccionador == "2":
            print ("")
            try:
                with open('inventarios.json', 'r', encoding='utf-8') as f:
                    dic_empresas = json.load(f)
                    print("Empresas disponibles:\n")
                    for i in dic_empresas:
                        print(i)
                        print("")
                    if dic_empresas is None:
                        print("Aun no hay empresas disponibles")
                        break
                    if len(dic_empresas) == 0:
                        print("Aun no hay empresas disponibles")
                        break

            except FileNotFoundError:
                print("Aun no hay empresas disponibles")
                check = False

            try:
                with open('clientes.json', 'r', encoding='utf-8') as g:
                    azul = guardar_evento_cliente(dic_empresas, json.load(g))

                    with open('clientes.json', 'w', encoding='utf-8') as archivo:
                        json.dump(azul, archivo, ensure_ascii=False, indent=2)
                        check = False

            except:
                    with open('clientes.json', 'w', encoding='utf-8') as archivo:
                        json.dump(guardar_evento_cliente(dic_empresas, dic_clientes), archivo, ensure_ascii=False, indent=2)
                        check = False
                











            
        elif seleccionador == "8":
            raise SystemExit
        









        
        elif seleccionador == "3":
            with open('inventarios.json', 'r', encoding='utf-8') as f:
                contenido = json.load(f)
            if contenido == {}:
                print("")
                print("Aun no hay empresas disponibles")
                break
            if contenido is None:    
                print("Aun no hay empresas disponibles")
                break
            if len(contenido) == 0:
                print("")
                print("Aun no hay empresas disponibles")
            else:    
                for i in contenido:
                    print(f"\n{i} : ")
                    for j in contenido[i]:
                        print(f"{j} : {contenido[i][j]}")
            check = False
        














        elif seleccionador == "4":
            with open('clientes.json', 'r', encoding='utf-8') as f:
                contenido = json.load(f)
            if contenido == {}:
                print("")
                print("Aun no hay eventos programados")
                break
            if contenido is None:    
                print("")
                print("Aun no hay eventos programados")   
                break            
            if len(contenido) == 0:
                print("")
                print("Aun no hay eventos programados")
                break
            else:    
                for element in contenido:
                            print(f"\n{element}:")
                            for i in contenido[element]:
                                print(f"{i}:")
                                for j in contenido[element][i]:
                                    print(f"{j} : {contenido[element][i][j]}")
                            check = False
            check = False
















        elif seleccionador == "5":
            try:
                with open('clientes.json', 'r', encoding='utf-8') as f:
                    dic = json.load(f)
                if dic is None:
                    print("No hay eventos programados")
                    break
                if dic == {}:
                    print("No hay eventos programados")
                    break
            except:
                print("No hay eventos programados")
            print("Escriba el numero asignado al evento que desea eliminar\nEscriba atras, para cancelar operacion")
            ver_evento_cliente = input()
            if ver_evento_cliente == "atras":
                break
            ver_evento_cliente = "evento_" + ver_evento_cliente
            if ver_evento_cliente not in dic:
                print("Numero asignado de evento incorrecto")
            else:
                    del dic[ver_evento_cliente]

                    with open('clientes.json', 'w', encoding='utf-8') as archivo:
                        json.dump(dic, archivo, ensure_ascii=False, indent=2)
                    print("Evento eliminado correctamente")

                    with open('lista_asignacion.json', 'r', encoding='utf-8') as f:
                        lista = json.load(f)
                        lista.remove(int(ver_evento_cliente[-1::]))
                    with open('lista_asignacion.json', 'w', encoding='utf-8') as g:
                        json.dump(lista, g, ensure_ascii=False, indent=2)
            check = False















        elif seleccionador == "6":
            print("Escriba el nombre de la empresa de la cual desea eliminar el inventario\nEscriba atras, para cancelar operacion")
            eliminar = input()
            if eliminar == "atras":
                break
            try:    
                with open('inventarios.json', 'r', encoding='utf-8') as f:
                    dic = json.load(f)
                    if eliminar in dic:
                        with open('clientes.json', 'r', encoding='utf-8') as g:
                            client = json.load(g)
                            if client is None:
                                del [dic[eliminar]]
                                with open('inventarios.json', 'w', encoding='utf-8') as archivo:
                                    json.dump(dic, archivo, ensure_ascii=False, indent=2)
                                print(f"inventario {eliminar} eliminado correctamente")
                                break
                            elif client == {}:
                                del [dic[eliminar]]
                                with open('inventarios.json', 'w', encoding='utf-8') as archivo:
                                    json.dump(dic, archivo, ensure_ascii=False, indent=2)
                                print(f"inventario {eliminar} eliminado correctamente")
                                break
                            else:
                                for i in client:
                                    for j in client[i]:
                                        if j == eliminar:
                                            print("\nNo es posible eliminar este inventario. Un cliente tiene programado rentarlo\n")                                
                                            check = False
                                            break
                        if check == True:               
                            del [dic[eliminar]]
                            with open('inventarios.json', 'w', encoding='utf-8') as archivo:
                                json.dump(dic, archivo, ensure_ascii=False, indent=2)
                            print(f"inventario {eliminar} eliminado correctamente")
                        
                    else:
                        print("El nombre de esa empresa no esta registrado")

            except:
                print("No hay inventarios aun que eliminar")


            check = False










        elif seleccionador == "7":
            while check:
                try:
                    with open('clientes.json', 'r', encoding='utf-8') as f:
                        evento = json.load(f)
                        if evento == {}:
                            print("No hay evntos disponibles")
                            break
                        if evento == None:
                            print("No hay evntos disponibles")
                            break
                        print("Escriba el numero del evento asignado\nEscriba atras para cancelar la operacion")
                        ver_evento = input()
                        if ver_evento == "atras":
                            break
                        ver_evento = "evento_" + ver_evento
                        if ver_evento in evento:
                            print(f"\n{ver_evento}:")
                            for i in evento[ver_evento]:
                                print(f"{i}:")
                                for j in evento[ver_evento][i]:
                                    print(f"{j} : {evento[ver_evento][i][j]}")
                            check = False
                        else:
                            print("Numero de evento invalido")
                            break
                except:
                    print("No hay evntos disponibles")
                    break











        else: 
            check = True
    menu(posible_inventario, varios_inventarios, dic_clientes)












            