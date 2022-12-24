# -- read the entire log into a list in memory
#
#   lines is a list, where each element is a record from the loudacre log
#
# lines = [ ]
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
# onerecord  = [ ]
# devicebase = ( )

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
print(devicebase)
print("Number of records in device base: ", len(devicebase))
print("Device base is a ", type(devicebase))

#1a opcion

numSorrento = 0
GPSon       = 0
for each in devicebase:
    if each[1] == 'Sorrento':
      numSorrento += 1
      if each[10] :
        GPSon += 1
print("Number of Sorrento records = ",numSorrento)
print("Number with GPS enabled    = ",GPSon)

#2a opcion

s=sum([1 for each in devicebase if each[1] == 'Sorrento'])
l =sum([1 for each in devicebase if each[1] == 'Sorrento' and each[10]])
print("Number of Sorrento records = ",s)
print("Number with GPS enabled    = ",l)


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

    

   
