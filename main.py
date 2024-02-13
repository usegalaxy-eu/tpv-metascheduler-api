from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict
from closest_location import closest_destinations


app = FastAPI()


class DestinationRequest(BaseModel):
    destinations: List[dict]
    objectstores: Dict[str, dict]
    dataset_attributes: Dict


class ProcessedResult(BaseModel):
    sorted_destinations: List


@app.post("/process_destinations", response_model=ProcessedResult)
async def process_destinations(data: DestinationRequest):

    sorted_destinations = closest_destinations(data.destinations, data.objectstores, data.dataset_attributes)

    return {
        "sorted_destinations": sorted_destinations
    }