# Lab 5 V4 - Dockerized Multi-Model AIoT Inference Service

This repository contains a FastAPI-based AIoT inference service that supports both sensor JSON input and image upload inference.

## Project goals

- Run the service locally using Python and Uvicorn.
- Run the service inside Docker.
- Capture screenshots for local and Docker execution.

## Run locally

`powershell
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python scripts/download_vision_model.py
uvicorn app.main:app --reload
`

Open:

- http://127.0.0.1:8000/health
- http://127.0.0.1:8000/docs
- http://127.0.0.1:8000/classify-image-demo

## Build and run with Docker

`powershell
docker build -t lab5-aiot-inference:v4 .
docker run --rm --name lab5-aiot-api -p 8000:8000 \
  -v E:\phuong	riển khai it và iot\lab5_dockerized_multimodel_aiot_inference_service_v4_code\lab5_dockerized_multimodel_aiot_inference_service_v4/outputs:/app/outputs \
  -v E:\phuong	riển khai it và iot\lab5_dockerized_multimodel_aiot_inference_service_v4_code\lab5_dockerized_multimodel_aiot_inference_service_v4/models/vision:/app/models/vision \
  lab5-aiot-inference:v4
`

## Run with Docker Compose

`powershell
docker compose up --build
docker compose down
`

## Local vs Docker comparison

| Criteria | Local | Docker |
|---|---|---|
| Setup | Requires Python, virtualenv, and dependencies | Requires Docker and a single image build |
| Startup | Fast if dependencies are already installed | Slower on first image build |
| Redeploy | Reinstall and restart Uvicorn | Rebuild or restart container |
| Reproducibility | Depends on local Python environment | More reproducible with container image |
| Data access | Files and logs written directly into the project | Use mounted volumes to persist outputs |
| Consistency | May differ across developer machines | More consistent through the image |

## Screenshot order

Save the images into docs/screenshots/ using these names:

1. health-local.png - response from /health when running local.
2. classify-image-demo-local.png - /classify-image-demo page when running local.
3. docker-images.png - Docker Desktop Images view.
4. docker-containers.png - Docker Desktop Containers Running view.
5. docker-logs.png - Docker Desktop Logs view.
6. swagger-docs-container.png - Swagger /docs when running container.
7. classify-image-demo-container.png - /classify-image-demo when running container.
8. outputs-log.png - log files in outputs/.

### Screenshot 1: Health local

![Health local](docs/screenshots/health-local.png)

### Screenshot 2: Classify image demo local

![Classify image demo local](docs/screenshots/classify-image-demo-local.png)

### Screenshot 3: Docker Desktop Images

![Docker Desktop Images](docs/screenshots/docker-images.png)

### Screenshot 4: Docker Desktop Containers Running

![Docker Desktop Containers Running](docs/screenshots/docker-containers.png)

### Screenshot 5: Docker Desktop Logs

![Docker Desktop Logs](docs/screenshots/docker-logs.png)

### Screenshot 6: Swagger docs container

![Swagger docs container](docs/screenshots/swagger-docs-container.png)

### Screenshot 7: Classify image demo container

![Classify image demo container](docs/screenshots/classify-image-demo-container.png)

### Screenshot 8: Logs in outputs

![Output logs](docs/screenshots/outputs-log.png)

## Additional docs

- docs/HUONG_DAN_CHAY_VA_QUAN_SAT.md
- docs/docker_environment_comparison.md
- docs/docker_desktop_gui_beginner.md
- docs/docker_ubuntu_engine_beginner.md
- docs/submission_checklist_v4.md
- docs/model_formats_for_students.md

## Smoke test local

`powershell
python scripts/smoke_test_local.py
`

Expected result:

`	ext
LOCAL_PIPELINE_TEST_PASS
`
