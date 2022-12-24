loglist1=[]
file=open('loudacre.log','r')
while True:
        x= file.readline()
        if not x:
                break
        loglist1.append(x)
print(loglist1)
file.close()
print(len(loglist1))
