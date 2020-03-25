import urllib.request
import json
import os


offset_counter = 1
file_counter = 0

while file_counter < 39:
    url = 'https://www.ncdc.noaa.gov/cdo-web/api/v2/locations?location&limit=1000&' + 'offset=' + str(offset_counter)
    headers = {'TOKEN':os.environ.get('TOKEN')}
    req = urllib.request.Request(url, headers=headers)
    file_name = './location_'+str(file_counter)+'.json'
    
    with urllib.request.urlopen(req) as f:
        data = json.load(f)
    
        with open(file_name, 'w') as handler:
            json.dump(data, handler)
            
    file_counter += 1
    offset_counter += 1000


"""
    # make the request ot noaa
    call
    noaa
    # writes the results
    write
    results
    # let the scrip sleep for 5 seconds for a bugger
    wait
"""