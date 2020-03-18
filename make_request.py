
2. Using [urllib.request](https://docs.python.org/3/library/urllib.request.html#module-urllib.request) module, make it so that your script makes rest calls to NOAA's api and saves the results to json files.
3. Once it is executed, you should have 39 files.
The files should be named as follows:
* locations_0.json
* locations_1.json


make an api call

store data as a variable in the code
save the data as a file.
file name has to iterate or +1 to incriment file name for every pull


import urllib.request
import json


url = ' https://www.ncdc.noaa.gov/cdo-web/api/v2/locations/'
req = urllib.request.Request(url)

##parsing response
r = urllib.request.urlopen(req).read()
cont = json.loads(r.decode('utf-8'))
counter = 0

##parcing json
for item in cont['data']['children']:
    counter += 1
print("Title:", item['data']['title'], "\nComments:", item['data']['num_comments'])
print("----")

##print formated
# print (json.dumps(cont, indent=4, sort_keys=True))
print("Number of titles: ", counter)

what i have about looks to pull the request. read yhte json file, store it in cont then
oarce through it and print it. I would take each parche. pickle it out?

use the counter to update a location_'x'.json file name and impliment it through interation