# tpv-metascheduler-api

Metascheduler for TPV as Service

1. Create a venv

   ```python

   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

2. Run the API locally:

   Set correct values for the environment variables to access InfluxDB in `set_env.sh`:
   ```shell
   source set_env.sh
   uvicorn main:app --reload
   ```

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
               "tags": null,
               "queued_job_count": 10,
               "tool_id": "api_test",
               "job_count_in_time_window": 30,
               "galaxy_db_query_time": "2024-04-18T14:20:00Z",
               "median_queue_time": 1,
               "median_run_time": 8,
               "completed_count": 0,
               "suspended_count": 0,
               "held_count": 4,
               "removed_count": 0,
               "running_count": 0,
               "idle_count": 0,
               "cpu_usage_perc": 0,
               "mem_usage_perc": 0,
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
               "tags": null,
               "queued_job_count": 8,
               "tool_id": "api_test",
               "job_count_in_time_window": 30,
               "galaxy_db_query_time": "2024-04-18T14:20:00Z",
               "median_queue_time": 1,
               "median_run_time": 8,
               "completed_count": 0,
               "suspended_count": 0,
               "held_count": 4,
               "removed_count": 0,
               "running_count": 0,
               "idle_count": 0,
               "cpu_usage_perc": 0,
               "mem_usage_perc": 0,
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
         "dataset_attributes": {
            "dataset_italy": {
               "object_store_id": "object_store_italy_S3_01",
               "size": 12345678
            },
            "dataset_poland": {
               "object_store_id": "object_store_poland",
               "size": 123456789
            }
         }
      }
      ```

   2. curl

      The Swagger UI can give you a curl version of your request after executing

   3. Using a python script with the requests or httpx library

      There is an example of how to do this with TPV:
      [example_tpv_config_locations_api.yml](./example_tpv_config_locations_api.yml).

      This config can be set up with a galaxy instance or by cloning the TPV repo
      (the example currently depends on an [open PR](https://github.com/galaxyproject/total-perspective-vortex/pull/108)):

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
      pip install -r requirements_test.txt
      # Run pytest for the api
      pytest -rPv  tests/test_scenarios_locations.py::TestScenarios::test_scenario_esg_group_user_api
      ```

