import urllib.request
import json
import pickle

file_start = 0
offset_counter = 1
file_counter = 0

while file_counter < 1:
    url = 'https://www.ncdc.noaa.gov/cdo-web/api/v2/locations?location&limt=1000&' + 'offset=' + str(offset_counter)
    headers = {'token': 'XedyBNDLDGtaqOCjNDlpEBYOyGyRlRvc'}
    req = urllib.request.Request(url, headers=headers)
    file_name = './location_' + str(file_start) + '.json'
    
    ##parsing response
    with urllib.request.urlopen(req) as f:
        data = json.loads(f)
        
        with open(file_name, 'wb') as handler:
            pickle.dump(data, handler)
        
        file_counter += 1
        offset_counter += 1000
