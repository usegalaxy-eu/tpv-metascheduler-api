Available test data inserted on 2025-01-06T10:59:23

`select * from "destination-queue-run-time"`

name: destination-queue-run-time
| time | avg_queue | avg_run | count | destination_id | max_queue | max_run | median_queue | median_run | min_queue | min_run | perc_95_queue | perc_95_run | perc_99_queue | perc_99_run | tool_id |
| ---- | --------- | ------- | ----- | -------------- | --------- | ------- | ------------ | ---------- | --------- | ------- | ------------- | ----------- | ------------- | ----------- | ------- |
| 2025-01-06T10:58:56.290173529Z | 4 | 2400 | 5 | condor_tpv | 10 | 5000 | 3.5 | 1800 | 2 | 200 | 7 | 4000 | 8 | 4500 | trinity |
| 2025-01-06T10:59:23.288272815Z | 15 | 7200 | 10 | condor_us | 35 | 18000 | 12 | 5000 | 10 | 400 | 25 | 15000 | 30 | 16000 | spades |
| 2025-01-06T10:59:23.310876297Z | 3.5 | 3600 | 3 | pulsar_be01 | 8 | 10000 | 3 | 3000 | 2 | 300 | 6 | 8000 | 7 | 9000 | bwa |
| 2025-01-06T10:59:23.332525592Z | 6.5 | 5400 | 12 | pulsar_us01 | 25 | 18000 | 6 | 5000 | 5 | 500 | 15 | 15000 | 20 | 16000 | hisat2 |
| 2025-01-06T10:59:23.354292289Z | 10.5 | 7200 | 8 | pulsar_eu01 | 30 | 25000 | 8 | 7000 | 5 | 600 | 15 | 20000 | 20 | 22000 | bowtie2 |
| 2025-01-06T10:59:23.375756986Z | 8 | 3600 | 20 | pulsar_asia01 | 20 | 15000 | 7 | 3000 | 3 | 300 | 12 | 10000 | 15 | 12000 | blast |
| 2025-01-06T10:59:23.397077463Z | 5.5 | 3600 | 8 | pulsar_fr | 15 | 10000 | 5 | 3000 | 3 | 600 | 10 | 8000 | 12 | 9000 | bwa |
| 2025-01-06T10:59:23.421365716Z | 7.5 | 5400 | 12 | pulsar_fr01_tpv | 20 | 18000 | 7 | 5000 | 5 | 500 | 12 | 15000 | 15 | 16000 | hisat2 |
| 2025-01-06T10:59:23.443104883Z | 5 | 2400 | 10 | pulsar_de | 12 | 5000 | 4 | 2000 | 2 | 300 | 8 | 4000 | 10 | 4500 | bowtie2 |
| 2025-01-06T10:59:23.466992508Z | 6.5 | 3600 | 6 | pulsar_in | 14 | 11000 | 6 | 3000 | 4 | 600 | 10 | 9000 | 12 | 10000 | trinity |
| 2025-01-06T10:59:23.489077131Z | 4 | 3600 | 5 | pulsar_cz01_tpv | 8 | 10000 | 3.5 | 3000 | 2 | 300 | 6 | 8000 | 7 | 9000 | spades |
| 2025-01-06T10:59:23.511607684Z | 8 | 3600 | 7 | pulsar_sk01_tpv | 20 | 15000 | 7 | 3000 | 3 | 300 | 12 | 10000 | 15 | 12000 | blast |
| 2025-01-06T10:59:23.534286394Z | 15.5 | 5400 | 15 | pulsar_uk | 30 | 13000 | 14 | 5000 | 10 | 300 | 20 | 10500 | 25 | 12000 | hisat2 |

`select * from queue_by_destination`

