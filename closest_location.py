from math import cos, asin, sqrt

def distance(lat1: float, lon1: float, lat2: float, lon2: float):
    p = 0.017453292519943295
    hav = 0.5 - cos((lat2-lat1)*p)/2 + cos(lat1*p)*cos(lat2*p) * (1-cos((lon2-lon1)*p)) / 2
    return 12742 * asin(sqrt(hav))

def closest_destination(destinations, objectstores, selected_object_store):
    objectstore = objectstores[selected_object_store]
    min_dist = 999999.99
    for dest in destinations:
        d_lat = dest['context']['latitude']
        d_lon = dest['context']['longitude']
        o_lat = objectstore['latitude']
        o_lon = objectstore['longitude']
        dist = distance(o_lat, o_lon, d_lat, d_lon)
        if dist < min_dist:
            min_dist = dist
            closest_dest = dest
    return closest_dest
