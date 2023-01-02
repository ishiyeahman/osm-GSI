import json 
from  meta.paths import jpath

import matplotlib.pyplot as plt

json_open = open(jpath, 'r')
geo_data = json.load(json_open)

coord = geo_data[0]['geojson']['coordinates']