name: queue_by_destination
| time | count | destination_id | state |
| ---- | ----- | -------------- | ----- |
| 2025-01-06T10:55:35.260525392Z | 8 | condor_tpv | queued |
| 2025-01-06T10:55:35.298107771Z | 4 | condor_tpv | running |
| 2025-01-06T10:55:35.320182726Z | 12 | condor_us | queued |
| 2025-01-06T10:55:35.345935921Z | 8 | condor_us | running |
| 2025-01-06T10:55:35.368691202Z | 5 | pulsar_be01 | queued |
| 2025-01-06T10:55:35.39199186Z | 5 | pulsar_be01 | running |
| 2025-01-06T10:55:35.41486518Z | 6 | pulsar_us01 | queued |
| 2025-01-06T10:55:35.4380563Z | 6 | pulsar_us01 | running |
| 2025-01-06T10:55:35.460375613Z | 10 | pulsar_eu01 | queued |
| 2025-01-06T10:55:35.482570896Z | 3 | pulsar_eu01 | running |
| 2025-01-06T10:55:35.504331712Z | 2 | pulsar_asia01 | queued |
| 2025-01-06T10:55:35.528102368Z | 8 | pulsar_asia01 | running |
| 2025-01-06T10:55:35.550833728Z | 4 | pulsar_fr | queued |
| 2025-01-06T10:55:35.572515715Z | 10 | pulsar_fr | running |
| 2025-01-06T10:55:35.595013946Z | 8 | pulsar_fr01_tpv | queued |
| 2025-01-06T10:55:35.616447843Z | 6 | pulsar_fr01_tpv | running |
| 2025-01-06T10:55:35.639569523Z | 5 | pulsar_de | queued |
| 2025-01-06T10:55:35.662562933Z | 5 | pulsar_de | running |
| 2025-01-06T10:55:35.684874386Z | 6 | pulsar_in | queued |
| 2025-01-06T10:55:35.707305998Z | 4 | pulsar_in | running |
| 2025-01-06T10:55:35.72989129Z | 3 | pulsar_cz01_tpv | queued |
| 2025-01-06T10:55:35.753371928Z | 2 | pulsar_cz01_tpv | running |
| 2025-01-06T10:55:35.776896285Z | 10 | pulsar_sk01_tpv | queued |
| 2025-01-06T10:55:35.799089929Z | 5 | pulsar_sk01_tpv | running |
| 2025-01-06T10:55:35.821539921Z | 7 | pulsar_uk | queued |
| 2025-01-06T10:55:35.844172022Z | 8 | pulsar_uk | running |

`select * from htcondor_cluster_usage`

name: htcondor_cluster_usage
| time | claimed_busy_slots | claimed_cpus | claimed_gpus | claimed_loadavg | claimed_memory | classad | destination_id | destination_status | querytime | total_detected_cpus | total_gpu_slots | total_loadavg | total_memory | total_slots | unclaimed_cpus | unclaimed_gpus | unclaimed_idle_slots | unclaimed_loadavg | unclaimed_memory |
| ---- | ------------------ | ------------ | ------------ | --------------- | -------------- | ------- | -------------- | ------------------ | --------- | ------------------- | --------------- | ------------- | ------------ | ----------- | -------------- | -------------- | -------------------- | ----------------- | ---------------- |
| 2025-01-06T10:53:10.309840161Z | 0 | 0 | 0 | 0 | machine | condor_tpv | online | 1730910000 | 32 | 0 | 64000 | 4 | 32 | 4 | 0 | 64000 |
| 2025-01-06T10:53:29.65364037Z | 2 | 16 | 4 | 32000 | machine | condor_us | online | 1730910100 | 32 | 8 | 64000 | 4 | 16 | 2 | 4 | 32000 |
| 2025-01-06T10:53:29.675302857Z | 3 | 30 | 15 | 62000 | machine | pulsar_be01 | online | 1730910200 | 32 | 29.5 | 64000 | 4 | 2 | 1 | 14.5 | 2000 |
| 2025-01-06T10:53:29.695709169Z | 2 | 10 | 7.5 | 20000 | machine | pulsar_us01 | online | 1730910300 | 32 | 15 | 64000 | 4 | 22 | 2 | 7.5 | 44000 |
| 2025-01-06T10:53:29.716481219Z | 3 | 20 | 12.5 | 40000 | machine | pulsar_eu01 | online | 1730910400 | 32 | 25 | 64000 | 4 | 12 | 1 | 12.5 | 24000 |
| 2025-01-06T10:53:29.737482969Z | 1 | 5 | 2 | 10000 | machine | pulsar_asia01 | online | 1730910500 | 32 | 4 | 64000 | 4 | 27 | 3 | 2 | 54000 |
| 2025-01-06T10:53:29.757587113Z | 6 | 50 | 22.5 | 100000 | machine | pulsar_fr | online | 1730910600 | 64 | 45 | 128000 | 8 | 14 | 2 | 22.5 | 28000 |
| 2025-01-06T10:53:29.777972306Z | 2 | 15 | 5.5 | 30000 | machine | pulsar_fr01_tpv | online | 1730910700 | 32 | 10.5 | 64000 | 4 | 17 | 2 | 5 | 34000 |
| 2025-01-06T10:53:29.798358917Z | 1 | 8 | 2 | 16000 | machine | pulsar_de | online | 1730910800 | 32 | 8 | 64000 | 4 | 24 | 3 | 6 | 48000 |
| 2025-01-06T10:53:29.818951029Z | 1 | 12 | 8 | 24000 | machine | pulsar_in | online | 1730910900 | 16 | 12 | 32000 | 2 | 4 | 1 | 4 | 8000 |
| 2025-01-06T10:53:29.83956168Z | 2 | 10 | 7.5 | 20000 | machine | pulsar_cz01_tpv | online | 1730911000 | 32 | 15 | 64000 | 4 | 22 | 2 | 7.5 | 44000 |
| 2025-01-06T10:53:29.861170816Z | 1 | 5 | 2 | 10000 | machine | pulsar_sk01_tpv | online | 1730911100 | 32 | 4 | 64000 | 4 | 27 | 3 | 2 | 54000 |
| 2025-01-06T10:53:29.881392019Z | 6 | 45 | 20 | 90000 | machine | pulsar_uk | online | 1730911200 | 64 | 40 | 128000 | 8 | 19 | 2 | 20 | 38000 |

