# Paso 1. Determinar si la roca tiene macrocristales
macro = input('''¿La roca tiene macrocristales? 
                 1- SI  
                 2- NO:\n''')

##############################################################
#        ROCAS FANERÍTICAS/PORFIDICAS (MACROCRISTALES)   #
##############################################################
if macro == "1":
    vidrio = input('''¿Cuál es el porcentaje de vidrio? 
                 1- Mayor a 90%
                 2- Entre 10-90%
                 3- Menor a 10%\n''')
    #perVi = input('''Introduzca en número entero el porcentaje de vidrio: ''')
# Clase 01. Roca holohialina vitrofídica
    if vidrio == "1":
        print("Roca holohialina vitrofídica (Obsidiana vitrofídica)")
        
    elif vidrio =="2":
        matrizVitrea = input('''¿Tiene matriz vítrea?
                                1- Si
                                2- No\n''' )
# Clase 02. Pórfido Hialocristalino vitrofídico
        if matrizVitrea == "1":
            print("Roca vitrofídica / Vitrófido")
            
# Clase 03. Pórfido holocristalino              
        elif matrizVitrea == "2":
            matrizHialo = input( '''Determinar el tipo de matriz:
                                    1- Microlítica
                                    2- Microlítica fluidal
                                    3- Felsítica
                                    4- Máfica\n
                                    ''')
            print("Roca holocristalina porfídica con matriz " + matrizHialo.lower())

            
# ROCAS AFANITICAS/AFIRICAS
if macro == "2":
    vidrio = input('''¿Cuál es el porcentaje de vidrio? 
                 1- Mayor a 90%
                 2- Entre 10-90%
                 3- Menor a 10%?\n''')
    
# Clase 01. Holohialina afírica, obsidiana.
    if vidrio == "1":
        print("Roca holohialina afírica (Obsidianas afírica)")     
        
# Clase 02. Hialocristalina afírica
    elif vidio =="2":                                     
        matrizMicro = input('''¿Determinar el tipo de microlitos y mesostais?
                                1- Microlitos orientados en matriz vítrea
                                2- Microlitos no orientados\n''' )
        if matrizMicro == "1":    # Hialocristalina afírica microlítica
            print("Roca hialocristalina afírica con textura microlítica orientada")
        elif matrizMicro == "2":  # Hialocristalina afírica microlítica
            print("Roca hialocristalina afírica con textura microlítica")
            
# Clase 03.  Holocristalina afírica            
    elif vidio =="3":                                     
        matrizMicro = input('''¿Determinar el tipo de microlitos y mesostais?
                                1- Microlitos orientados en matriz vítrea
                                2- Microlitos no orientados\n''' )
        if matrizMicro == "1":    # Matriz microlítica orientada
            print("Roca holocristalina afírica con textura microlítica orientada")
        elif matrizVitrea == "2":  # Matriz microlítica
            print("Roca holocristalina afírica con textura microlítica") 
