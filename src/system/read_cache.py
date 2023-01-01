import json 
from  meta.paths import jpath

json_open = open(jpath, 'r')
geo_data = json.load(json_open)
print(geo_data[0]['geojson']['coordinates'])
