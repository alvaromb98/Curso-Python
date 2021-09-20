foods = ['apples', 'bread', 'cheese', 'milk']

for food in foods:
    if food =='cheese':
        break          #Si encuentra queso, deja de ejecutar el bucle, ocurre lo 
    print(food)        #contrario con continue, si no lo encuentra, para el buble


for letter in "Hello":
    print(letter)

count = 4

while count <= 10:  
    print(count)
    count = count + 1  #Un while siempre debe tener una condición de rotura