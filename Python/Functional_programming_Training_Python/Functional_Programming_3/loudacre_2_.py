line=[]
file=open('loudacre.log','rt')
while True:
	x= file.readline()
	if not x:
		break
	x=x.split(',')
	line.append(x)
file.close()
print(len(line))
print(len(line[0]))
print(line[375][2])
print(line[410][2])
print(line[435][2])
