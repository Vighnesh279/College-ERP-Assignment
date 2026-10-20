# Q3 End-to-End DevOps Architecture



## Architecture Diagram



```mermaid

flowchart TD

&#x20;   A[Jira: Backlog and Sprint Planning]

&#x20;   B[Git and GitHub Repository]

&#x20;   C[GitHub Actions CI/CD]

&#x20;   D[Docker Image Build]

&#x20;   E[Automated Pytest Tests]

&#x20;   F{Tests Passed?}

&#x20;   G[Docker Compose Deployment]

&#x20;   H[MLflow Tracking and Model Registry]

&#x20;   I[Flask Iris Prediction API]

&#x20;   J[Prometheus Metrics Collection]

&#x20;   K[Grafana Monitoring Dashboard]

&#x20;   L[Health and Prediction Verification]



&#x20;   A --> B

&#x20;   B --> C

&#x20;   C --> D

&#x20;   D --> E

&#x20;   E --> F

&#x20;   F -- No --> M[Pipeline Failure and Logs]

&#x20;   F -- Yes --> G

&#x20;   G --> H

&#x20;   H --> I

&#x20;   I --> J

&#x20;   J --> K

&#x20;   I --> L

&#x20;   L --> C

```



## Component Responsibilities



| Component | Responsibility |

|---|---|

| Jira | Manage user stories, tasks, priorities, and sprint progress |

| Git and GitHub | Maintain source code, workflow files, and commit history |

| GitHub Actions | Automate build, test, deployment, and verification stages |

| Docker and Docker Compose | Build application images and orchestrate services |

| MLflow | Track experiments and manage the registered Iris model |

| Flask API | Accept prediction requests and expose application metrics |

| Prometheus | Scrape and store API monitoring metrics |

| Grafana | Visualize prediction requests, errors, and latency |

| Verification stage | Check service health, prediction responses, and monitoring availability |



## Execution Flow



1. Project work is organized in Jira using a Scrum backlog and sprint.

2. Source code and configuration changes are committed and pushed to GitHub.

3. GitHub Actions validates the Compose configuration, builds images, and runs automated tests.

4. Following successful tests, the workflow starts the Docker Compose application stack.

5. The workflow verifies MLflow, the prediction API, a sample prediction, Prometheus metrics, the Prometheus target, and Grafana health.

6. The resulting workflow status and logs provide a record of the execution.



The diagram represents the intended workflow. Actual execution outcomes should be supported by the successful GitHub Actions run and the project's test results.
