from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from closest_location import closest_destination


app = FastAPI()


class DestinationRequest(BaseModel):
    destinations: List[dict]
    yaml_file: str
    input_string: str


class ProcessedResult(BaseModel):
    selected_destination_id: str


@app.post("/process_destinations", response_model=ProcessedResult)
async def process_destinations(data: DestinationRequest):

    final_destination = closest_destination(data.destinations, data.yaml_file, data.input_string)

    return {
        "selected_destination_id": final_destination["id"]
    }
