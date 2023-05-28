
print('==============================================')
print('==           Realizar una lista             ==')
print('==============================================')


"""
Éste programa realiza una lista. 

"""

lis=[1,200,3,56,5,15,7,8,9,105]
mayor=0
for i in lis:
  if i>mayor:
    mayor=i
  else:
    mayor=mayor
print(mayor,"Es el número mayor")