
import functools
from functools import reduce
list=[8,34,9,10]
print(reduce(lambda x,y: x if x<y else y, list))
print(reduce(lambda x,y: min(x,y),list))
print(min(list))
