import pytest
import json
from dotenv import load_dotenv
from fastapi.testclient import TestClient
from main import app  # Import your FastAPI app

client = TestClient(app)

@pytest.fixture(scope="function", autouse=True)
def load_environment_variables():
    """
    Fixture to load environment variables from a .env file for the tests.
    """
    load_dotenv(".env")  # Load variables from .env file

def test_process_data():
    # Load input data from JSON file
    with open("tests/example_request1.json", "r") as f:
        input_data = json.load(f)

    # Expected output (in this case, same as input wrapped in a message)
    expected_response = {
        'sorted_destinations': ['pulsar_us01']
    }

    # Send POST request
    response = client.post("/process_data", json=input_data)
    print(response.json())

    # Assertions
    assert response.status_code == 200
    assert response.json() == expected_response
