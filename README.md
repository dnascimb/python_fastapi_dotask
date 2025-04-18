# Python FastAPI DoTask

This is a project to demonstrate, incrementally, how to build a scaleable "processor" that processes tasks. This is a common need in computer systems and we're using contemporary tools in 2025 to demonstrate how to provide a solution in various ways.

## Outline

- (current) initial version

## Architecture

A basic FastAPI microservice that does the following on startup:

1. Logs that the service has started.
2. Generates a random number.
3. Persists it to a PostgreSQL database.
4. Stores it in a Redis cache with a TTL of 1 minute.

```bash
fastapi-microservice/
├── app/
│   ├── main.py
│   ├── db.py
│   └── cache.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── .env
```

**Pros**:
 - keeps things simple, yet modular and expandable

**Cons**:
 - doesn't use best practices

## Run

Provide a .env file and run docker-compse

```bash
docker-compose up --build
```

## Test

```bash
curl -X POST http://localhost:8000/tasks

{"status":"success","value":268}%                                      
```

...and in the app logs
```bash
python_fastapi_dotask-app-1    | INFO:     Task triggered
python_fastapi_dotask-app-1    | INFO:     Generated random number: 268
python_fastapi_dotask-app-1    | INFO:     Saved to Postgres
python_fastapi_dotask-app-1    | INFO:     Saved to Redis with TTL 60s
python_fastapi_dotask-app-1    | INFO:     172.22.0.1:49160 - "POST /tasks HTTP/1.1" 200 OK
```