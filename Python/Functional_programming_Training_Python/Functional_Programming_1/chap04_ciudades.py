#Obtaining the city and the people living in it

#Personal list v

#Pedro Barcelona
#Juana Zaragoza
#Luisa Sevilla
#Vega Madrid
#Hugo Madrid
#Carlota Zaragoza
#Andrea Barcelona

file = open( 'personal', 'rt' )
lines = file.readlines()

ciudades = set()
for l in lines:
  ciudades.add( l.split()[1] )

print(ciudades)
