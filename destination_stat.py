import requests


def fetch_influx_data(url, queries, db="telegraf"):
    params = {
        "db": db,
        "q": ";".join(queries)
    }
    response = requests.get(url, params=params)
    return response.json()


def parse_series(series):
    columns = series['columns']
    values = series['values']
    return columns, values

def process_timing_series(results):
    timing_series = results['results'][0]['series'][0]
    columns, values = parse_series(timing_series)
    timing_data = [dict(zip(columns, value)) for value in values]
    return timing_data


def process_queue_series(results):
    queue_series = results['results'][1]['series'][0]
    columns, values = parse_series(queue_series)
    queue_data = [dict(zip(columns, value)) for value in values]
    return queue_data

def process_alloc_series(results):
    alloc_series = results['results'][2]['series'][0]
    columns, values = parse_series(alloc_series)
    alloc_data = [dict(zip(columns, value)) for value in values]
    return alloc_data

def process_candidate_destinations(candidate_destinations, queue_data, alloc_data, series, stat_indices, stat_columns):
    candidate_destinations_list = []
    for dest in candidate_destinations:
        dest_dict = dest.to_dict()
        dest_dict["queued_job_count"] = app.model.context.query(model.Job).filter(model.Job.state == "queued", model.Job.destination_id == dest.dest_name).count()

        for row in series:
            stats = [row[i] for i in stat_indices]
            if stats[0] == dest.dest_name and stats[1] == job.tool_id:
                dest_dict.update(zip(stat_columns, stats))
                dest_dict["galaxy_db_query_time"] = dest_dict.pop("time")
                dest_dict["job_count_in_time_window"] = dest_dict.pop("count")
                dest_dict["median_queue_time"] = dest_dict.pop("median_queue")
                dest_dict["median_run_time"] = dest_dict.pop("median_run")
                break

        for row in queue_data:
            dest_dict[row['state'] + "_count"] = row['count']

        for row in alloc_data:
            dest_dict["cpu_usage_perc"] = row['cores']
            dest_dict["mem_usage_perc"] = row['memory']

        candidate_destinations_list.append(dest_dict)
    return candidate_destinations_list


def destination_statistics(influx_url, queries):

    results = fetch_influx_data(influx_url, queries)
    print(results)
    timing_data = process_timing_series(results)
    queue_data = process_queue_series(results)
    alloc_data = process_alloc_series(results)
    # candidate_destinations_list = process_candidate_destinations(candidate_destinations, queue_data, alloc_data, series, stat_indices, stat_columns)

    print(timing_data)
    print(queue_data)
    print(alloc_data)
    # series, stat_indices = extract_statistics(results, stat_columns)
    # candidate_destinations_list = process_candidate_destinations(candidate_destinations, series, stat_indices, stat_columns, results)
