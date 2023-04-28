
##############################################################
#                ROCAS FANERÍTICAS/PORFIDICAS                #
##############################################################

# Paso 1. Determinar si la roca tiene macrocristales
macro = input('''¿La roca tiene macrocristales? 
                 1- SI  
                 2- NO:''')

if macro == "1":
    vidrio = input('''¿Cuál es el porcentaje de vidrio? 
                 1- Mayor a 90%
                 2- Entre 10-90%
                 3- Menor a 10%''')
# Clase 01. Pórfido Holohialino vitrofídico.
    if vidrio == "1":
        print("Roca holohialina porfídica-vitrofídica")
        
    elif vidrio =="2":
        matrizVitrea = input('''¿Tiene matriz vítrea?
                                1- Si
                                2- No''' )
# Clase 02. Pórfido Hialocristalino vitrofídico
        if matrizVirea == "1":
            print("Roca vitrofídica / Vitrófido")
            
# Clase 03. Pórfido holocristalino              
        elif matrizVirea == "2":
            matrizHialo = input( '''Determinar el tipo de matriz:
                                    1- Microlítica
                                    2- Microlítica fluidal
                                    3- Felsítica
                                    4- Máfica
                                    ''')
            print("Roca hialocristalina porfídica con matriz " + lower(matrizHialo)

            
# ROCAS AFANITICAS/AFIRICAS
elif macro == "2":
    vidrio = input('''¿Cuál es el porcentaje de vidrio? 
                 1- Mayor a 90%
                 2- Entre 10-90%
                 3- Menor a 10%''')
    
# Clase 01. Holohialina afírica, obsidiana.
    if vidrio == "1":
        print("Roca holohialina afírica (Obsidianas)")     
        
# Clase 02. Hialocristalina afírica
    elif vidio =="2":                                     
        matrizMicro = input('''¿Determinar el tipo de microlitos y mesostais?
                                1- Microlitos orientados en matriz vítrea
                                2- Microlitos no orientados''' )
        if matrizMicro == "1":    # Hialocristalina afírica microlítica
            print("Roca hialocristalina afírica con textura microlítica orientada")
        elif matrizMicro == "2":  # Hialocristalina afírica microlítica
            print("Roca hialocristalina afírica con textura microlítica")
            
# Clase 03.  Holocristalina afírica            
    elif vidio =="3":                                     
        matrizMicro = input('''¿Determinar el tipo de microlitos y mesostais?
                                1- Microlitos orientados en matriz vítrea
                                2- Microlitos no orientados''' )
        if matrizMicro == "1":    # Matriz microlítica orientada
            print("Roca holocristalina afírica con textura microlítica orientada")
        elif matrizVirea == "2":  # Matriz microlítica
            print("Roca holocristalina afírica con textura microlítica") 

    
    