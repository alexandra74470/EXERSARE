zi=['luni','marti','miercuri','joi','vineri','sambata','duminica']
venit=[2000,3500,4400,6700,1600,3000,7500]
vs=sum(venit)
print('a)venitul saptamanal al intreprinderii=', vs)
vm=round(vs/7,2)
print('b)media venitului zilnic=', vm)
x=zi[venit.index(max(venit))]
print('c)ziua cu cel mai mare venit este', x)
y=zi[venit.index(min(venit))]
print('d)ziua cu cel mai mic venit este', y)
print(zi[venit.index(3500)])