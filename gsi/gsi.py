import requests

# latitude , longitude 
def getGetMaxDepth(LAT, LON, key=None):
    url = f"https://suiboumap.gsi.go.jp/shinsuimap/Api/Public/GetMaxDepth?lon={LON}&lat={LAT}"
    response = requests.get(url)
    jsonData = response.json()
    
    if key:
        return jsonData[key]
    
    return jsonData

""" debug """
def getGetMaxDepthKeys():
    return ["Depth", "OfficeCode", "RiverCode", "SubRiverCode",  "CSVScale"]

