import gsi.gsi as gsi


data =  gsi.address_search("博多区")
print(data)

data = gsi.lon_lat_to_address(130.41435382, 33.59089486)
print(data)

print(gsi.get_max_depth_from_lat_lon(130.41435382, 33.59089486, 0))