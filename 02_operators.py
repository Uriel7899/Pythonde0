### Operadores Aritméticos ###

print(3 + 4)
print(3 - 4)
print(3 * 4)
print(3 / 4)

print(10 % 2)  #Operador de módulo

print(10 // 3)  #division aproximada a un número entero (Flor división)

print(2 ** 3) #Operador oponente

#tambien sirve para cadenas de texto
print("Hola" + " Python")
print("tu nombre es" + "--" * 5 + ">" + input("Cuál era?"))

### Operadores comparativos ###

print(3 > 4)
print(3 < 4)
print(3 >= 4)
print(3 <= 4)
print(3 == 4)
print(3 != 4)

### Tambien sirve para comparar por una ordenación alfabética ###

print("hola" == "Python")
print("Hola" != "Python")
print("Hola" < "Python")
print("Hola" > "Python")
print("Hola" >= "Python")
print("Hola" <= "Python")

### Si quiero comparar cantidad de caracteres utilizo la f! len() ###
print(len("Hola") >= len("Python"))
print(len("Hola") >= len("Zero"))

### Operadores lógicos ###
print(3 >= 4 and "hola" == "Python")  ### ambas tienen que ser true ###
print(3 >= 4 or "hola" == "Python")   ### una de las dos condiciones debe cumplirse para que arroje true ###
print(3 < 4 and "hola" == "Python")
print(3 > 4 or "hola" != "Python")
print(not(3 < 4)) ### Sirve para contradecir/negar el true/false ###
print(not(3 > 4))
