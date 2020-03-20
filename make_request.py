import urllib.request
import json
import os


offset_counter = 1
file_counter = 0

while file_counter < 39:
    url = 'https://www.ncdc.noaa.gov/cdo-web/api/v2/locations?location&limit=1000&' + 'offset=' + str(offset_counter)
    headers = {os.environ.get('token')}
    req = urllib.request.Request(url, headers=headers)
    file_name = './location_'+str(file_counter)+'.json'
    
    with urllib.request.urlopen(req) as f:
        data = json.load(f)
    
        with open(file_name, 'w') as handler:
            json.dump(data, handler)
            
    file_counter += 1
    offset_counter += 1000