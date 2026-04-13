# variables

my_variable = "My string variable"
print(my_variable)

my_int_variable = 25
print(my_int_variable)

my_bool_variable = False
print(my_bool_variable)

# Concatenación de variables en cadena
print(my_variable, my_int_variable, my_bool_variable)

# Funciones del sistema - len ()---> cuenta la cantidad de caracteres
print(len(my_variable))
"""FUNCIONA CON STRINGS PERO NO CON INT"""

# Varias variables en una línea
first_name, last_name, age, country = "Uriel", "Aguilar", 26, "Ezeiza, Bs. As."

print("Hola, mi nombre es", first_name, last_name,", tengo", age, "años y vivo en", country)

# Inputs ---> Sirve para asignar/cambiar valores a variables

first_name = input("¿Cuál es tu nombre? ")
age = input("¿Cuántos años tienes? ")
print(first_name)
print(age)


