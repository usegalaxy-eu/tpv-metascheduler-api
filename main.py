from fastapi import FastAPI, HTTPException, File, UploadFile, Form
from typing import List, Optional
import yaml
from pydantic import BaseModel, create_model, validator

from tpv.core.entities import Destination

from closest_location import closest_destination


objectstore_loc_path = "tests/fixtures/object_store_locations.yml"
selected_object_store = "object_store_australia"


app = FastAPI()


def process_destinations(destinations: List[dict], yaml_file: UploadFile = File(None), string_input: Optional[str] = Form(None)):
    # Process the list of dictionaries
    processed_destinations = []
    for destination in destinations:
        # Example processing: extracting 'id' and 'runner'
        processed_info = f"ID: {destination['id']}, Runner: {destination['runner']}"
        processed_destinations.append(processed_info)

    # Process the YAML file
    yaml_data = None
    if yaml_file:
        yaml_data = yaml.safe_load(yaml_file.file.read())
    
    # Process the string input
    string_data = None
    if string_input:
        string_data = f"String input: {string_input}"

    return {
        "processed_destinations": processed_destinations,
        "yaml_data": yaml_data,
        "string_data": string_data
    }


@app.post("/process_input")
async def process_input(destinations: List[dict], yaml_file: UploadFile = File(None), string_input: Optional[str] = Form(None)):
    return process_destinations(destinations, yaml_file, string_input)
