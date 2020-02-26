mensaje = "Hola"
mensaje += " "
mensaje += "Marcus"
print(mensaje)

print("Concatenacion:")

mensaje = "Hola"
espacio = " "
nombre = "Marcus"
print(mensaje + espacio + nombre)

numero_uno = 4
numero_dos = 6
resultado = numero_uno + numero_dos
resultado = str(resultado)
print("El resultado de la suma es: " +resultado)

print("Busqueda:")
mensaje = "Hola Marcus"
buscar_subcadena = mensaje.find("Marcus")
print(buscar_subcadena)

print("Extraccion:")

mensaje = "Hola Marcus"
extraer_cadena = mensaje[1:8]
print(extraer_cadena)

print("Comparacion")

mensaje_uno = "Hola"
mensaje_dos = "Hol"
print (mensaje_uno == mensaje_dos)
