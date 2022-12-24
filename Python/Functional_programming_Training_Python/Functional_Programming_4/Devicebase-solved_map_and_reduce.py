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
#  temperaturebase is a list used to collect the device temperatures
#  it is then cast as a tuple
#

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

