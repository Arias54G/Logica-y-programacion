
print('==============================================')
print('==           Encontrar número máximo        ==')
print('==============================================')


"""
Éste programa indica el numero mayor entre a,b y c

"""

a=int(input("Escriba primer número: "))
b=int(input("Escriba segundo número: "))
c=int(input("Escriba tercer número: "))

if(a==b==c):
    print("Todos son iguales")
else:
    if(a>b and a>c):
        print(a," Es el número mayor")
    else:
        if(b>a and b>c):
            print(b," Es el número mayor")
        else:
            print(c," Es el número mayor")