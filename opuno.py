import random
print("Programa para aprender los símbolos químicos".center(100,'-'))
print ('''
Selecciona una respuesta

    [Salir] Para salir (en cualquier momento)
    [1] Para comenzar''')
print ("")
x = input("Respuesta: ")

if x == "1":
    print ("")
    print(" ( RECORDATORIO: Para terminar de ejecutar el programa simplemente teclea: Salir )".center(100,'.'))
    print ("")
    nombre= ["Hidrógeno","Helio","Litio","Berilio","Boro","Carbono","Nitrógeno","Oxígeno","Flúor","Neón","Sodio","Magnesio","Aluminio","Silicio","Fósforo","Azufre","Cloro","Argón","Potasio","Calcio","Escandio","Titanio","Vanadio","Cromo","Manganeso","Hierro","Cobalto","Níquel","Cobre","Zinc","Galio","Germanio","Arsénico","Selenio","Bromo","Kriptón","Rubidio","Estroncio","Itrio","Zirconio","Niobio","Molibdeno","Tecnecio","Rutenio","Rodio","Paladio","Plata","Cadmio","Indio","Estaño","Antimonio","Telurio","Yodo","Xenón","Cesio","Bario","Lutecio","Hafnio","Tantalio","Wolframio","Renio","Osmio","Iridio","Platino","Oro","Mercurio","Talio","Plomo","Bismuto","Polonio","Astato","Radón","Francio","Radio","Laurencio","Rutherfordio","Dubnio","Seaborgio","Bohrio","Hassio","Meitnerio","Darmstatio","Roentgenio","Copernicio","Nihonio","Flerovio","Moscovio","Livermorio","Teneso","Organesón","Lantano","Cerio","Praseodimio","Neodimio","Prometio","Samario","Europio","Gadolinio","Terbio","Disprosio","Holmio","Erbio","Tulio","Iterbio","Actinio","Torio","Protactinio","Uranio","Neptunio","Plutonio","Americio","Curio","Berkelio","Californio","Einstenio","Fermio","Mendelevio","Nobelio"]
    símbolo_químico=["H","He","Li","Be","B","C","N","O","F","Ne","Na","Mg","Al","Si","P","S","Cl","Ar","K","Ca","Sc","Ti","V","Cr","Mn","Fe",
                         "Co","Ni","Cu","Zn","Ga","Ge","As","Se","Br","Kr","Rb","Sr","Y","Zr","Nb","Mo","Tc","Ru","Rh","Pd","Ag","Cd","In","Sn","Sb","Te","I","Xe","Cs","Ba","Lu","Hf","Ta","W","Re","Os","Ir","Pt","Au","Hg","Tl","Pb","Bi","Po","At","Rn","Fr","Ra","Lr","Rf","Db","Sg","Bh","Hs","Mt","Ds","Rg","Cn","Nh","Fl","Mc","Lv","Ts","Og","La","Ce","Pr","Nd","Pm","Sm","Eu","Gd","Tb","Dy","Ho","Er","Tm","Yb","Ac","Th","Pa","U","Np","Pu","Am","Cm","Bk","Cf","Es","Fm","Md","No"]
    respuesta="si"
    total=1
    buenas=0
    while respuesta!= "Salir":
        posicion= random.randint(0,len(nombre)-1)
        print(" ")
        print ("¿Cuál es el símbolo químico de:", nombre[posicion])
        respuesta=input("Escribe aquí tu respuesta con la primera letra en mayúscula: ")
        if respuesta == símbolo_químico[posicion]:
            print("Correcto,",símbolo_químico[posicion], " es el símbolo químico de",nombre[posicion])
            print(" ")
            buenas=buenas+1
            total=total+1
        elif respuesta == "Salir":
            print("\nHas terminado de responder\n")
            print (" . . .")
            score = buenas*100/(total-1)
            print("Tu puntaje es de:",score)
            print("Obtuviste",buenas,"de",total - 1)
        else:
            print("Incorrecto, el símbolo químico de", nombre[posicion],"es", símbolo_químico[posicion],".")
            total=total+1
    if score<60:
        print("Necesitas practicar mucho :(")
        x=0
        despedida()
    elif score<80:
        print("Vas por buen camino, pero tienes que practicar un poquito :)")
        x=0
        despedida()
    elif score>80:
        print("Vas muy bien sigue asi :D")
        x=0
        despedida()
    else:
        print("Intenta de nuevo")
        x=0