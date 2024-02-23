from math import cos, asin, sqrt


def distance(lat1: float, lon1: float, lat2: float, lon2: float):
    p = 0.017453292519943295
    hav = 0.5 - cos((lat2-lat1)*p)/2 + cos(lat1*p)*cos(lat2*p) * (1-cos((lon2-lon1)*p)) / 2
    return 12742 * asin(sqrt(hav))


def get_object_store(dataset_attributes):
    """Extract the object store id from the dataset attributes"""
    object_store = []
    for value in dataset_attributes.values():
        if value["object_store_id"]:
            object_store.append(value["object_store_id"])

    if len(set(object_store)) == 1:
        object_store = [object_store[0]]

    return object_store


def closest_destinations(destinations, objectstores, dataset_attributes):
    """Calculate the closest destination for each object store and return
    the list of destinations sorted by distance"""
    object_store = get_object_store(dataset_attributes)

    if len(object_store) == 0:
        # Return all destination IDs if no object store is in the dataset
        return [destination['id'] for destination in destinations]
    elif len(object_store) == 1:
        objectstore = objectstores[object_store[0]]
        out_destinations = []

        for destination in destinations:
            d_lat, d_lon = destination['context']['latitude'], destination['context']['longitude']
            o_lat, o_lon = objectstore['latitude'], objectstore['longitude']
            queue_size = destination['queued_job_count']
            out_dest = {"id": destination["id"], "distance": distance(o_lat, o_lon, d_lat, d_lon), "queue": queue_size}
            out_destinations.append(out_dest)

        # In this simple logic: give equal sorting weight to both the distance and the queue size 
        sorted_destinations = sorted(out_destinations, key=lambda d: (d['distance'], d['queue']))
        
        sorted_destinations = [k["id"] for k in sorted_destinations]

        return sorted_destinations
    else:
        # Calculate the minimum distance for each destination
        candidate_destinations = []

        for _, store_info in objectstores.items():
            o_lat, o_lon = store_info['latitude'], store_info['longitude']
            min_distance = float('inf')  # Initialize with infinity for comparison
            min_distance_dest = None

            for destination in destinations:
                d_lat, d_lon = destination['context']['latitude'], destination['context']['longitude']
                dist = distance(o_lat, o_lon, d_lat, d_lon)
                if dist < min_distance:
                    min_distance = dist
                    # min_distance_dest = destination['id']

            # candidate_destinations.append(min_distance_dest)
            candidate_destinations.append(destination)

        sorted_candidate_destinations = sorted(candidate_destinations, key=lambda q: q['queued_job_count'])
        sorted_candidate_destination_ids = [dest['id'] for dest in sorted_candidate_destinations]
        
        return sorted_candidate_destination_ids
