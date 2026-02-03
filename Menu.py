from Funciones import crear_inventario
from Funciones import guardar_evento_cliente
from Funciones import introducir_fechas
import json




def menu(posible_inventario, varios_inventarios, dic_clientes):
    check = True
    print ("")
    while check:
        print ("Seleccioe una opcion:\n    1- para anadir una nueva empresa\n    2- contratar empresa\n    3- ver empresas disponibles\n    4- ver eventos\n    5- cancelar eventos\n    6- eliminar un inventario de una empresa (SOLO si este no va a ser rentado)\n    7- 'salir'")
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
                











            
        elif seleccionador == "7":
            raise SystemExit
        









        
        elif seleccionador == "3":
            with open('inventarios.json', 'r', encoding='utf-8') as f:
                contenido = f.read()
            if contenido == '{}':
                print("")
                print("Aun no hay empresas disponibles")
                break
            if contenido == 'null':    
                print("Aun no hay empresas disponibles")
                break
            if len(contenido) == 0:
                print("")
                print("Aun no hay empresas disponibles")
            else:    
                print(contenido)
            check = False
        














        elif seleccionador == "4":
            with open('clientes.json', 'r', encoding='utf-8') as f:
                contenido = f.read()
            if contenido == '{}':
                print("")
                print("Aun no hay eventos programados")
                break
            if contenido == 'null':    
                print("")
                print("Aun no hay eventos programados")   
                break            
            if len(contenido) == 0:
                print("")
                print("Aun no hay eventos programados")
                break
            else:    
                print(contenido)
            check = False
















        elif seleccionador == "5":
            print("Escriba el numero de evento asignado")
            eliminar_cliente = input()
            eliminar_cliente = "evento_" + eliminar_cliente
            try:
                with open('clientes.json', 'r', encoding='utf-8') as f:
                    dic = json.load(f)
                    if eliminar_cliente not in dic:
                        print("Numero de evento incorrecto")
                    else:
                            del dic[eliminar_cliente]

                            with open('clientes.json', 'w', encoding='utf-8') as archivo:
                                json.dump(dic, archivo, ensure_ascii=False, indent=2)
                            print("Evento eliminado correctamente")
                    check = False
            except:
                print("No hay eventos programados")















        elif seleccionador == "6":
            print("Escriba el nombre de la empresa de la cual desea eliminar el inventario\n")
            eliminar = input()
            try:    
                with open('inventarios.json', 'r', encoding='utf-8') as f:
                    dic = json.load(f)
                    if eliminar in dic:
                        with open('clientes.json', 'r', encoding='utf-8') as g:
                            client = json.load(g)
                            for i in client:
                                for j in client[i]:
                                    if j == eliminar:
                                        print("\nNo es posible eliminar este inventario. Un cliente tiene programado rentarlo\n")                                
                                        check = False
                        if check == True:               
                            del [dic[eliminar]]
                            with open('inventarios.json', 'w', encoding='utf-8') as archivo:
                                json.dump(dic, archivo, ensure_ascii=False, indent=2)
                            print(f"inventario {eliminar} eliminado correctamente")
                        
                    else:
                        print("El nombre de esa empresa no esta registrado")

            except FileNotFoundError:
                print("no hay inventarios aun que eliminar")


            check = False

        else: 
            check = True
    menu(posible_inventario, varios_inventarios, dic_clientes)