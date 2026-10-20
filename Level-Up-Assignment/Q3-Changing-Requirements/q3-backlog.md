# Q3 — Managing Changing Requirements



## Project

College ERP System



## Scenario

The College ERP team is developing a student portal.

Requirements may change after stakeholder feedback.

The team has limited time and must prioritize features

according to business value, urgency, and available resources.



## 1. Initial Requirements



1. Students must log in using valid credentials.

2. Students must view an academic dashboard.

3. Students must view subject-wise attendance percentages.

4. Students must view their examination results.



At this stage, the dashboard does not have a dedicated

warning for attendance below 75%.



## 2. Initial Product Backlog



| ID | User Story | Business Value | Priority | Estimate |

|---|---|---|---|---|

| REQ-01 | As a student, I want to log in securely so that I can access my academic information. | High | Must | 5 points |

| REQ-02 | As a student, I want to view my academic dashboard so that I can see a summary of my academic details. | High | Must | 3 points |

| REQ-03 | As a student, I want to view subject-wise attendance so that I can monitor my attendance. | High | Must | 5 points |

| REQ-04 | As a student, I want to view examination results so that I can check my academic performance. | Medium | Should | 3 points |



The estimates are illustrative planning estimates for this

academic exercise, not measurements from an actual team.



## 3. Initial Iteration Plan



Iteration duration: 3 working days



Available resources: One simulated developer and one

simulated tester/reviewer.



Planned work:

- Verify the student login workflow.

- Check that the academic dashboard displays sample data.

- Verify the attendance percentage display.

- Record defects and stakeholder feedback.



The team will not claim that a task is complete until it

has been implemented and tested.



## 4. Initial Baseline



The existing backlog covers login, dashboard, attendance,

and examination results. A dedicated low-attendance warning

has not yet been included. The backlog will be updated after

the simulated stakeholder review.





## 5. Simulated Stakeholder Feedback



Review type: Simulated customer review



Stakeholder: College representative (simulated)



Feedback:

"The student portal should clearly warn students when

their attendance in any subject falls below 75%. Students

need to identify attendance risks before examinations."



Change requested:

Add a low-attendance warning to the academic dashboard.



Reason:

Students may overlook low attendance when only a percentage

is displayed. A visible warning makes the information easier

to notice and act upon.



## 6. Updated Product Backlog



| ID | User Story | Business Value | Priority | Estimate | Status |

|---|---|---|---|---|---|

| REQ-01 | As a student, I want to log in using valid credentials so that I can access my academic information. | High | Must | 5 points | Existing |

| REQ-02 | As a student, I want to view my academic dashboard so that I can see my academic summary. | High | Must | 3 points | Existing |

| REQ-03 | As a student, I want to view subject-wise attendance so that I can monitor my attendance. | High | Must | 5 points | Existing |

| REQ-05 | As a student, I want a warning when any subject's attendance falls below 75% so that I can identify attendance risks. | High | Must — newly added | 3 points | To Do |

| REQ-04 | As a student, I want to view examination results so that I can check my academic performance. | Medium | Should | 3 points | Deferred if capacity is insufficient |



The estimates are illustrative planning estimates, not measured

development effort.



## 7. Prioritization After the Change



REQ-05 is prioritized because the warning is directly related

to student attendance risk and was explicitly requested during

the simulated review.



Available resources are limited, so the team will focus first

on login verification, dashboard display, attendance display,

and the new warning. Examination results remain in the backlog

but may be deferred if they do not fit within the iteration.



Prioritization considers:

- Business value: helps students recognize attendance risk.

- Urgency: requested during the current review.

- Resources: the team has limited development and testing capacity.



## 8. Updated Iteration Plan



Iteration duration: 3 working days



Simulated developer:

- Add the low-attendance warning to the dashboard.

- Verify that normal attendance does not show a warning.



Simulated tester/reviewer:

- Test attendance below 75%.

- Test attendance equal to 75%.

- Test attendance above 75%.

- Record results and report defects.



Acceptance criteria for REQ-05:

1. A warning appears when attendance is below 75%.

2. No low-attendance warning appears at exactly 75%.

3. No low-attendance warning appears above 75%.

4. The displayed attendance percentage remains visible.

5. The warning can be understood without relying on color alone.



## 9. Implementation Status and Verification

The attendance-warning requirement was implemented in the browser-based College ERP prototype and tested with sample attendance values.

| Test | Sample attendance | Observed result |
|---|---:|---|
| Q3-T1 | 68% | Warning displayed |
| Q3-T2 | 75% | No low-attendance warning |
| Q3-T3 | 82% | No low-attendance warning |

These results apply to the local browser demonstration using sample data. Stakeholder feedback and team roles were simulated for the assignment. The prototype is not a production ERP system.



