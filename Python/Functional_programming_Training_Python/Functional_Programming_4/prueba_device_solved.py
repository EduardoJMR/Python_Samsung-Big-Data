# lines=list()
file=open('loudacre.log','rt')
lines=file.readlines()
file.close()

tempbase= list()
# onerecord= list()
# devicebase= tuple()

for i in lines:
    onerecord = i.split(',')
    
    onerecord[3] = 9/5*int(onerecord[3]) + 32
    onerecord[4] = 9/5*int(onerecord[4]) +32

    for i in range(5,9):
        onerecord[i]= int(onerecord[i])

    if onerecord[9] == "TRUE":
        onerecord[9] = True
    else:
        onerecord[9] = False

    
    onerecord[12] = float(onerecord[12])
    onerecord[13] = float(onerecord[13])

    model = onerecord[1].split(' ')
    onerecord.insert(1,model[0])

    tempbase.append(onerecord)

devicebase= tuple(tempbase)
print(devicebase)
print("Number of records in device base: ", len(devicebase))
print("Device base is a ",type(devicebase))

numSorrento = 0
GPSon = 0

for i in devicebase:
    if i[1] == 'Sorrento':
        numSorrento +=1
        if i[10]:
            GPSon += 1

print("Number of Sorrento records =", numSorrento)
print("Number with GPS enabled =",GPSon)

s=sum(1 for i in devicebase if i[1]=='Sorrento')
t=sum(1 for i in devicebase if i[1]=='Sorrento' and i[10])

print("Number of Sorrento records = ",s)
print("Number with GPS enabled =",t)
