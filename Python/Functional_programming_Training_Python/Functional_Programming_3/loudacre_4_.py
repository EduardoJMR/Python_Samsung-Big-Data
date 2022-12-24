loglist2=[]
file=open('loudacre.log','rt')
loglist2=file.readlines()
file.close()
print(loglist2)
print(len(loglist2))
