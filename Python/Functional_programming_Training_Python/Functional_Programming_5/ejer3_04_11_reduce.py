
import functools
from functools import reduce
lista=["ave","pez","gusano"]
print(reduce(lambda x,y:max(x,len(y)),lista, 0))
