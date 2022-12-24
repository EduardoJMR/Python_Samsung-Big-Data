import re

# -- Read the entire file into log
log = []
line=' '
file = open('loudacre.log','rt')
while True:
    line = file.readline()
    if not line:
       break
    log.append(line.split(','))
file.close()

pattern = re.compile("[0-9abcdef]*8-4[0-9abcdef][0-9abcdef][0-9abcdef]-[0-9abcdef]b")
for each in log:
#  print each[2]
  results = pattern.match(each[2])
#  print results
  if results != None:
     print(each[2])
     print(each)
 

