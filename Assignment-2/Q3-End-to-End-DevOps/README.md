# Q3 - End-to-End DevOps Pipeline for an ML Prediction Service



## 1. Project Overview



This project demonstrates an end-to-end DevOps pipeline by integrating Agile planning, Git-based version control, automated Continuous Integration and Continuous Deployment (CI/CD), Docker-based deployment, automated testing, and application monitoring.



The project reuses the Iris machine learning prediction service developed in Q2. The application uses Flask to provide predictions, MLflow to track experiments and manage the registered model, Docker Compose to orchestrate services, Prometheus to collect application metrics, and Grafana to visualize monitoring data.



A dedicated GitHub Actions workflow will integrate these components into a repeatable pipeline that validates the application, executes tests, builds the required containers, deploys the services, and verifies their availability.



## 2. Problem Statement



Develop and demonstrate an integrated DevOps workflow for a machine learning prediction application. The pipeline should connect Agile planning, source code management, automated testing, containerization, deployment, and monitoring into a single development and delivery process.



## 3. Objectives



- Apply Agile planning practices to organize project requirements, user stories, tasks, and acceptance criteria.

- Maintain application code and configuration files using Git and GitHub.

- Implement an automated CI/CD workflow using GitHub Actions.

- Execute automated tests to validate application functionality.

- Build and run application containers using Docker and Docker Compose.

- Integrate MLflow for experiment tracking and model registration.

- Monitor application activity using Prometheus and Grafana.

- Verify deployment and document the complete pipeline with an architecture diagram and execution results.



## 4. Technology Stack



| Technology | Purpose |

|---|---|

| Jira | Agile backlog and task management |

| Git | Source code version control |

| GitHub | Repository hosting and collaboration |

| GitHub Actions | Automated CI/CD pipeline |

| Python | Application and model development |

| Flask | REST API for machine learning predictions |

| Scikit-learn | Iris classification model |

| MLflow | Experiment tracking and model registry |

| Pytest | Automated application testing |

| Docker | Containerization |

| Docker Compose | Multi-service orchestration |

| Prometheus | Application metric collection |

| Grafana | Monitoring dashboards |



## 5. Project Architecture



The following diagram represents the intended end-to-end workflow.



```mermaid

flowchart TD

&#x20;   A[Jira Agile Planning] --> B[Git and GitHub]

&#x20;   B --> C[GitHub Actions Trigger]

&#x20;   C --> D[Build Docker Images]

&#x20;   D --> E[Run Automated Tests]

&#x20;   E --> F{Tests Passed?}

&#x20;   F -- No --> G[Report Pipeline Failure]

&#x20;   F -- Yes --> H[Deploy with Docker Compose]

&#x20;   H --> I[MLflow Tracking and Model Registry]

&#x20;   I --> J[Flask Prediction API]

&#x20;   J --> K[Prometheus Metrics Collection]

&#x20;   K --> L[Grafana Dashboard]

&#x20;   J --> M[Health and Prediction Verification]

&#x20;   M --> N[Pipeline Result]

```



## 6. Agile Planning



Agile practices are used to organize development work into manageable tasks. The team can manage these activities using the existing Jira Scrum project or an appropriate project backlog.



### Proposed Product Backlog



| Backlog Item | Description | Priority |

|---|---|---|

| User Story 1 | Organize project requirements and define acceptance criteria | High |

| User Story 2 | Manage source code through Git and GitHub | High |

| User Story 3 | Automate build and testing using GitHub Actions | High |

| User Story 4 | Deploy the application using Docker Compose | High |

| User Story 5 | Integrate MLflow, Prometheus, and Grafana | High |

| User Story 6 | Document architecture and verify end-to-end execution | Medium |



### Example User Story



**Title:** Automate deployment of the ML prediction service.



**User Story:** As a developer, I want the application to be built, tested, and deployed automatically so that code changes can be validated consistently.



**Acceptance Criteria:**



1. The workflow triggers when relevant project files are pushed to the main branch or submitted through a pull request.

2. The application Docker images build successfully.

3. Automated tests execute and report their results.

4. The deployment services start successfully when the required tests pass.

5. The application health endpoint responds successfully.

6. The monitoring service can collect application metrics.



The backlog items and acceptance criteria are proposed planning artifacts and should be created or updated in Jira as part of the implementation.



## 7. Git and GitHub Integration



The project uses a common GitHub repository:



https://github.com/Vighnesh279/College-ERP-Assignment



The existing Q2 MLflow application is located at:



`Assignment-2/Q2-MLflow-Monitoring/`



The Q3 integration documentation is located at:



`Assignment-2/Q3-End-to-End-DevOps/`



The Q3 CI/CD configuration will be maintained separately under:



`.github/workflows/q3-end-to-end-devops.yml`



Meaningful commits and the main branch are used to maintain a traceable project history. A separate workflow helps prevent unnecessary modifications to the existing Assignment 1 and Q1 pipelines.



## 8. CI/CD Pipeline Design



The Q3 GitHub Actions pipeline is intended to contain the following stages.



### Stage 1: Checkout



Retrieve the latest repository contents from GitHub.



### Stage 2: Build



Build the container images required by the ML prediction application and its supporting services.



### Stage 3: Test



Execute automated tests using Pytest to validate the homepage, health endpoint, input validation, successful prediction behavior, and Prometheus metrics endpoint.



### Stage 4: Deployment



Start the required application services using Docker Compose after successful validation.



### Stage 5: Health Verification



