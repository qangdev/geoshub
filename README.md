# Geo's Hub

## App Structure
A simple monolithic structure since this is a MVP. It has three main parts.

I. The root project folder contains the configuration files and a file to serve the app.

II. `app` folder is responsible for defining models, handling APIs requests and responses, database connection, business logic.

III. `tests` folder containts unittest and APItests cases.


```
geoshub
|    app
|    |    routers
|    |    |    services.py                  APIs for services
|    |    |    activities.py                APIs for activities
|    |    application.py                    Define FastAPI instance and routes
|    |    database.py                       Database connetion
|    |    models.py                         Define tables and models
|    |    schemas.py                        Define schema for routes inputs
|    |    services.py                       Handle bussiness logic
|    |    settings.py                       App setting variables. Loading the configuration from a .env file when it is present 
|    tests
|    |    e2e
|    |    |    test_activities_api.py       Testing activity's APIs defined in routers/activities.py
|    |    |    test_services_api.py         Testing service's APIs defined in routers/services.py
|    |    unit
|    |    |    test_activities.py           Test ActivityModel methods defined in models.py
|    |    |    test_services.py             Test ServiceModel methods defined in models.py
|    .env-template                          Define key-value pairs as environment variables
|    cmd.py                                 Containts commands such as importing data
|    main.py                                For running the app
|    README.md                              Me
|    requirements.txt                       List of required packages
```

## Diagrams
App components and entity diagram are located under `docs` folder named `components_diagram.png` and `entity_diagram.png` respectively.

## Setup
Prerequirement
1. `python3` installed.

### Step 0: Virtual Environment (Optional)
1. Open terminal and navigate to project root folder.
2. Create a new env by running `python3 -m venv venv`.
3. Activate the env by running `source ./venv/bin/activate`.

### Step 1: Install required packages
On your terminal run `pip install -r requirements.txt`.

### Step 2: Environment Variable
You can config the app's host, port, and database url by adding a `.env` file under root folder.

1. Clone a new `.env` from `.env-template`.
2. The default values are good to go but you can adjust `APP_HOST`, `APP_PORT`, `APP_DATABASE_URL` to change app's host, port, and database url respectively.


### Step 3: Run the app
On your terminal run `python3 main.py`

Sample output
```
INFO:     Started server process [23361]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```   

## CURL Testing
Run `python3 cmd.py` to import sample data beforehand.

Also there are APIs test cases under `tests/e2e` folder.

1. Select all services: `curl -X GET http://127.0.0.1:8000/api/v1/services/`
2. Search services with `os` is `linux`: `curl -X GET http://127.0.0.1:8000/api/v1/services/?os=android`
3. Add a new service: `curl -H "Accept: application/json" -H "Content-type: application/json" -X POST -d '{"name":"sample", "price": 99.9, "os_platform": "linux"}' http://127.0.0.1:8000/api/v1/services/`

