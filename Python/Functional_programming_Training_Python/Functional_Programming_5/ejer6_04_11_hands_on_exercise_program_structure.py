import functools
from functools import reduce
# -- read the entire log into a list in memory
#
#   lines is a list, where each element is a record from the loudacre log
#
lines = [ ]
file = open('loudacre.log','rt')
lines = file.readlines()
file.close()

# -- load devicebase 
#
#  onerecord is a list made of each field in a single record
#
#  tempbase is a list used to collect each of the processed records
#     it is therefore a list of lists, or a nested collection
#
#  devicebase is a tuple cast from tempbase after processing is complete

tempbase = [ ]
onerecord  = [ ]
devicebase = ( )

for eachline in lines:
  onerecord  = eachline.split(',')
# -- leave these fields unchanged --
#
#               dts = onerecord[0]
#             model = onerecord[1]
#          uniqueID = onerecord[2]
#

# -- convert temperature to F
  onerecord[3] = 9/5 * int(onerecord[3]) + 32  # Device temp
  onerecord[4] = 9/5 * int(onerecord[4]) + 32  # Ambient temp

# -- convert numerical strings to integers
#          batt    = int(onerecord[5])
#          signal  = int(onerecord[6])
#          cpu     = int(onerecord[7])
#          ram     = int(onerecord[8])
  for i in range(5,9):
    onerecord[i] = int(onerecord[i])

# -- convert gps status to bool
#  gps    = onerecord[9]
  if onerecord[9]  == "TRUE":
     onerecord[9]  = True
  else:
     onerecord[9]  = False

# -- leave these fields unchanged --
#
#         btooth   = onerecord[10]
#           wifi   = onerecord[11]
#
# -- convert location to float
  onerecord[12]  = float(onerecord[12])                # Latitude
  onerecord[13]  = float(onerecord[13])                # Longitude

# --  split out the brand name and add it in a separate field
#
#        Note that the indexes for most fields just shifted right by one
#
  model = onerecord[1].split(' ')
  onerecord.insert(1,model[0])

# -- field processing is complete
# -- collect the modified record in tempbase
#
  tempbase.append(onerecord)

# -- processing is done -- cast the tuple
devicebase = tuple(tempbase)

print("functions-solved")

# -- Version 1 -- named function
def biggerthan(s):
 TF = len(s[1]) > 7
 return TF
#
# -- Version 2 -- single line named function
# def biggerthan(s): return len(s[1])>7   
#
# -- Filter for Versions 1 and 2
#
result = filter(biggerthan,devicebase)
# print result
print(len(result))

print("lambda-solved")

# -- Version 1 -- named function
# def biggerthan(s):
#     TF = len(s[1]) > 7
#     return TF
#
# -- Version 2 -- single line named function
# def biggerthan(s): return len(s[1])>7   
#
# -- Filter for Versions 1 and 2
#
# result = filter(biggerthan,devicebase)
# print result
# print len(result)

# -- Filter using anonymous function
#
result = filter(lambda s:len(s[1])>7, devicebase)
print(len(result))

print("map-reduce")

temperaturebase = [ ]
onerecord  = [ ]

for eachline in lines:
  onerecord  = eachline.split(',')

#  onerecord[3] contains the Device Temperature
#  onerecord[4] contains the Ambient Temperature
# -- collect the modified record in tempieraturebase
#
  temperaturebase.append(int(onerecord[3]))

# -- processing is done -- cast the tuple
temperaturebase  = tuple(temperaturebase)

print("Number of records: ", len(temperaturebase))
print("Type is a ", type(temperaturebase))

# print temperaturebase
#
#  -- use an anonymous function in a Python map() to convert C to F
#
temp2 = map(lambda t:t*9/5+32, temperaturebase)

print(temp2)

#
# -- Part 1: use reduce() to find the highest temp
#

highest = reduce(lambda x,y: x if(x>y) else y, temp2)
print("highest:",highest)

#
# -- Part 2: use reduce() to find the average temp
average = reduce(lambda x,y: x+y, temp2)/float(len(temp2))
print("average:",average)








# --
#
# --



# Date Time: 2014-03-15:10:10:31
# Model name and number: Titanic 4000
# Unique Device ID: 1882b564-c7e0-4315-aa24-228c0155ee1b
# Device temperature (celsius): 58
# Ambient temperature (Celsius) : 36
# Battery available (percent): 39
# Signal strength (percent): 31
# CPU utilization (percent): 15
# RAM memory usage (percent): 0
# GPS Status (enabled=True/disabled=False): TRUE
# Bluetooth status (enabled/disabled/connected): enabled
# WiFi status (enabled/disabled/connected): enabled
# Latitude: 40.69206648
# Longitude: -119.4216429

