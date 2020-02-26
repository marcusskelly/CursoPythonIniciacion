print("Sistema para calcular el promedio de un alumno")

nombre = input("Para comenzar, cual es tu nombre?: ")

matematicas = float(input(nombre + " Cual es tu nota en matematicas?: "))
quimica = float(input(nombre + " Cual es tu nota en quimica?: "))
biologia= float(input(nombre + " Cual es tu nota en biologia?: "))

promedio = (matematicas + quimica + biologia) /3

if promedio >=6:
    
    print('Felicidades ' + nombre + '"aprobaste" con un promedio de: ', round(promedio,2))
else:
    print("Lo sentimos " + nombre + " 'has suspendido' con un promedio de: ", promedio)
    print("Lo sentimos " + nombre + " 'has suspendido' con un promedio de: ", round(promedio,1))

print("Fin")
