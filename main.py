import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List, Dict
from closest_location import closest_destinations
from destination_stat import destination_statistics
from influxdb import InfluxDBClient

app = FastAPI()


class ObjectStoreInfo(BaseModel):
    latitude: float
    longitude: float

    class Config:
        schema_extra = {
            "example": {
                "latitude": 50.0689816,
                "longitude": 19.9070188
            }
        }


class DatasetInfo(BaseModel):
    object_store_id: str
    size: float

    class Config:
        schema_extra = {
            "example": {
                "object_store_id": "object_store_australia",
                "size": 1073741824000.0
            }
        }


class JobInfo(BaseModel):
    tool_id: str
    mem: int
    cores: int
    gpus: int

    class Config:
        schema_extra = {
            "example": {
                "tool_id": "trinity",
                "mem": 8,
                "cores": 2,
                "gpus": 0
            }
        }


class DestinationInfo(BaseModel):
    id: str
    latitude: float
    longitude: float
    queued_job_count: int
    running_job_count: int

    class Config:
        schema_extra = {
            "example": {
                "id": "pulsar_italy",
                "latitude": 50.0689816,
                "longitude": 19.9070188,
                "queued_job_count": 5,
                "running_job_count": 5
            }
        }


class RequestModel(BaseModel):
    static_objectstores_info: Dict[str, ObjectStoreInfo]
    static_dataset_info: Dict[int, DatasetInfo]
    static_job_info: JobInfo
    current_dest_info: List[DestinationInfo]

    class Config:
        schema_extra = {
            "example": {
                "static_objectstores_info": {
                    "object_store_australia": {"latitude": -26.4390917, "longitude": 133.281323}
                },
                "static_dataset_info": {
                    "0": {"object_store_id": "object_store_australia", "size": 1073741824000.0}
                },
                "static_job_info": {"tool_id": "trinity", "mem": 8, "cores": 2, "gpus": 0},
                "current_dest_info": [
                    {
                        "id": "slurm_germany",
                        "latitude": 51.1642292,
                        "longitude": 10.4541192,
                        "queued_job_count": 5,
                        "running_job_count": 5
                    },
                    {
                        "id": "condor_france",
                        "latitude": 46.71109,
                        "longitude": 1.7191036,
                        "queued_job_count": 5,
                        "running_job_count": 5
                    },
                    {
                        "id": "pulsar_australia",
                        "latitude": -26.4390917,
                        "longitude": 133.281323,
                        "queued_job_count": 5,
                        "running_job_count": 5
                    }
                ]
            }
        }


class ProcessedResult(BaseModel):
    sorted_destinations: List = Field(examples=[["pulsar_italy"]])


@app.post("/process_data", response_model=ProcessedResult)
async def process_data(data: RequestModel):

    sorted_destinations = closest_destinations(
        data.current_dest_info,
        data.static_objectstores_info,
        data.static_dataset_info
        )

    return {
        "sorted_destinations": sorted_destinations
    }



queries = [
    "SELECT * FROM queue_by_destination LIMIT 10",
    "SELECT median(count) FROM queue_by_destination GROUP BY \"destination_id\", state ORDER BY time DESC LIMIT 10",
    "SELECT \"tool_id\", \"destination_id\", count, \"median_queue\", \"median_run\" FROM \"destination-queue-run-time\" ORDER BY time DESC LIMIT 10",
    "SELECT * FROM \"cluster.queue\" WHERE host = 'vgcn-pulsar-central-manager.usegalaxy.be' ORDER BY time DESC LIMIT 6",
    "SELECT * FROM \"cluster.alloc\" WHERE host = 'vgcn-pulsar-central-manager.usegalaxy.be' ORDER BY time DESC LIMIT 10",
]
# Retrieve the config vars
address = os.getenv('INFLUXDB_HOST')
port = os.getenv('INFLUXDB_PORT')
db = os.getenv('INFLUXDB_DATABASE')
influxdb_username = os.getenv('INFLUXDB_USERNAME')
influxdb_password = os.getenv('INFLUXDB_PASSWORD')

# Ensure the variables are set
if not influxdb_username or not influxdb_password:
    raise ValueError("InfluxDB credentials are not set in environment variables")

# Initialize the InfluxDB client
client = InfluxDBClient(host=address, port=port, database=db, ssl=True,
                        username=influxdb_username, password=influxdb_password)


def parse_results(results):
    for key, value in results.items():
        print("TAGS")
        print(key)
        print("SERIES")
        print(list(value))
    # parsed_series = [dict(zip(columns, value)) for value in values]
    # return parsed_series


for query in queries:
    results = client.query(query)
    # print(len(results.items()))
    parse_results(results)


# destination_statistics(influx_url, queries)

# class DestinationRequest(BaseModel):
#     destinations: List[dict] = Field(examples=[[{"id":"pulsar_italy",
#                                                 "context":{"latitude": 50.0689816,
#                                                            "longitude": 19.9070188},
#                                                 "queued_job_count": 10,
#                                                 'total_job_count': 39, 
#                                                 'avg_queue_time': 1136.874096, 
#                                                 'min_queue_time': 0.828691, 
#                                                 'median_queue_time': 3.045126, 
#                                                 'perc_95_queue_time': 6262.695555, 
#                                                 'perc_99_queue_time': 17540.290275, 
#                                                 'max_queue_time': 22867.276603,
#                                                 'avg_run_time': 14.982373, 
#                                                 'min_run_time': 7.343693, 
#                                                 'median_run_time': 8.905191, 
#                                                 'perc_95_run_time': 40.208785, 
#                                                 'perc_99_run_time': 47.76481, 
#                                                 'max_run_time': 48.391205}]])
#     objectstores: Dict[str, dict] = Field(examples=[{"object_store_italy_S3_01": {
#                                                     "latitude": 50.0689816,
#                                                     "longitude": 19.9070188,}}])
#     dataset_attributes: Dict = Field(examples=[{"dataset_italy": {
#                                                 "object_store_id": "object_store_italy_S3_01",
#                                                 "size": 12345678}}])
