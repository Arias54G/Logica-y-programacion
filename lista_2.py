
print('==============================================')
print('==           Realizar una lista             ==')
print('==============================================')


"""
Éste programa realiza una lista. 

"""

lis=[11,25,31,6,51,15,7,8,9,105]
menor=i
for i in lis:
  if i>menor:
    menor=menor
  else:
    menor=i
print(menor,"Es el número menor")
posicion=1
for x in lis:
  if x==menor:
    print("posición ",posicion)
  else:
    posicion=posicion+1