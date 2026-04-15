### Strings ###

my_string = "Mi string"
print(len(my_string))

my_new_string = "Este es un string\ncon salto de línea"
print(my_new_string)

my_tab_string = "\tEste es un string con tabulación"
print(my_tab_string)

# Formateo #
name, surname, age = 'Uriel', 'Aguilar', 26

# %s para strings y %d para int #
print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))
print("Mi nombre es %s %s y mi edad es %d" %(name, surname, age))
print(f"Mi nombre es {name} {surname} y mi edad es {age}") ### Mejor forma de realizarlo ###

# Desempaquetado de caracteres #
language = "python"
a, b, c, d, e, f = language
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

# División #

language_slice = language[1:3]
print(language_slice)

# Reversa # 

language_reverse = language[::-1]
print(language_reverse)

# Otras funciones del sistema #
print(language.capitalize())
print(language.upper())
print(language.count("t"))
print(language.isnumeric())
print("1".isnumeric())
print(language.lower())