def loadfile(filename):
	lines=[]
	file=open(filename,'rt')
	lines=file.readlines()
	file.close()
	return lines
def userinput(s):
	s=input(s)
	return s
	
