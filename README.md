# geoshub


### TODOs
[X] Design database > `Services` and `Actitivties`
[X] Implement database
[X] Choose a design
[X] Make unit test
[X] Make integration test
[X] `Services` RESTFul APIs
[X] How to log different acitivities in database
[X] `Activities` RESTFul APIs
[X] Make function test
[X] Make DB diagram
[X] Make App flow diagram
[X] App configable
[] README
    [] A brief explanation for the code structure
    [] CURL commands to test and verify API endpoints.
[] Hight Available
[] Horizontaly Scale
[] Logging

## App Structure

```
st_fastapi_v2
|    app
|    |    routers
|    |    |    services.py           APIs for services
|    |    |    activities.py         APIs for activities
|    |    database.py        Database connetion
|    |    models.py          Define tables and models
|    |    schemas.py         Define schema for routes inputs
|    |    settings.py        App setting variables. Loading the configuration from a .env file when it is present 
|    tests
|    |    e2e
|    |    |    test_activities_api.py      Testing activity's APIs defined in routers/activities.py
|    |    |    test_services_api.py        Testing service's APIs defined in routers/services.py
|    |    unit
|    |    |    test_activities.py        Test ActivityModel methods defined in models.py
|    |    |    test_services.py          Test ServiceModel methods defined in models.py
|    .env-template           Define key-value pairs as environment variables
|    application.py          Define FastAPI instance and routes
|    README.md               Me
|    requirements.txt        List of required packages
```

## Setup
Prerequirement
1. `python3` installed

### Step 0: Virtual Environment (Optional)
1. Open terminal and navigate to project root folder
2. Create a new env by running `python3 -m venv venv`
3. Activate the env by running `source ./venv/bin/activate`

### Step 1: Install required packages
On your terminal run `pip install -r requirements.txt`

### Step 2: Environment Variable
You can config the app's host, port, and database url by adding a `.env` file under root folder

1. Clone a new `.env` from `.env-template`
2. Adjust `APP_HOST`, `APP_PORT`, `APP_DATABASE_URL` to change app's host, port, and database url respectively


### Step 2: Run the app
On your terminal run `python3 main.py`

Sample output
```
INFO:     Started server process [23361]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```   

## CURL Testing
