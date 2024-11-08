from math import cos, asin, sqrt


def distance(lat1: float, lon1: float, lat2: float, lon2: float):
    p = 0.017453292519943295
    hav = 0.5 - cos((lat2-lat1)*p)/2 + cos(lat1*p)*cos(lat2*p) * (1-cos((lon2-lon1)*p)) / 2
    return 12742 * asin(sqrt(hav))


def get_object_store(dataset_attributes):
    """Extract the object store id from the dataset attributes"""
    object_store = []
    for value in dataset_attributes.values():
        if value.object_store_id:
            object_store.append(value.object_store_id)

    if len(set(object_store)) == 1:
        object_store = [object_store[0]]

    return object_store


def closest_destination(destination, objectstores, dataset_attributes) -> float:
    """
    Calculates the minimum distance between a given destination and the object store(s).
    """
    object_store = get_object_store(dataset_attributes)

    # If there is no object store, return infinity
    if not object_store:
        return float('inf')

    d_lat, d_lon = destination.latitude, destination.longitude
    min_distance = float('inf')

    # Calculate distance to each object store and keep the minimum
    for object_store_id in object_store:
        object_store_info = objectstores.get(object_store_id)
        if object_store_info:
            o_lat, o_lon = object_store_info.latitude, object_store_info.longitude
            min_distance = min(min_distance, distance(o_lat, o_lon, d_lat, d_lon))

    return min_distance


def calculate_matching_score(destination: dict) -> float:
    """
    Calculate the matching score between a job and a destination
    """
    median_waiting_time = destination.get('dest_tool_median_queue_time', None)
    queue_size = destination.get('dest_queue_count', 1)
    median_running_time = destination.get('dest_tool_median_run_time', None)
    running_jobs = destination.get('dest_run_count', 1)

    # Queue matching factor (qm).
    if median_waiting_time > 0 and queue_size > 0:
        qm = 1 / (median_waiting_time * queue_size)
    else:
        qm = float('inf')

    # Compute matching factor (cm).
    if median_running_time > 0 and running_jobs > 0:
        cm = 1 / (median_running_time * running_jobs)
    else:
        cm = float('inf')

    # Final matching score
    return qm + cm


def get_sorted_destinations(job_requirements: dict, destinations: list, objectstores: dict, dataset_attributes: dict) -> list:
    """
    Sorts the destinations based on the matching score and distance to the input data location.
    """
    sorted_destinations = []
    cpu_required = job_requirements['cpu_cores']
    memory_required = job_requirements['memory']

    # Filter out destinations that can't meet basic requirements based on the "real-time" data
    viable_destinations = []
    for dest in destinations:
        # Check if the destination_status is 'online'
        if dest['dest_status'] == 'online':
            # Check if the destination has enough resources
            if dest['dest_unconsumed_cpu'] > cpu_required and dest['dest_unconsumed_mem'] > memory_required:
                # Calculate the distance to the input data location
                dest['distance_to_data'] = closest_destination(dest, objectstores, dataset_attributes)
                viable_destinations.append(dest)

    # Fallback case if no viable destinations are found (e.g. no destination has enough resources)
    if not viable_destinations:
        for dest in destinations:
            dest['distance_to_data'] = closest_destination(dest, objectstores, dataset_attributes)
        sorted_destinations = sorted(destinations, key=lambda x: x['distance_to_data'])
        return [dest['destination_id'] for dest in sorted_destinations]

    # Sort by distance to input data location (ascending)
    viable_destinations.sort(key=lambda x: x['distance_to_data'])

    # Calculate matching scores for each viable destination
    for dest in viable_destinations:
        dest['matching_score'] = calculate_matching_score(dest)

    # Sort by matching score (descending)
    viable_destinations.sort(key=lambda x: x['matching_score'], reverse=True)

    sorted_destinations = [dest['destination_id'] for dest in viable_destinations]
    return sorted_destinations
