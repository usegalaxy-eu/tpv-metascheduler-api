import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List, Dict
from closest_location import get_sorted_destinations
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
    mem: float
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
    objectstores: Dict[str, ObjectStoreInfo]
    datasets: Dict[int, DatasetInfo]
    job_info: JobInfo
    destinations: List[DestinationInfo]

    class Config:
        schema_extra = {
            "example": {
                "objectstores": {
                    "object_store_australia": {"latitude": -26.4390917, "longitude": 133.281323}
                },
                "datasets": {
                    "0": {"object_store_id": "object_store_australia", "size": 1073741824000.0}
                },
                "job_info": {"tool_id": "trinity", "mem": 8, "cores": 2, "gpus": 0},
                "destinations": [
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


def influx_client():
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
    client = InfluxDBClient(host=address, port=port, database=db, ssl=True, verify_ssl=True,
                            username=influxdb_username, password=influxdb_password)

    return client

# def retrieve_sorted_destinations(request_data):


@app.post("/process_data", response_model=ProcessedResult)
async def process_data(data: RequestModel):
    client = influx_client()
    destination_metrics = destination_statistics(client, data)

    sorted_destinations = get_sorted_destinations(
        data.job_info,
        destination_metrics,
        data.objectstores,
        data.datasets
        )
    print(sorted_destinations)

    return {
        "sorted_destinations": sorted_destinations
    }
