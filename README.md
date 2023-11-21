# tpv-metascheduler-api

Metascheduler for TPV as Service

1. create a venv

   ```python
   
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

2. Run the API locally:
   `uvicorn main:app --reload`
3. Testing the API with input data:

   1. SwaggerUI: <http://127.0.0.1:8000/docs>
      Try out >  Fill out the request body:
      Request body:

      ```json
      {
         "destinations": [
            {
               "id": "pulsar_italy",
               "abstract": false,
               "runner": "general_pulsar_1",
               "destination_name_override": "pulsar_italy",
               "cores": null,
               "mem": null,
               "gpus": null,
               "min_cores": null,
               "min_mem": null,
               "min_gpus": null,
               "max_cores": null,
               "max_mem": null,
               "max_gpus": null,
               "min_accepted_cores": null,
               "min_accepted_mem": null,
               "min_accepted_gpus": null,
               "max_accepted_cores": 8,
               "max_accepted_mem": 32,
               "max_accepted_gpus": null,
               "env": null,
               "params": null,
               "resubmit": null,
               "scheduling": {
               "require": ["pulsar"],
               "prefer": [],
               "accept": ["general"],
               "reject": []
               },
               "inherits": null,
               "context": { 
                  "latitude": 50.0689816, 
                  "longitude": 19.9070188 },
               "rules": {},
               "tags": null
            },
            {
               "id": "slurm_poland",
               "abstract": false,
               "runner": "slurm",
               "destination_name_override": "slurm_poland",
               "cores": null,
               "mem": null,
               "gpus": null,
               "min_cores": null,
               "min_mem": null,
               "min_gpus": null,
               "max_cores": null,
               "max_mem": null,
               "max_gpus": null,
               "min_accepted_cores": null,
               "min_accepted_mem": null,
               "min_accepted_gpus": null,
               "max_accepted_cores": 16,
               "max_accepted_mem": 64,
               "max_accepted_gpus": null,
               "env": null,
               "params": null,
               "resubmit": null,
               "scheduling": {
               "require": [],
               "prefer": [],
               "accept": ["slurm"],
               "reject": []
               },
               "inherits": null,
               "context": { 
                  "latitude": 51.9189046, 
                  "longitude": 19.1343786 },
               "rules": {},
               "tags": null
            }
         ],
         "objectstores": {
            "object_store_italy_S3_01": {
               "latitude": 50.0689816,
               "longitude": 19.9070188,
               "other_stuff_that_we_find_useful": "foobar"
            },
            "object_store_poland": {
               "latitude": 51.9189046,
               "longitude": 19.1343786,
               "other_stuff_that_we_find_useful": "foobar"
            }
         },
         "selected_objectstore": "object_store_poland"
      }
      ```

   2. curl
      The Swagger UI can give you a curl version of your request after executing
   3. using a python script with the requests or httpx library
      There is an example of how to do this with TPV:
      `tpv-metascheduler-api/example_tpv_config_locations_api.yml`
      This config can be set up with a galaxy instance or by cloning the TPV repo (the example currently depends on an open PR to this repo)
      `test/test_scenario_esg_group_user_api` contains a test that has a similar request as above to test out:

      ```sh
      # Clone the remote repository
      git clone https://github.com/pauldg/total-perspective-vortex.git
      # Change into the cloned repository directory
      cd total-perspective-vortex
      # Checkout the desired remote branch
      git checkout -b location_test origin/location_test
      # Create a venv for testing
      python -m venv .venv
      source .venv/bin/activate
      pip install -r test_requirements.txt
      # Run pytest for the api
      pytest -rPv  tests/test_scenarios_locations.py::TestScenarios::test_scenario_esg_group_user_api
      ```

