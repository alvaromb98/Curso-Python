#numbers_list = list(1,2,3,4)
colors = ['red', 'green', 'blue']

#print(numbers_list) #esto me devolverá error porque espera un elemento pero recibe 4

#Lo arreglamos agrupando los 4 elementos en uno solo, usando una tupla

#numbers_list = list((1,2,3,4))
#print (type(numbers_list))

r = list(range(1, 10)) #Lista de números del 1 al 10 (éste no inclusive)

#print(dir(numbers_list))

#print (len(numbers_list))

#print(numbers_list[2]) 

# print('green' in colors)   #Me dice si lo que introduzca existe dentro de una lista

# print(colors)

# colors[1] = 'yellow'   #Cambio elementos de una lista

# print(colors)

# colors.append('violet') #Con este método añado un nuevo elemento al final de la lista

#colors.extend(['violet', 'yellow'])  #Para añadir múltiples elementos debo usar extend 
                                     #y pasar los elementos en una tupla



#Si ahora quisiera añadir elementos pero en una posición concreta:
colors.insert(1, 'violet')

colors.insert(len(colors), 'violet')   #Lo inserta al final, pues pasamos como posición la longitud total de la lista

colors.pop() #Elimina el último elemento de la lista

colors.clear() #Elimina todos los elementos de la lista

colors.sort() #Los ordena alfabeticamente

colors.sort(reverse=True) #Los ordena en orden alfabetico inverso

#Otros métodos como .index o .count también funcionan en listas

print(colors)