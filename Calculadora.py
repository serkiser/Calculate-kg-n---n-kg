import math
opcion = 0
while True:
    print("""
    Dime, ¿qué quieres hacer?
    
    1) Calcular Newtows
    2) Calcular Kilogramos
    """)
    opcion = int(input("Elige una opción: ") )     

    if opcion == 1:
        m = float(input("Introduce los Kilos a pasar ") )
        g = 9.80665
        print(" ")
        print("RESULTADO:",m*g,"Newtons")
    elif opcion == 2:
        f = float(input("Introduce los Newtons a pasar ") )
        g = 9.80665
        print(" ")
        print("RESULTADO:",f/g,"Kilogramos")
    elif opcion == 3:
        break
    else:
        print("Opción incorrecta")