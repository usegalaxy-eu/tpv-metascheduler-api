# tpv-metascheduler-api
Metascheduler for TPV as Service

1. create a venv
2. install requirements
   `pip install -r requirements.txt`
3. Run the API: 
   `uvicorn main:app --reload`
4. Testing the API with input data:
   1. SwaggerUI: http://127.0.0.1:8000/docs
   2. curl
   3. using a python script with the requests or httpx library