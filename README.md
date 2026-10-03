# Agile and DevOps Assignment – College ERP System

## Application Domain

**College ERP System**

This project implements the Agile, Git/GitHub, and CI/CD practices required for the Agile and DevOps assignment.

---

# Assignment Overview

The assignment is divided into three major parts:

- **Q1 – Agile and Scrum using Jira**
- **Q2 – Source Code Management using Git and GitHub**
- **Q3 – CI/CD using GitHub Actions**

The complete assignment PDF is also included in the root of this repository as `DEV_ASSI_1VIG.pdf`.

---

# Q1 – Agile and Scrum using Jira

## Objective

Apply Agile principles and Scrum techniques to develop and prioritize User Stories with suitable Acceptance Criteria and manage the Product Backlog using Jira.

## Application Domain

The **College ERP System** was selected as the application domain.

## User Stories

Eight User Stories were created and prioritized in Jira:

| Issue | User Story | Priority |
|---|---|---|
| SCRUM-5 | Student Login to College ERP | Highest |
| SCRUM-6 | Student Attendance Tracking | High |
| SCRUM-7 | Student Timetable Access | High |
| SCRUM-8 | Student Examination Results | High |
| SCRUM-9 | Faculty Attendance Management | Medium |
| SCRUM-10 | Faculty Study Material Upload | Medium |
| SCRUM-11 | Student College Notices | Medium |
| SCRUM-12 | Student Profile Management | Low |

Acceptance Criteria were defined for the User Stories in Jira.

## Sprint

A Scrum Sprint was created with the following configuration:

- **Sprint:** College ERP Sprint 1
- **Duration:** 2 weeks
- **Sprint Goal:** Implement the core student features of the College ERP system including secure login, attendance tracking, timetable access, and examination results.

The first four high-priority student features were included in Sprint 1.

The selected stories were moved through the Scrum workflow and completed.

## Agile Practices Implemented

- Product Backlog creation
- User Story creation
- Acceptance Criteria definition
- Story prioritization
- Sprint planning
- Scrum workflow management
- Progress tracking
- Sprint completion

Detailed Q1 documentation and screenshots are available in:

`Q1-Agile-Jira/`

---

# Q2 – Source Code Management using Git and GitHub

## Objective

Implement source-code management practices using Git and GitHub, including repository creation, commit management, branching, merging, and remote repository management.

## Implementation

A Git repository was created for the College ERP project.

The following Git practices were implemented:

- Git repository initialization
- Main branch creation
- Initial commit
- Feature branch creation
- Student Login feature development
- Feature commit
- Branch merging
- GitHub remote repository creation
- Pushing the project to GitHub

## Feature Branch

```text
feature/student-login
```

## Student Login Feature

The Student Login feature was developed using a separate feature branch.

The feature was committed and subsequently merged into the `main` branch.

## GitHub Repository

The project source code and assignment work are maintained in this GitHub repository:

**College-ERP-Assignment**

## Repository Structure

```text
College-ERP-Assignment/
├── README.md
├── DEV_ASSI_1VIG.pdf
├── Q1-Agile-Jira/
│   ├── README.md
│   └── Screenshots/
├── Q2-Git-GitHub/
│   ├── README.md
│   ├── Screenshots/
│   └── college-erp/
│       └── index.html
├── Q3-CI-CD/
│   ├── README.md
│   └── Screenshots/
└── .github/
    └── workflows/
        └── ci-cd.yml
```

Detailed Q2 documentation and screenshots are available in:

`Q2-Git-GitHub/`

---

# Q3 – CI/CD using GitHub Actions

## Objective

Apply CI/CD practices to the College ERP application and Git repository by configuring and implementing an automated pipeline using GitHub Actions to build, test, package, and deploy the application.

## CI/CD Platform

**GitHub Actions**

The workflow file is located at:

```text
.github/workflows/ci-cd.yml
```

## CI/CD Pipeline

The implemented pipeline consists of four stages:

```text
Build
  ↓
Test
  ↓
Package
  ↓
Deploy
```

The stages are connected using job dependencies so that each stage runs after the required previous stage is completed successfully.

## Build Stage

The Build stage:

- Checks out the source code.
- Verifies that the College ERP application file exists.
- Confirms that the application files are available for the next stages.

Application file verified:

```text
Q2-Git-GitHub/college-erp/index.html
```

## Test Stage

The Test stage:

- Checks out the source code.
- Verifies that the application file exists.
- Checks for the HTML structure.
- Verifies the presence of the College ERP content.
- Reports successful completion when the tests pass.

## Package Stage

The Package stage:

- Creates a deployment package.
- Copies the College ERP application into the package.
- Uploads the package as a GitHub Actions artifact.

Artifact name:

```text
college-erp-package
```

## Deploy Stage

The Deploy stage uses **GitHub Pages** to deploy the College ERP web application.

The deployment process:

- Configures GitHub Pages.
- Uploads the College ERP website.
- Deploys the application using GitHub Pages.

## Pipeline Technologies

- GitHub
- GitHub Actions
- Git
- HTML
- GitHub Pages

## Workflow Location

```text
.github/workflows/ci-cd.yml
```

## CI/CD Result

The GitHub Actions pipeline was successfully executed.

The following stages completed successfully:

- Build Application
- Test Application
- Package Application
- Deploy to GitHub Pages

The College ERP application was successfully packaged and deployed through the automated CI/CD workflow.

Detailed Q3 documentation and screenshots are available in:

`Q3-CI-CD/`

---

# Project Structure

```text
College-ERP-Assignment/
│
├── README.md
├── DEV_ASSI_1VIG.pdf
│
├── Q1-Agile-Jira/
│   ├── README.md
│   └── Screenshots/
│
├── Q2-Git-GitHub/
│   ├── README.md
│   ├── Screenshots/
│   └── college-erp/
│       └── index.html
│
├── Q3-CI-CD/
│   ├── README.md
│   └── Screenshots/
│
└── .github/
    └── workflows/
        └── ci-cd.yml
```

---

# Technologies Used

| Area | Technology |
|---|---|
| Agile / Scrum | Jira |
| Version Control | Git |
| Repository Hosting | GitHub |
| CI/CD | GitHub Actions |
| Web Application | HTML |
| Deployment | GitHub Pages |

---

# Final Result

The College ERP project demonstrates the complete Agile and DevOps workflow:

```text
Jira
  ↓
Agile Planning & Sprint
  ↓
Git & GitHub
  ↓
Source Code Management
  ↓
GitHub Actions
  ↓
Build
  ↓
Test
  ↓
Package
  ↓
Deploy
```

The repository contains the assignment documentation, application source code, Jira/Git/CI-CD evidence screenshots, CI/CD workflow, and the original assignment PDF.

---

# Conclusion

The College ERP System was used to demonstrate Agile planning with Jira, source-code management using Git and GitHub, and automated CI/CD using GitHub Actions.

The project covers the required activities for Q1, Q2, and Q3 and maintains the corresponding documentation and evidence within the GitHub repository.
