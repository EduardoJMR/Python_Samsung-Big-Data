devlog=[]
file=open('loudacre.log','r')
devlog=file.readlines()
file.close()
for l in devlog:
	print(l.split(',')[0].split(':')[0])
