#listas con elementos que no van a cambiar. Son inmutables. Son más rápidas que las listas
x = (1,2,3)

#months = ('January', 'February')

#print(dir(x))

#Caso de tener una tupla de un solo elemento
y=(1)

print(type(y))  #Esto devolverá tipo int, ya que es un solo elemento
                #para evitarlo, pongo una coma
y = (1,) 

del y #elimina la tupla

#Es útil combinar diccionarios y tuplas:

locations = {
    (35.1221, 43.432): "Tokyo"   #Asigno a ciudades sus coordenadas mediante tuplas, pues son datos inmutables
}