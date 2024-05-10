import requests

# URL of local influxDB
influx_url = "http://127.0.0.1:8086/query"

queries = [
    "SELECT * FROM \"destination-queue-run-time\"  WHERE time > now() - 30m",
    "SELECT * FROM \"cluster.queue\" WHERE host = 'vgcn-pulsar-central-manager.usegalaxy.be' LIMIT 6;",
    "SELECT * FROM \"cluster.alloc\" WHERE host = 'vgcn-pulsar-central-manager.usegalaxy.be' LIMIT 10;",
]

params = {
    "db": "telegraf",
    "q": ";".join(queries)
}
response = requests.get(influx_url, params=params)
results = response.json()

columns = results['results'][0]['series'][0]['columns']
stat_columns = ['destination_id', 'tool_id', 'time', 'count', 'median_queue', 'median_run']
stat_indices = [columns.index(c) for c in stat_columns]
#stat_indices = [i for i,l in enumerate(columns) if l in stat_columns]
series = results['results'][0]['series'][0]['values']