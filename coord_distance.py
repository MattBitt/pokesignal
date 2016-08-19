import math

def distance(origin, destination):
    # returns distance in km
    lat1, lon1 = origin
    lat2, lon2 = destination
    radius = 6371 # km

    dlat = math.radians(lat2-lat1)
    dlon = math.radians(lon2-lon1)
    a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1)) \
        * math.cos(math.radians(lat2)) * math.sin(dlon/2) * math.sin(dlon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = radius * c

    return d
    
origin = (30.019090, -90.156090)
origin = (29.963279, -90.224245)
destination = (29.933747, -90.197399)
origin = (30.0216059559791, -90.1544360692241)
destination = (30.0137434762862, -90.1594836653675)


print distance(origin, destination)
