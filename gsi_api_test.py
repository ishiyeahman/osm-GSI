import gsi.gsi as gsi



data =  gsi.address_search("博多区")
print(data)

LON = 130.41435382
LAT = 33.59089486

data = gsi.lon_lat_to_address(LON, LAT)
print(data)

print(gsi.get_max_depth_from_lat_lon(LON, LAT, 0))
print(gsi.get_break_points_180min_50cm(LON, LAT))