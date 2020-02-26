print("===========\n")

print("Menu de opciones: \n")

print("============ \n")
print("Presiona 1 para convertir de numero a palabra")
print("Presiona 2 para convertir de palabra a numero")

opcion = int(input("Cual es tu opcion deseada?:"))

if opcion == 1:
    print("\n Conversor de numero a palabra \n")

    opcion_uno = int(input("Cual es el numero que deseas a palabra?: "))

    if opcion_uno == 1:
        print("El numero es 'uno'")
    elif opcion_uno == 2:
        print("El numero es 'dos'")
    elif opcion_uno == 3:
        print("El numero es 'tres'")
    else:
        print("El numero seleccionado, no esta registrado")
    
elif opcion == 2:
    print("\n Conversor de palabra a numero \n")

    opcion_dos = input("Cual es la palabra que deseas convertir a numero?: ")

    if opcion_dos == "uno":
        print("El numero es '1'")
    elif opcion_dos == "tres":
        print("El numero es '3'")
    elif opcion_dos == "cuatro":
        print("El numero es '4'")
    elif opcion_dos == "cinco":
        print("El numero es '5'")
    else:
        print("El numero seleccionado no esta registrado")
else:
    print("Opcion no disponible")

print("Fin")


    
