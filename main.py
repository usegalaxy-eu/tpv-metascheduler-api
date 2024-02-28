from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List, Dict
from closest_location import closest_destinations


app = FastAPI()


class DestinationRequest(BaseModel):
    destinations: List[dict] = Field(examples=[[{"id":"pulsar_italy",
                                                "context":{"latitude": 50.0689816,
                                                           "longitude": 19.9070188},
                                                "queued_job_count": 10}]])
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
