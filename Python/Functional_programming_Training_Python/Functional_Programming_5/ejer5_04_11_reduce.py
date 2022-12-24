import functools
from functools import reduce
lista=[-3,5,-20,90,200]
def f(x,y):
	if y>0:
		return (x[0]+1,x[1]+y)
	else:
		return x
r=reduce( lambda x,y: (x[0],x[1]+y) if y>0 else (x[0]+y,x[1]), lista, (0,0) )
print(r)
