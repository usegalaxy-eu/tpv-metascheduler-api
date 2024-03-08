from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List, Dict
from closest_location import closest_destinations


app = FastAPI()


class DestinationRequest(BaseModel):
    destinations: List[dict] = Field(examples=[[{"id":"pulsar_italy",
                                                "context":{"latitude": 50.0689816,
                                                           "longitude": 19.9070188},
                                                "queued_job_count": 10,
                                                'total_job_count': 39, 
                                                'avg_queue_time': 1136.874096, 
                                                'min_queue_time': 0.828691, 
                                                'median_queue_time': 3.045126, 
                                                'perc_95_queue_time': 6262.695555, 
                                                'perc_99_queue_time': 17540.290275, 
                                                'max_queue_time': 22867.276603,
                                                'avg_run_time': 14.982373, 
                                                'min_run_time': 7.343693, 
                                                'median_run_time': 8.905191, 
                                                'perc_95_run_time': 40.208785, 
                                                'perc_99_run_time': 47.76481, 
                                                'max_run_time': 48.391205}]])
    objectstores: Dict[str, dict] = Field(examples=[{"object_store_italy_S3_01": {
                                                    "latitude": 50.0689816,
                                                    "longitude": 19.9070188,}}])
    dataset_attributes: Dict = Field(examples=[{"dataset_italy": {
                                                "object_store_id": "object_store_italy_S3_01",
                                                "size": 12345678}}])


class ProcessedResult(BaseModel):
    sorted_destinations: List = Field(examples=[["pulsar_italy"]])


@app.post("/process_destinations", response_model=ProcessedResult)
async def process_destinations(data: DestinationRequest):

    sorted_destinations = closest_destinations(data.destinations, data.objectstores, data.dataset_attributes)

    return {
        "sorted_destinations": sorted_destinations
    }
