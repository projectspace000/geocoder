
import csv
import time
import shutil
from geopy import geocoders
geolocator = geocoders.GoogleV3(api_key='AIzaSyBgWKZkSlUzJblOY0bKknTdV946hobPNpE')

# Let's start by creating a copy of our raw file just to be safe
shutil.copyfile("raw.csv","output.csv")

# open the file and assign it to the var f
f = open('raw.csv')

# create a blank array called addresses
addresses = []

# use the csv reader to actually start doing stuff
csv_f = csv.reader(f)
# iterate through each row, and only grab column 1, and add it to the address array
for row in csv_f:
   addresses.append(row[1])
   
print(addresses[3])

# close our original file
f.close()

# create a new empty array called locations
locations = []

# for each value in the addresses array that we created earlier 
# geocode it and save it to a variable called location
# then we'll then append that single location to the locations variable
for val in addresses:
   location = geolocator.geocode([val])
   locations.append((str(location.longitude) + str(", ") + str(location.latitude)))
   time.sleep(.1)
   

# Create a header row for our new csv
header = ['NAME','ADDRESS','COORDINATES']

# open the original csv and grab all the data
# place it in a var called data, and close the file again
f = open('raw.csv')
data = [item for item in csv.reader(f)]
f.close()

# create a blank arraycalled new_data
new_data = []

# for each item in data append a location
# then add the complete item to the new data variable
for i, item in enumerate(data):
    item.append(locations[i])
    new_data.append(item)

# open the new csv and write the header row 
# followed by a row for each object in the new_data array
f = open('output.csv', 'w')
csv.writer(f, lineterminator='\n').writerow(header)
csv.writer(f, lineterminator='\n').writerows(new_data)
f.close()

fname = "output.csv"
data = csv.reader(open(fname), delimiter = ',')

#Skip the 1st header row.
data.next()

#Open the file to be written.
f = open('newmap.kml', 'w')

#Writing the kml file.
f.write("<?xml version='1.0' encoding='UTF-8'?>\n")
f.write("<kml xmlns='http://earth.google.com/kml/2.1'>\n")
f.write("<Document>\n")
f.write("   <name>" 'newmap.kml' +"</name>\n")
for row in data:
    f.write("   <Placemark>\n")
    f.write("       <name>" + str(row[0]) + "</name>\n")
    f.write("       <description>" + str(row[1]) + "</description>\n")
    f.write("       <Point>\n")
    f.write("           <coordinates>" + str(row[2]) + "</coordinates>\n")
    f.write("       </Point>\n")
    f.write("   </Placemark>\n")
f.write("</Document>\n")
f.write("</kml>\n")
f.close()
print "File Created. "
print "Press ENTER to exit. "
raw_input()