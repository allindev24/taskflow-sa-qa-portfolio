# TaskFlow — System Analysis + QA Automation (Python)

Portfolio project demonstrating end-to-end engineering approach:
from **system analysis artifacts** to **automated API/UI tests** and **CI pipeline**.

---

## Highlights

- **System Analysis**: Vision, Functional/Non-Functional requirements, User Stories + Acceptance Criteria
- **Data Modeling**: DB schema + ER diagram
- **QA Automation (Python)**:
  - API tests: `pytest` + `requests`
  - UI test: `pytest-playwright` (Playwright)
  - pytest fixtures + session usage
- **CI**: GitHub Actions runs tests on every push / pull request

---

## Repository Structure

- `docs/` — analysis documents (vision, requirements, user stories, DB schema)
- `diagrams/` — ER diagram and other diagrams
- `automation-tests/`
  - `api-tests/` — API automated tests
  - `ui-tests/` — UI automated tests (Playwright)
  - `requirements.txt` — python dependencies
- `.github/workflows/` — CI pipeline

---

## How to Run Locally

### 1) Create and activate venv (Windows)
```bash
py -m venv venv
venv\Scripts\activate