# Database Schema — TaskFlow

## Entities Overview

The system stores information about users, tasks, comments, and task assignments.

---

## 1. Users

| Field | Type | Description |
|------|------|------------|
| id | UUID | unique user identifier |
| email | varchar | user email |
| password_hash | varchar | encrypted password |
| created_at | timestamp | account creation date |

---

## 2. Tasks

| Field | Type | Description |
|------|------|------------|
| id | UUID | task identifier |
| title | varchar | task title |
| description | text | task details |
| status | varchar | To Do / In Progress / Done |
| priority | varchar | Low / Medium / High |
| deadline | date | due date |
| created_at | timestamp | creation date |
| created_by | UUID | creator user id |

---

## 3. Task_Assignees

| Field | Type | Description |
|------|------|------------|
| id | UUID | assignment id |
| task_id | UUID | related task |
| user_id | UUID | assigned user |

---

## 4. Comments

| Field | Type | Description |
|------|------|------------|
| id | UUID | comment id |
| task_id | UUID | related task |
| user_id | UUID | comment author |
| content | text | comment text |
| created_at | timestamp | comment time |

---

## Relationships

- One user can create many tasks
- One task can have multiple assignees
- One task can have multiple comments
- Comments belong to a single task