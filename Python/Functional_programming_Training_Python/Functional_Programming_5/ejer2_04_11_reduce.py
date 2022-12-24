
import functools
from functools import reduce
list=["ave","pez","gusano"]
print(reduce(lambda x,y:y+":"+x , list))