Check that the MLflow service and prediction API are available. Submit a sample prediction request and verify the response.



### Stage 6: Monitoring Verification



Check the Prometheus target and metrics endpoint. Confirm that Grafana is available to visualize the application metrics.



### Stage 7: Pipeline Result



Publish the workflow status in GitHub Actions so that successful and failed executions can be inspected.



The Q3 GitHub Actions workflow completed successfully. Supporting execution screenshots are included in the Screenshots folder. Review the corresponding GitHub Actions run and logs when presenting the assignment.



## 9. Docker-Based Deployment



Docker Compose is used to coordinate the application's services.



The existing Q2 configuration includes:



- **MLflow:** Experiment tracking and model registry.

- **Trainer:** Machine learning model training and registration.

- **API:** Flask prediction service.

- **Prometheus:** Application metrics collection.

- **Grafana:** Monitoring dashboard.



The project will reuse the existing configuration wherever practical instead of duplicating the application implementation.



### Local Deployment Commands



Execute these commands from the repository root.



Start the application stack:



```cmd

docker compose -f Assignment-2\Q2-MLflow-Monitoring\\docker-compose.yml up --build -d

```



Check service status:



```cmd

docker compose -f Assignment-2\Q2-MLflow-Monitoring\\docker-compose.yml ps

```



View application logs:



```cmd

docker compose -f Assignment-2\Q2-MLflow-Monitoring\\docker-compose.yml logs --tail=50

```



Stop the application stack:



```cmd

docker compose -f Assignment-2\Q2-MLflow-Monitoring\\docker-compose.yml down

```



## 10. Application and Monitoring Endpoints



| Component | URL | Purpose |

|---|---|---|

| MLflow | http://localhost:5001 | Experiment tracking and model registry |

| Flask API | http://localhost:5002 | Prediction service |

| Prometheus | http://localhost:9090 | Metrics queries and target status |

| Grafana | http://localhost:3000 | Monitoring dashboard |



The prediction API exposes the following endpoints:



- `GET /` - Application information.

- `GET /health` - Application health status.

- `POST /predict` - Prediction using four numeric Iris features.

- `GET /metrics` - Prometheus metrics.



Example prediction request:



```json

{

&#x20; "features": [5.1, 3.5, 1.4, 0.2]

}

```



The API returns a prediction, the class name, and registered model information when the request succeeds.



## 11. Automated Testing



The existing Q2 application contains five automated tests covering:



1. Homepage response.

2. Health endpoint.

3. Invalid prediction input.

4. Successful prediction.

5. Prometheus metrics endpoint.



Run the tests from the repository root:



```cmd

docker compose -f Assignment-2\Q2-MLflow-Monitoring\\docker-compose.yml run --rm api python -m pytest -v tests/test_app.py

```



**Previously verified local baseline:** 5 tests passed, with 9 non-fatal dependency deprecation warnings.



This baseline result does not by itself confirm that the new Q3 GitHub Actions pipeline has passed. The integrated workflow must be run and verified separately.



## 12. Monitoring and Observability



Prometheus scrapes metrics exposed by the Flask prediction API. The Grafana dashboard visualizes the following measurements:



- **Prediction Requests per Minute:** Shows API request activity.

- **Prediction Errors per Minute:** Shows recorded prediction errors.

- **Average Prediction Latency:** Shows the average time spent processing predictions.



These metrics help demonstrate application observability after deployment. The Prometheus API target should report an `UP` status when the API is reachable.



## 13. Validation and Expected Results



The following checks will be used to assess the completed pipeline.



| Validation Item | Expected Result |

|---|---|

| Repository integration | Q2 application and Q3 configuration are available in GitHub |

| Workflow execution | GitHub Actions completes the required stages |

| Docker build | Required service images build successfully |

| Automated testing | All application tests pass |

| Deployment | Application services start successfully |

| Health verification | The prediction API reports a healthy status |

| Prediction verification | A valid prediction request returns a response |

| Prometheus | The API target is UP and metrics are available |

| Grafana | Monitoring dashboard is accessible and displays metrics |

| Documentation | Architecture and actual execution results are recorded |



Actual CI/CD outcomes are documented through the completed GitHub Actions run and evidence in the Screenshots folder. Refer to ne results.



## 14. Screenshots and Execution Evidence



The `Screenshots/` folder is reserved for relevant execution evidence, including:



1. Jira backlog and sprint planning.

2. GitHub repository and Q3 workflow configuration.

3. GitHub Actions workflow execution and job results.

4. Successful automated testing.

5. Docker Compose service status.

6. Prediction API response.

7. Prometheus target and metrics verification.

8. Grafana monitoring dashboard.

9. Final integrated pipeline result.



Only genuine screenshots or actual command output should be included as execution evidence.



## 15. Conclusion



This project integrates Agile planning, source code management, automated build and testing, containerized deployment, MLflow model lifecycle management, and application monitoring into a single DevOps workflow.



The reuse of the existing Iris prediction application reduces duplicate development work and allows the Q3 assignment to focus on integrating and demonstrating the complete pipeline. Successful execution is supported by the completed GitHub Actions run, application health checks, automated test results, and mand monitoring verification.

## Architecture and Execution Evidence

The end-to-end architecture diagram and component descriptions are documented in [architecture.md](architecture.md).

The Q3 GitHub Actions workflow is defined in .github/workflows/q3-end-to-end-devops.yml.

Jira planning screenshots and workflow execution evidence are stored in the Screenshots/ directory.
