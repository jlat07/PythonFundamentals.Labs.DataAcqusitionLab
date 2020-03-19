import urllib.request
import json


file_counter = 0
offset_counter = 1
file_start = 0

while file_counter < 1:
    url = 'https://www.ncdc.noaa.gov/cdo-web/api/v2/locations/' + 'offset=' + str(offset_counter)
    headers = {'token': 'XedyBNDLDGtaqOCjNDlpEBYOyGyRlRvc'}
    req = urllib.request.Request(url, headers=headers)
    file_name = './location_' + str(file_start) + '.json'
    
    ##parsing response
    with urllib.request.urlopen(req) as f:
        data = json.loads(f)
        
    file_counter += 1
    offset_counter += 1000