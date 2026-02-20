# Library Management GraphQL API

A simple Library Management System built with **Django** and **Graphene-Django** (GraphQL).

## Features
- Manage **Authors** (Create, Update, Delete, List)
- Manage **Books** (Create, List, Retrieve by ID)
- GraphQL API endpoint with GraphiQL interface
- CSRF exempt for easy API testing

## Prerequisites
- Python 3.x
- Django
- Graphene-Django

## Setup

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd Library
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install django graphene-django
    ```

4.  **Run migrations:**
    ```bash
    python manage.py migrate
    ```

5.  **Start the development server:**
    ```bash
    python manage.py runserver
    ```

## API Usage

The API is accessible at: `http://localhost:8000/graphql/`

### GraphiQL Interface
You can interact with the API directly in your browser at the URL above. It provides a visual interface for constructing queries and reading documentation.

### Postman
You can import the `library_graphql_postman_collection.json` file into Postman to get a set of pre-configured requests.

### Example Query (List Books)
```graphql
query {
  allBooks {
    id
    title
    author {
      name
    }
  }
}
```

### Example Mutation (Create Author)
```graphql
mutation {
  createAuthor(name: "New Author", email: "author@example.com") {
    author {
      id
      name
    }
  }
}
```
