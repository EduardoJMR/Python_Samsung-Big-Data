file=open('loudacre.log','rt')
lines=file.readlines()
allmodels= set()
allmodels_2=set()
for l in lines:
 brand_name=l.split(',')[1]
 allmodels.add(brand_name)
for l in lines:
 brand_name_2=l.split(',')[1].split(' ')[0]
 allmodels_2.add(brand_name_2)
s=sorted(allmodels)
print('----------')
t=sorted(allmodels_2)
print('----------')
print(s)
print('----------')
print(t)
print('--------')

r=sorted(set([l.split(',')[1] for l in lines]))
t=sorted(set([l.split(' ')[0] for l in r]))	
print(r)
print('---------')
print(t)
