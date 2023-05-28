
print('==============================================')
print(' Encontrar el número negativo, positivo o cero')
print('==============================================')


"""
Éste programa indica si el número es positiv, negativo o si es cero.

"""


numero=(int(input("Digite un número: ")))

if numero==0:
    print("El número es 0")
else:
    if numero<0:
        print("El número es un negativo")
    else:
        print("El número es positivo")