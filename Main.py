from Menu import menu


posible_inventario = [ 
    "escenarios",
    "consolas de sonido",
    "lineas de sonido" ,
    "referencias",
    "microfonos",
    "torres de sonido",
    "ingenieros de sonido",
    "tecnicos de sonido",
    "consola de luces tradicionales",
    "consola de luces inteligente",
    "luces tradicionales",
    "luces con efectos",
    "ingeniero de luces",
    "tecnico de luces",
    "disenaor de escenario",
    "tramoyistas"
]

varios_inventarios = {}
dic_clientes = {}

menu(posible_inventario, varios_inventarios, dic_clientes)




# for i in nuevo_evento.keys():
#     print (f"{i} : {nuevo_evento[i]}")

# with open('recursos.json', 'w', encoding = 'utf-8') as archivo:
#     json.dump(inventario, archivo, ensure_ascii = False, indent = 2)

# print(inventario)