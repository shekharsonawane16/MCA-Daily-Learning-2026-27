# Homework Notes: Client–Server Architecture and APIs

**FY MCA | Division B | Academic Year 2026–27**

## 1. Client–Server Architecture
Client–Server Architecture is a model in which a client sends a request to a server, and the server processes it and returns a response.

- **Client:** An application or device that requests information, such as a browser or mobile app.
- **Server:** Receives requests, applies application logic, and returns responses.
- **Database:** Stores and retrieves application data.
- **API:** Defines how software components communicate.

### Example: Logging in
1. The client sends login details to the server over a secure connection.
2. The server validates the request and credentials.
3. The server may query the database.
4. The server returns a result.
5. The client displays the response.

The client does not necessarily connect directly to the database; commonly, the server accesses it.

## 2. What Is an API?
API stands for **Application Programming Interface**. It is a defined way for software applications or components to communicate.

Example: A weather application requests information from a weather service API and displays the returned data.

### Common API types and styles
- **REST API:** Uses HTTP methods and resource-oriented URLs; JSON is commonly used.
- **SOAP API:** A messaging protocol with defined rules, commonly using XML.
- **GraphQL API:** Lets clients request specific fields of data.
- **WebSocket API:** Supports two-way communication over a persistent connection, useful for chat and live updates.

APIs may also be classified by access as public, private/internal, or partner APIs.

## 3. HTTP Methods

| Method | Common purpose | Example |
|---|---|---|
| `GET` | Retrieve data | View student details |
| `POST` | Create a resource or submit data for processing | Register a student |
| `PUT` | Replace a resource, or create it at a specified URI when supported | Replace a student's record |
| `PATCH` | Partially update a resource | Change only an email address |
| `DELETE` | Delete a resource | Remove a student record |

### Difference between POST, PUT, and PATCH
- **POST:** Commonly submits data to a collection or operation. Example: `POST /students`.
- **PUT:** Commonly replaces the complete representation of a resource. Example: `PUT /students/101`.
- **PATCH:** Commonly changes selected fields. Example: `PATCH /students/101`.

Example JSON body for a partial update:

```json
{
  "email": "student@example.com"
}
```

Exact behavior depends on the API's documentation; these are common conventions.

## 4. How an API Request Works
1. The client sends a request containing a method, URL, headers, and possibly a body.
2. The server validates and processes it.
3. The server may read or change data in a database.
4. The server returns a status code and possibly response data.

## 5. Common HTTP Status Codes

| Code | Meaning |
|---|---|
| `200 OK` | Request succeeded |
| `201 Created` | A resource was created |
| `204 No Content` | Request succeeded with no response body |
| `400 Bad Request` | The request is invalid |
| `401 Unauthorized` | Authentication is missing or invalid |
| `403 Forbidden` | Access is not allowed |
| `404 Not Found` | Resource was not found |
| `500 Internal Server Error` | The server encountered an unexpected error |

## 6. Other Important API Concepts
- **Endpoint:** A URL where a resource or operation can be accessed, e.g. `/students/101`.
- **Request:** Information sent from client to server.
- **Response:** Information returned by the server.
- **JSON:** A text format commonly used to exchange structured data.
- **Headers:** Metadata such as content type or authorization.
- **Authentication:** Verifies identity.
- **Authorization:** Determines what actions an identity may perform.
- **CRUD:** Create, Read, Update, Delete.

## 7. Student Management System Example
These are illustrative endpoints, not from a real service.

| Operation | Method | Example endpoint |
|---|---|---|
| View all students | GET | `/students` |
| View student 101 | GET | `/students/101` |
| Add a student | POST | `/students` |
| Replace student 101's record | PUT | `/students/101` |
| Update only student 101's email | PATCH | `/students/101` |
| Delete student 101 | DELETE | `/students/101` |

## 8. Quick Revision
- **GET** = Read
- **POST** = Create or submit
- **PUT** = Replace
- **PATCH** = Partially update
- **DELETE** = Remove

The API documentation defines the exact behavior of each endpoint.

## 9. Practice Questions
1. What is client–server architecture?
2. What is an API, and why is it useful?
3. Explain REST, SOAP, GraphQL, and WebSocket APIs.
4. Differentiate GET and POST.
5. Differentiate PUT and PATCH.
6. What is an endpoint?
7. What is JSON?
8. Explain status codes 200, 201, 400, 401, 404, and 500.
9. Explain authentication and authorization.
10. Give an example of CRUD operations in a student management system.


## 10. Practice Questions with Answers

### Q1. What is Client–Server Architecture?

**Answer:** Client–Server Architecture is a model in which a client sends a request to a server, and the server processes the request and returns a response.

**Example:** A web browser requests a webpage from a web server.

### Q2. What is an API, and why is it useful?

**Answer:** API stands for Application Programming Interface. It allows different software applications to communicate with each other.

**Example:** A weather application uses a weather API to fetch current weather information.

### Q3. Explain REST, SOAP, GraphQL, and WebSocket APIs.

**Answer:**

- **REST:** Uses HTTP methods such as GET and POST to access resources.
- **SOAP:** A messaging protocol that commonly uses XML.
- **GraphQL:** Allows clients to request specific fields of data.
- **WebSocket:** Supports two-way communication over a persistent connection, such as in chat applications.

### Q4. Differentiate between GET and POST.

**Answer:**

| GET | POST |
|---|---|
| Used mainly to retrieve data. | Used to submit data or create resources. |
| Parameters may be included in the URL. | Data is commonly sent in the request body. |
| Example: `GET /students` | Example: `POST /students` |

### Q5. Differentiate between PUT and PATCH.

**Answer:**

| PUT | PATCH |
|---|---|
| Commonly replaces the complete resource representation. | Updates selected parts of a resource. |
| Example: Replace a student's complete record. | Example: Update only a student's email. |
| Endpoint: `PUT /students/101` | Endpoint: `PATCH /students/101` |

### Q6. What is an endpoint?

**Answer:** An endpoint is a URL path through which a client accesses a particular resource or operation in an API.

**Example:** `/students/101` can represent the student whose ID is 101.

### Q7. What is JSON?

**Answer:** JSON stands for JavaScript Object Notation. It is a lightweight text format used to exchange structured data between applications.

**Example:**

```json
{
  "id": 101,
  "name": "Rahul",
  "course": "MCA"
}
```

### Q8. Explain HTTP status codes 200, 201, 400, 401, 404, and 500.

**Answer:**

- **200 OK:** The request was successful.
- **201 Created:** A new resource was created successfully.
- **400 Bad Request:** The request contains invalid information.
- **401 Unauthorized:** Authentication is missing or invalid.
- **404 Not Found:** The requested resource was not found.
- **500 Internal Server Error:** The server encountered an unexpected error.

### Q9. Explain Authentication and Authorization.

**Answer:**

- **Authentication:** Verifies who the user is.
- **Authorization:** Determines what the user is allowed to access or do.

**Example:** Logging in with a password is authentication. Checking whether the user can delete a student record is authorization.

### Q10. Give an example of CRUD operations in a Student Management System.

**Answer:** CRUD stands for Create, Read, Update, and Delete.

| Operation | HTTP Method | Example Endpoint |
|---|---|---|
| Create a student | POST | `/students` |
| Read student details | GET | `/students/101` |
| Update student details | PATCH | `/students/101` |
| Delete a student | DELETE | `/students/101` |

**Conclusion:** Client–Server Architecture and APIs enable applications to communicate and exchange data. Understanding HTTP methods, status codes, endpoints, JSON, authentication, and CRUD operations is essential for developing web applications.
