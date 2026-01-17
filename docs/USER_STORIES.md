# User Stories – Library Management System

## User Story 1: Book Registration
**As a** librarian  
**I want** to register new books in the system  
**So that** books can be tracked and managed easily.

**Acceptance Criteria:**
- Book ID must be unique
- Book status should be set to `Available`
- Registered book should appear in the library records

---

## User Story 2: Borrow Book
**As a** user  
**I want** to borrow a book  
**So that** I can read it.

**Acceptance Criteria:**
- Only available books can be borrowed
- Borrowed book status should change to `Borrowed`
- Borrowing an already borrowed book should fail

---

## User Story 3: Return Book
**As a** user  
**I want** to return a borrowed book  
**So that** it becomes available for others.

**Acceptance Criteria:**
- Returned book status should change to `Available`
- Only borrowed books can be returned

---

## User Story 4: Generate Library Report
**As a** librarian  
**I want** to generate a report of all books  
**So that** I can view the current library status.

**Acceptance Criteria:**
- Report should list all books
- Each book should show its current status
