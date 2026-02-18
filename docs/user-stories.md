# User Stories — TaskFlow System

## Epic 1: User Account Management

### US-1 Registration
As a new user,  
I want to create an account,  
so that I can manage my tasks.

**Acceptance Criteria:**
- user can register with email and password
- email must be unique
- password must meet security requirements
- user receives confirmation message

---

### US-2 Login
As a registered user,  
I want to log into the system,  
so that I can access my tasks.

**Acceptance Criteria:**
- user can log in with valid credentials
- error message shown for invalid credentials
- user is redirected to dashboard after login

---

## Epic 2: Task Management

### US-3 Create Task
As a user,  
I want to create a task,  
so that I can track my work.

**Acceptance Criteria:**
- user can enter task title
- user can add description
- user can set deadline
- task appears in task list

---

### US-4 Edit Task
As a user,  
I want to edit tasks,  
so that I can update information.

**Acceptance Criteria:**
- user can modify title and description
- changes are saved successfully
- updated task is displayed immediately

---

### US-5 Delete Task
As a user,  
I want to delete tasks,  
so that I can remove unnecessary items.

**Acceptance Criteria:**
- user can delete task
- confirmation is requested
- task is removed from the list

---

## Epic 3: Task Tracking

### US-6 Change Status
As a user,  
I want to change task status,  
so that I can track progress.

**Acceptance Criteria:**
- user can switch between statuses
- updated status is visible instantly
- system saves status automatically

---

## Epic 4: Collaboration

### US-7 Comment on Task
As a user,  
I want to comment on tasks,  
so that I can communicate with team members.

**Acceptance Criteria:**
- user can add comment
- comments display author and timestamp
- comments appear in chronological order