x=[1,2,3,4,5]
y=x
suma=0
for i in range(0,3):
    suma=suma+x[i]
print('a)suma primelor 3 componente ale variabilei x=',suma)
sy=suma
print('b)suma primelor 3 componente ale variabilei x=',sy)
produs=1
for j in range(0,len(x)):
    produs=produs*x[j]
print('c)produsul tuturor componentelor variabilei x=', produs)
print('d)valoarea absoluta a componentei a 3-a a variabilei y=',abs(y[2]))
print('e)uma primelor componente ale variabilelor x si y=',x[0]+y[0])