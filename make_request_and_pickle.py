import urllib.request
import os
import json
import pickle


offset_counter = 1
file_counter = 0

while file_counter < 39:
    url = 'https://www.ncdc.noaa.gov/cdo-web/api/v2/locations?location&limt=1000&' + 'offset=' + str(offset_counter)
    headers = {os.environ.get('token')}
    req = urllib.request.Request(url, headers=headers)
    file_name = './location_' + str(file_counter) + '.json'
    
    ##parsing response
    with urllib.request.urlopen(req) as f:
        data = json.load(f)

        with open(file_name, 'wb') as handler:
            pickle.dump(data, handler)
    
    file_counter += 1
    offset_counter += 1000
