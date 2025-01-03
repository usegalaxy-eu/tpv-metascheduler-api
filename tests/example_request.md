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