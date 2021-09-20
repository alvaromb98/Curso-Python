def hello(name):
    print("Hello " + name)

hello("joe")

# def hello(name="Person"):      #establezco que, si no le paso nada como parámetro, por defecto, tome Person
#     print("Hello " + name) 
# hello()

def add(n1, n2):
    return n1 + n2

print(add(10, 30))




add = lambda n1 , n2 : n1 + n2 #Función ya predeterminada en python
