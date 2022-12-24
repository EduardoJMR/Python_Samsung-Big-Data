import sys

arguments =  len(sys.argv)

for i in range(0,arguments):
	print "argv[",i,"] ", type(sys.argv[i]), sys.argv[i]
