# Functional & Non-Functional Requirements — TaskFlow

## 1. Functional Requirements

### 1.1 User Management

FR-1: Users must be able to register using email and password.

FR-2: Users must be able to log in and log out.

FR-3: Users must be able to reset their password.

---

### 1.2 Task Management

FR-4: Users must be able to create tasks.

FR-5: Users must be able to edit tasks.

FR-6: Users must be able to delete tasks.

FR-7: Users must be able to assign tasks to other users.

FR-8: Users must be able to set task priority.

FR-9: Users must be able to set deadlines.

---

### 1.3 Task Status Tracking

FR-10: Users must be able to change task status:
- To Do
- In Progress
- Done

FR-11: The system must display task status in real time.

---

### 1.4 Collaboration

FR-12: Users must be able to comment on tasks.

FR-13: Users must be able to view task history.

---

### 1.5 Search & Filtering

FR-14: Users must be able to search tasks by title.

FR-15: Users must be able to filter tasks by:
- status
- priority
- assigned user
- deadline

---

## 2. Non-Functional Requirements

### 2.1 Performance

NFR-1: The system should load dashboard data within 2 seconds.

NFR-2: Task updates should be reflected within 1 second.

---

### 2.2 Security

NFR-3: User passwords must be stored in encrypted form.

NFR-4: Only authorized users can access tasks.

---

### 2.3 Usability

NFR-5: The interface should be intuitive for first-time users.

NFR-6: Users should be able to create a task within 3 clicks.

---

### 2.4 Reliability

NFR-7: The system uptime should be at least 99%.

---

### 2.5 Compatibility

NFR-8: The system must support modern web browsers (Chrome, Edge, Firefox).