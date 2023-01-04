import requests
import asyncio
import concurrent.futures

#  longitude , latitude 
def get_max_depth(LON, LAT, key=None):
    url = f"https://suiboumap.gsi.go.jp/shinsuimap/Api/Public/GetMaxDepth?lon={LON}&lat={LAT}"
    response = requests.get(url)
    jsonData = response.json()
    print(f"get_max_depth : {LON} {LAT} : {jsonData}")
    if key:
        if jsonData:
            return jsonData[key]
        else :
            return jsonData
            # return  None
    
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
    MAX_WORKERS = 10000
    
    results = []
    """
    with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        # Start the load operations and mark each future with its URL
        # future_to_url = {executor.submit(load_url, url, 60): url for url in URLS}
        
        # future_gmd =  dict(map(get_max_depth, LONS, LATS, key))
        
        future_gmd = {executor.submit( get_max_depth, lon, 32.82554, key) : lon for lon in LONS}
        # future_gmd = {executor.submit( get_max_depth, LONS, LATS, [key]*len_argument) }
        print(future_gmd)
        
        
        for future in concurrent.futures.as_completed(future_gmd):
            jsonData = future_gmd[future]
            print(f"future - jsonData : {jsonData}")
            results += [jsonData ]
            
            try:
                return results
            except Exception as exc:
                print('get_max_depth_multi_thread : error')
            
    """
    
    with concurrent.futures.ThreadPoolExecutor(max_workers= MAX_WORKERS) as executor:
        # futures = [executor.submit(target_func, x) for x in range(8)]
        future_gmd = [executor.submit( get_max_depth, lon, 32.82554, key) for lon in LONS]
        (done, notdone) = concurrent.futures.wait(future_gmd)
        for future in future_gmd:
            # print(future.result())
            results += [ future.result()]
    
    return results
            
    

