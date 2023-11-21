from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict
from closest_location import closest_destination


app = FastAPI()


class DestinationRequest(BaseModel):
    destinations: List[dict]
    objectstores: Dict[str, dict]
    selected_objectstore: str


class ProcessedResult(BaseModel):
    selected_destination_id: str


@app.post("/process_destinations", response_model=ProcessedResult)
async def process_destinations(data: DestinationRequest):

    final_destination = closest_destination(data.destinations, data.objectstores, data.selected_objectstore)

    return {
        "selected_destination_id": final_destination["id"]
    }
