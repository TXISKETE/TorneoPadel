from random import randrange
import time
import sys

# VARIABLES. 
# El backup se usa para volver a llenar la lista jugadores cuando alguna pareja coincida con los anteriores
jugadores = ["Fran", "Txerra", "Gabri", "Javi", "Pikaza", "Sergi", "Garro", "Josu"]
jugadores_backup = jugadores.copy()
anteriores =[["Fran", "Txerra"],["Gabri", "Garro"],["Josu", "Pikaza"],["Aitor", "Sergi"],["Fran", "Sergi"],["Gabri", "Josu"],["Aitor", "Pikaza"],["Garro", "Txerra"]]

# PRESENTACION DE LAS REGLAS DEL SORTEO
print("\nSORTEO PARA EL SEGUNDO TORNEO DE PADEL NOVIEMBRE 2020\n")
time.sleep(2)
print("Las parejas no podran coincidir con las de los anteriores torneos, que fueron las siguientes:\n")
time.sleep(3)
print("Torneo 1: Fran y Txerra, Josu y Pikaza, Aitor y Sergi, y Gabri y Garro. Ganado por Gabri y Garro\n")
print("Torneo 2: Fran y Sergi, Aitor y Pikaza, Gabri y Josu, y Garro y Txerra. Ganado por Aitor y Pikatza\n")
time.sleep(3)
print("Comenzamos haciendo las parejas...\n")
time.sleep(3)

# FUNCION QUE RECIBE LAS PAREJAS, Y ASIGNA LOS ENFRENTAMIENTOS
def hacer_sorteo(parejas):
    time.sleep(3)
    print("\nHacemos el sorteo de emparejamientos... \n")
    time.sleep(3)
    print("Estos son los partidos:\n")
    time.sleep(3)
    # SEPARAMOS CADA PAREJA EN UNA LISTA PARA FACILITAR LA MANIPULACION, PARA MOSTRAR LOS DATOS "BONITOS" EN PANTALLA
    pareja1 = []
    pareja2 = []
    pareja3 = []
    pareja4 = []
    # SEPARAMOS
    pareja1.append(parejas.pop(randrange(len(parejas))))
    pareja2.append(parejas.pop(randrange(len(parejas))))
    pareja3.append(parejas.pop(randrange(len(parejas))))
    pareja4.append(parejas.pop(randrange(len(parejas))))
    # MOSTRAMOS LOS RESULTADOS DEL SORTEO, CON LOS EMPAREJAMIENTOS
    print("Partido 1 - {} y {} vs {} y {}".format(pareja1[0][0], pareja1[0][1],pareja2[0][0], pareja2[0][1]))
    print("Partido 2 - {} y {} vs {} y {}\n".format(pareja3[0][0], pareja3[0][1],pareja4[0][0], pareja4[0][1]))
    # FINALIZAMOS PROGRAMA
    sys.exit()
    
# FUNCION PARA HACER LAS PAREJAS    
def hacer_parejas(jugadores_t):
    #lista de parejas temporal hasta comprobar que no han jugado antes
    parejas_t = []
    #Hacemos cuatro parejas
    while len(jugadores_t) != 0:
        # Creamos una lista temporal para añadirla posteriormente a la lista parejas como lista
        pareja_add= []
        # Añadimos a la lista dos jugadores aleatorios
        pareja_add.append(jugadores_t.pop(randrange(len(jugadores_t))))
        pareja_add.append(jugadores_t.pop(randrange(len(jugadores_t))))
        # Ordenamos alfabeticamente para facilitar la comparacion
        pareja_add.sort()
        # Añadimos la lista con la pareja aleatoria a la lista de parejas
        parejas_t.append(pareja_add)
    comparar_parejas(parejas_t)

# FUNCION PARA COMPROBAR QUE LAS PAREJAS NO COINCIDAN CON LAS DEL ANTERIOR TORNEO
def comparar_parejas(parejas_te):
    # Recorremos la lista de parejas para comparar cada una con las anteriores
    for i in range(len(parejas_te)): 
        # Recorremos la lista de anteriores para compararlas con cada pareja generada
        for j in range(len(anteriores)):
            # Comprobamos que las parejas no coinciden con las anteriores, si es asi, mostramos un mensaje indicando que vuelve a sortearse (se puede omitir)
            if parejas_te[i][0] == anteriores[j][0] and parejas_te[i][1] == anteriores[j][1]:
                print("La pareja {} y {} ya ha jugado anteriormente, volviendo a sortear...\n".format(parejas_te[i][0], parejas_te[i][1]))
                time.sleep(3)
                jugadores = jugadores_backup.copy()
                hacer_parejas(jugadores) 
    print("Las parejas son las siguientes:\n")
    # Mostramos cada una de las parejas
    for i in range(len(parejas_te)):
        time.sleep(3)
        print("Pareja {} - {} y {}".format(i+1, parejas_te[i][0], parejas_te[i][1]))
    hacer_sorteo(parejas_te)
            
#Arrancamos programita!
hacer_parejas(jugadores) 


