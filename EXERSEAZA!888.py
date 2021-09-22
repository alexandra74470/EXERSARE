ora=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
grade=[8,8,8,8,8,7,7,7,7,7,8,9,9,11,13,12,12,12,12,11,11,10,9,9]
gt=sum(grade)
tm=round(gt/24)
print('a)temperatura medie=', tm)
x=max(grade)
y=min(grade)
print('b)maximul temperaturii=', x,'; minimul temperaturii=', y)
l=ora[grade.index(x)]
print('c)temperatura maxima s-a inregistrat la orele',l)
m=ora[grade.index(y)]
print('d)temperatura minima s-a inregistrat la orele',m)