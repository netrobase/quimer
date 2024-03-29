# Quimer: Computer Based Test System Rest API Documentation

The Quimer API is a RESTful API that provides endpoints for managing various aspects of a computer-based test system, including authentication, subjects, topics, tests, questions, answers, sessions, and user responses.

## Authentication

### Credentials:
- `username`: The username of the user.
- `password`: The password of the user.

> Test Credentials: `username: admin`, `password: admin_quimer`.

### Endpoint: `/api/auth/`

#### Methods:
- `POST`: Authenticate user credentials and obtain an access token.

### Endpoint: `/api/auth/logout/`

#### Methods:
- `POST`: Logout the authenticated user and invalidate the access token.

### Endpoint: `/api/auth/user/`

#### Methods:
- `GET`: Retrieve details of the authenticated user.

### Endpoint: `/api/auth/password/change/`

#### Methods:
- `POST`: Change the password of the authenticated user.

### Endpoint: `/api/auth/token/verify/`

#### Methods:
- `POST`: Verify the validity of an access token.

### Endpoint: `/api/auth/token/refresh/`

#### Methods:
- `POST`: Refresh an expired access token.

## Subjects

### Endpoint: `/api/subjects/`

#### Methods:
- `GET`: Retrieve all subjects.
- `POST`: Create a new subject.

### Endpoint: `/api/subjects/{id}/`

#### Methods:
- `GET`: Retrieve a specific subject.
- `PUT`: Update a specific subject.
- `DELETE`: Delete a specific subject.

## Topics

### Endpoint: `/api/topics/`

#### Methods:
- `GET`: Retrieve all topics.
- `POST`: Create a new topic.

### Endpoint: `/api/topics/{id}/`

#### Methods:
- `GET`: Retrieve a specific topic.
- `PUT`: Update a specific topic.
- `DELETE`: Delete a specific topic.

## Tests

### Endpoint: `/api/tests/`

#### Methods:
- `GET`: Retrieve all tests.
- `POST`: Create a new test.

### Endpoint: `/api/tests/{id}/`

#### Methods:
- `GET`: Retrieve a specific test.
- `PUT`: Update a specific test.
- `DELETE`: Delete a specific test.

## Questions

### Endpoint: `/api/questions/`

#### Methods:
- `GET`: Retrieve all questions.
- `POST`: Create a new question.

### Endpoint: `/api/questions/{id}/`

#### Methods:
- `GET`: Retrieve a specific question.
- `PUT`: Update a specific question.
- `DELETE`: Delete a specific question.

## Answers

### Endpoint: `/api/answers/`

#### Methods:
- `GET`: Retrieve all answers.
- `POST`: Create a new answer.

### Endpoint: `/api/answers/{id}/`

#### Methods:
- `GET`: Retrieve a specific answer.
- `PUT`: Update a specific answer.
- `DELETE`: Delete a specific answer.

## Sessions

### Endpoint: `/api/sessions/`

#### Methods:
- `GET`: Retrieve all sessions.
- `POST`: Create a new session.

### Endpoint: `/api/sessions/{id}/`

#### Methods:
- `GET`: Retrieve a specific session.
- `PUT`: Update a specific session.
- `DELETE`: Delete a specific session.

## User Responses

### Endpoint: `/api/user-responses/`

#### Methods:
- `GET`: Retrieve all user responses.
- `POST`: Create a new user response.

### Endpoint: `/api/user-responses/{id}/`

#### Methods:
- `GET`: Retrieve a specific user response.
- `PUT`: Update a specific user response.
- `DELETE`: Delete a specific user response.

> Pagination are supported for all endpoints that return a list of items. The default page size is 10 items per page.
