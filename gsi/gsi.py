import requests
import asyncio
import concurrent.futures
from itertools import repeat

config_get_max_depth_keys = ["Depth", "OfficeCode", "RiverCode", "SubRiverCode",  "CSVScale"]

#  longitude , latitude 
def get_max_depth(LON, LAT, key=None):
    url = f"https://suiboumap.gsi.go.jp/shinsuimap/Api/Public/GetMaxDepth?lon={LON}&lat={LAT}"
    
    
    try:
        response = requests.get(url, timeout=300)
    except :
        print(f"get_max_depth : {LON} {LAT} : exception!")
        return None
        
    print(response)
    jsonData = response.json()
    print(f"get_max_depth : {LON} {LAT} : {jsonData}")
    if key in config_get_max_depth_keys:
        if jsonData:
            return jsonData[key]
        else :
            # return jsonData
            return  None
    
    return jsonData


def get_max_depth_keys():
    return ["Depth", "OfficeCode", "RiverCode", "SubRiverCode",  "CSVScale"]


# multiple coordinates
async def async_get_max_depth(LON, LAT, key=None):
    
    url = f"https://suiboumap.gsi.go.jp/shinsuimap/Api/Public/GetMaxDepth?lon={LON}&lat={LAT}"
    response = requests.get(url)
    jsonData = response.json()
    print(LON, LAT, jsonData)
    if key:
        if jsonData:
            return jsonData[key]
        else :
            return  None
    
    return jsonData


async def get_multi_max_depth(LONS, LATS, key=None):
    co_list = list(map(async_get_max_depth, LONS, LATS))
    print(co_list)
    result = await asyncio.gather(*co_list)
    
    return result
    

def get_max_depth_multi_thread(LONS, LATS, key=None):
    len_argument =  len(LONS)
    MAX_WORKERS = 256
    
    processed = []
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        results = executor.map( get_max_depth, LONS, LATS, repeat(key))
        
        for result in results:
            processed.append(result)
            
    return processed

def address_search(query):
    url = f"https://msearch.gsi.go.jp/address-search/AddressSearch?q={query}"
    
    try:
        response = requests.get(url, timeout=300)
    except :
        return None
    
    jsonData = response.json()
    return  jsonData
    
def lon_lat_to_address(lon, lat):
    url = f"GET https://mreversegeocoder.gsi.go.jp/reverse-geocoder/LonLatToAddress?lat={lat}&lon={lon}"
    
    try:
        response = requests.get(url, timeout=300)
    except :
        return None
    
    jsonData = response.json()
    return  jsonData