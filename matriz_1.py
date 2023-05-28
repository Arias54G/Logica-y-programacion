
print('==============================================')
print('==           Realizar una matriz            ==')
print('==============================================')


"""
Éste programa realiza una matriz.

"""

M=[[8,6,-3],[2,1,4],[3,1,9]]
M1=M[0]
M2=M[1]
M3=M[2]

contar=0
contar2=0
for i in M:
  contar=contar+1
  for x in i:
    contar2=contar2+1
seg_valor=int(contar2/contar)
print("Esta es un matriz de",contar,"x",seg_valor)

for i in M1:
    print(i,end=" ")
print("")
for d in M2:
    print(d,end=" ")
print("")
for e in M3:
    print(e,end=" ")