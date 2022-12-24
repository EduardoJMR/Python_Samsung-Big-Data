#Obtaining the city and the number of people living in it

#Personal list v

#Pedro Barcelona
#Juana Zaragoza
#Luisa Sevilla
#Vega Madrid
#Hugo Madrid
#Carlota Zaragoza
#Andrea Barcelona

from pprint import pprint as pp

file = open( 'personal', 'rt' )
lines = file.readlines()

dict = dict()
cont = 0
for l in lines:
  persona = l.split()[0]
  ciudad = l.split()[1]
  
  pers = dict.get( ciudad, set() )
  pers.add( persona )
  cont += 1
  dict[ciudad] = pers
  print("El numero de personas de la ciudad",ciudad,"es",len(pers)) 
file.close( )
pp( dict )