Example json request
```
{
    "objectstores": {
        "object_store_usa": {
            "latitude": 37.7749,
            "longitude": -122.4194  # Close to pulsar_us01, testing proximity efficiency
        },
        "object_store_europe": {
            "latitude": 48.8566,
            "longitude": 2.3522    # Close to pulsar_fr, testing data efficiency
        },
        "object_store_asia": {
            "latitude": 35.6895,
            "longitude": 139.6917  # Farther from most destinations, testing long-distance access
        },
        "object_store_australia": {
            "latitude": -25.2744,
            "longitude": 133.7751  # Far from most locations, testing global access impact
        }
    },

    "datasets": {
        "0": {
            "object_store_id": "object_store_usa",
            "size": 50000000000.0    # 50 GB, a smaller dataset
        },
        "1": {
            "object_store_id": "object_store_europe",
            "size": 200000000000.0   # 200 GB, moderate-sized dataset
        },
        "2": {
            "object_store_id": "object_store_asia",
            "size": 1000000000000.0  # 1 TB, large dataset
        },
        "3": {
            "object_store_id": "object_store_australia",
            "size": 5000000000000.0  # 5 TB, very large dataset
        }
    },

    "job_info":
    {
        "tool_id": "trinity",    # Tool requiring moderate resources
        "mem": 16,               # 16 GB memory requirement
        "cores": 4,              # Moderate CPU requirement
        "gpus": 1                # Moderate GPU requirement
    },
    {
        "tool_id": "spades",     # Tool requiring high memory
        "mem": 32,               # High memory requirement
        "cores": 8,              # High CPU demand
        "gpus": 2                # GPU-intensive
    },
    {
        "tool_id": "bwa",        # Lightweight job with low resource needs
        "mem": 8,                # Low memory requirement
        "cores": 2,              # Low CPU requirement
        "gpus": 0                # No GPU needed
    },
    {
        "tool_id": "hisat2",     # Moderate job that may run well on most destinations
        "mem": 12,
        "cores": 3,
        "gpus": 0
    }


    "destinations": [
        {
            "id": "pulsar_us01",
            "latitude": 37.7749,
            "longitude": -122.4194,
            "queued_job_count": 5,   # Moderate queue size
            "running_job_count": 10  # High number of jobs running
        },
        {
            "id": "pulsar_uk",
            "latitude": 51.5074,
            "longitude": -0.1278,
            "queued_job_count": 10,  # Higher queue load simulating backlog
            "running_job_count": 3   # Fewer jobs running
        },
        {
            "id": "pulsar_de",
            "latitude": 50.1109,
            "longitude": 8.6821,
            "queued_job_count": 5,   # Balanced queue and running jobs
            "running_job_count": 5   # Average load scenario
        },
        {
            "id": "pulsar_fr",
            "latitude": 48.8566,
            "longitude": 2.3522,
            "queued_job_count": 0,   # No queue, indicating immediate availability
            "running_job_count": 6   # Average workload
        },
        {
            "id": "condor_us",
            "latitude": 34.0522,
            "longitude": -118.2437,
            "queued_job_count": 20,  # High queue load to simulate busy destination
            "running_job_count": 15  # High running job count
        }
    ]
}
```