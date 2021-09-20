print(2**3)  #El operador ** equivale a la potencia ^. Devolverá 8

print(3//2) #Me devolverá el resto, 1. Equivale a 3%2

#Es muy común que tenga que trabajar con datos que introduce el cliente. Por eso usaremos la función input

age = input("Insert your age: ")

#Si ahora quisiera operar con ese número que ha introducido el cliente,
#no podré, ya que es un string, por lo que tengo que convertirlo


print(type(int(age)))

new_age = int( age) + 5

print(new_age)