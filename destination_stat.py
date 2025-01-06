import requests
from collections import defaultdict


def calculate_median(values):
    # Sort the values
    values.sort()

    # Calculate the median
    n = len(values)
    if n % 2 == 1:
        median = values[n // 2]
    else:
        median = (values[n // 2 - 1] + values[n // 2]) / 2

    return median


def group_and_calculate_medians(data, group_key, value_key):
    grouped_data = defaultdict(list)

    # Group the data by the specified group_key
    for item in data:
        grouped_data[item[group_key]].append(item[value_key])

    # Calculate the median for each group
    medians = {state: calculate_median(counts) for state, counts in grouped_data.items()}

    return medians


def query_construction(destination, tool_id):

    queries = {}
    # TODO: for the test cases add a where clause for the date
    queries['dest_queue_count_query'] = f"SELECT last(count) FROM queue_by_destination WHERE \"state\"='running' AND \"destination_id\"='{destination}'"
    queries['dest_run_count_query'] = f"SELECT last(count) FROM queue_by_destination WHERE \"state\"='queued' AND \"destination_id\"='{destination}'"
    # dest_queue_count_query = "SELECT median(count) FROM queue_by_destination GROUP BY \"destination_id\", state ORDER BY time DESC LIMIT 10"
    queries['dest_tool_median_queue_time_query'] = f"SELECT last(\"median_queue\") FROM \"destination-queue-run-time\" WHERE \"tool_id\"='{tool_id}' AND \"destination_id\"='{destination}'"
    queries['dest_tool_median_run_time_query'] = f"SELECT last(\"median_run\") FROM \"destination-queue-run-time\" WHERE \"tool_id\"='{tool_id}' AND \"destination_id\"='{destination}'"
    queries['dest_unconsumed_cpu_query'] = f"SELECT last(\"unclaimed_cpus\") FROM \"htcondor_cluster_usage\" WHERE \"destination_id\"='{destination}'"
    queries['dest_unconsumed_mem_query'] = f"SELECT last(\"unclaimed_memory\") FROM \"htcondor_cluster_usage\" WHERE \"destination_id\"='{destination}'"
    queries['dest_status'] = f"SELECT last(\"destination_status\") FROM \"htcondor_cluster_usage\" WHERE \"destination_id\"='{destination}'"

    return queries


def get_influx_results(influx_client, query: str):
    print("QUERY: ", query)
    results = list(influx_client.query(query).get_points())
    print("RESULTS: ", results)
    if results:
        # if results[0]["last"].isdigit():
        #     return float(results[0]["last"])
        # else:
        return results[0]["last"]


def destination_statistics(influx_client, static_data):

    destination_metrics = []
    tool_id = static_data.job_info.tool_id
    for dest in static_data.destinations:
        destination = dest.id
        queries = query_construction(destination, tool_id)

        metrics = {}
        metrics["destination_id"] = destination
        metrics["dest_queue_count"] = get_influx_results(influx_client, queries['dest_queue_count_query']) or 0
        metrics["dest_run_count"] = get_influx_results(influx_client, queries['dest_run_count_query']) or 0
        metrics["dest_tool_median_queue_time"] = get_influx_results(influx_client, queries['dest_tool_median_queue_time_query']) or 0
        metrics["dest_tool_median_run_time"] = get_influx_results(influx_client, queries['dest_tool_median_run_time_query']) or 0
        metrics["dest_unconsumed_cpu"] = get_influx_results(influx_client, queries['dest_unconsumed_cpu_query']) or 0
        metrics["dest_unconsumed_mem"] = get_influx_results(influx_client, queries['dest_unconsumed_mem_query']) or 0
        metrics["dest_status"] = get_influx_results(influx_client, queries['dest_status']) or ""
        metrics["latitude"] = dest.latitude
        metrics["longitude"] = dest.longitude

        destination_metrics.append(metrics)

    return destination_metrics
