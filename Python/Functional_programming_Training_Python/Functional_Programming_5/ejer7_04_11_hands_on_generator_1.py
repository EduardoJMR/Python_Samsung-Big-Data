import functools
from functools import reduce
#def stern_series( startnum,endnum ):
#   def sumofparts(n):
#    r = 0
#    t = n
#    while( t > 0 ):
#      r += t % 10
#      t //= 10
#    return r
#
#   return [ ( n, float(n)/sumofparts(n)) for n in range(startnum,endnum) ]
  

def stern_series( startnum, endnum ):
   def sumofparts(n): return reduce( lambda x, y: x + int(y), str(n), 0 )
   return [ ( n, float(n)/sumofparts(n)) for n in range(startnum,endnum) ]
  
for eachratio in stern_series(1,500):
   print( eachratio )
