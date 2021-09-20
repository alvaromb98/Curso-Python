colors = {'Red', 'Green', 'Blue'}

#En set los elementos no tienen una posición dentro de este, no puedo hacer .index

colors.add('Violet')  #Lo añade al principio, a diferencia de las listas, dónde predeterminadamente se añadian al final

print(colors)  

colors.remove('Red')

colors.clear()  #Vacía el set