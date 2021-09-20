myStr= "hello world"
# print(dir(myStr))   #dir me sugiere qué puedo hacer con la variable dentro del paréntesis

# print(myStr.upper())  #otros métodos de este tipo son lower, capitalize, swapcase, etc

# print(myStr.replace('hello', 'bye').upper()) #ejemplo de métodos encadenados

# print(myStr.count('l'))

# print(myStr.startswith('hello')) #boolean que devolverá true

# print(myStr.endswith('world'))

# print(myStr.split())

# print(myStr.split('o')) #hace lista con el string 
#                         #cortado por las o's que encuentre

# print(myStr.find('r'))

# print(len(myStr))  #devuelve la longitud del string

# print(myStr.index('e'))   #devuelve la posición en la que esté ese caracter

# print(myStr.isnumeric())

# print(myStr.isalpha())

print(myStr[0])

print(myStr[-1])  #al poner número negativo irá desde el final del string

myName = 'Álvaro'

print('My name is ' + myName) #concatenación. Añadir espacio después de la palabra

print(f"My name is {myName}") #otra manera de concatenar. Poniendo f
                              #al principio advierte de que habrá un string que debe ser interpretado como variable

print("My name is {0}".format(myName))  #Lo mismo.