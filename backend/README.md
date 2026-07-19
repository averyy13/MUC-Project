# Emergency Medical Assistant

## Description

Backend API for the **Emergency Medical Assistant** university project. This service will support emergency medical workflows such as user management, incident handling, and push notifications. The codebase follows a layered FastAPI architecture to keep concerns separated and maintainable.

## Folder Structure

```
backend/
│
├── alembic/
│   └── versions/          # Database migration scripts
│
├── app/
│   ├── api/
│   │   └── v1/
│   │       └── routers/   # Versioned API route modules
│   │
│   ├── core/              # Config, security, constants, dependencies
│   ├── db/                # Database session and base setup
│   ├── models/            # SQLAlchemy ORM models
│   ├── schemas/           # Pydantic request/response schemas
│   ├── repositories/      # Data access layer
│   ├── services/          # Business logic
│   ├── firebase/          # Firebase Cloud Messaging integration
│   ├── middleware/        # Custom middleware
│   ├── exceptions/        # Custom exceptions and handlers
│   ├── utils/             # Shared utilities
│   │
│   └── main.py            # Application entry point
│
├── tests/                 # Test suite
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```



## Setup



### Prerequisites

- Python 3.12+
- Docker and Docker Compose (recommended for local development)
- PostgreSQL (if running without Docker)



### Local Setup with Docker

1. Clone the repository and navigate to the `backend/` directory.
2. Copy the environment template and adjust values as needed:
  ```bash
   cp .env.example .env
  ```
3. Build and start the services:
  ```bash
   docker compose up --build
  ```
4. The API will be available at `http://localhost:8000`.



### Local Setup without Docker

1. Create and activate a virtual environment.
2. Install dependencies:
  ```bash
   pip install -r requirements.txt
  ```
3. Copy `.env.example` to `.env` and configure your local PostgreSQL connection.
4. Start the development server:
  ```bash
   uvicorn app.main:app --reload
  ```



### Database Migrations

Alembic is included for schema migrations. Migration commands will be configured once models are implemented.



