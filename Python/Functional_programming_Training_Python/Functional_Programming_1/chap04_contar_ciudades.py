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

dict = dict()
for l in lines:
  ciudad = l.split()[1]
  v = dict.get( ciudad )
  if v is None:
    dict[ciudad] = 1
  else:
    dict[ciudad] = v + 1

print(dict)
