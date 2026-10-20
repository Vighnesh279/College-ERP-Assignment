# Assignment 2 — Question 1: CI/CD Pipeline and Docker Deployment

## 1. Objective

Implement a CI/CD pipeline that automates application testing, Docker image building, deployment using Docker Compose, and application health verification.

## 2. Technologies Used

- Python 3.12
- Flask
- Pytest
- Docker
- Docker Compose
- GitHub Actions

## 3. Application Overview

The College ERP demonstration application provides a homepage and a health-check endpoint.

- Homepage: http://localhost:5000/
- Health endpoint: http://localhost:5000/health

The health endpoint returns a JSON response confirming that the application is running.

## 4. Project Structure

```text
Q1-CI-CD-Docker/
├── app.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .dockerignore
├── README.md
├── tests/
│   └── test_app.py
└── Screenshots/
    ├── 02-ubuntu-setup.png
    ├── 03-docker-verified.png
    ├── 04-automated-tests-passed.png
    └── 05-docker-compose-app.png
```

## 5. Implementation

### 5.1 Application Development

A Flask application was developed with a College ERP dashboard and a health-check endpoint.

### 5.2 Automated Testing

Two automated tests were created using Pytest.

The tests verify:

- The homepage returns HTTP 200 and contains the expected College ERP content.
- The health endpoint returns HTTP 200 with the expected JSON response.

Run the tests from the repository root:

```cmd
docker compose -f Assignment-2\Q1-CI-CD-Docker\docker-compose.yml run --build --rm web python -m pytest -q
```

**Observed result:** 2 tests passed.

### 5.3 Docker Image Build

The Dockerfile uses Python 3.12 slim, installs the dependencies, copies the application files into the image, and starts the Flask server on port 5000.

### 5.4 Docker Compose Deployment

Start the application:

```cmd
docker compose -f Assignment-2\Q1-CI-CD-Docker\docker-compose.yml up --build -d
```

Check the container status:

```cmd
docker compose -f Assignment-2\Q1-CI-CD-Docker\docker-compose.yml ps
```

Verify the health endpoint:

```cmd
curl http://localhost:5000/health
```

Open the application in a browser:

http://localhost:5000/

Stop the application after verification:

```cmd
docker compose -f Assignment-2\Q1-CI-CD-Docker\docker-compose.yml down
```

### 5.5 GitHub Actions CI/CD

The workflow is located at:

`.github/workflows/assignment2-q1-ci-cd.yml`

The pipeline performs these stages:

1. Checks out the repository.
2. Sets up Python and installs dependencies.
3. Runs automated tests.
4. Builds the Docker image.
5. Deploys the application using Docker Compose.
6. Verifies the health endpoint and container status.
7. Stops the temporary deployment.

The workflow is configured to run on pushes and pull requests to the main branch when relevant Question 1 files change.

## 6. Screenshot Evidence

The `Screenshots/` folder contains evidence of:

- Ubuntu and WSL setup.
- Docker and Docker Compose verification.
- Successful automated tests.
- The College ERP application running in the browser through Docker Compose.

## 7. Results

Local execution confirmed that:

- The Docker image built successfully.
- Both automated tests passed.
- Docker Compose started the application container.
- The container reached a healthy state.
- The health endpoint returned the expected JSON response.
- The local application was stopped successfully after verification.

The GitHub Actions workflow completed successfully. Execution evidence is provided in the Screenshots folder. Verify the workflow run and job logs when presenting the assignment.

## 8. Conclusion

This practical demonstrates automated testing, Docker containerization, Docker Compose deployment, health verification, and CI/CD automation using GitHub Actions for the College ERP demonstration application.