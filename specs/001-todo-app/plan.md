# Implementation Plan: Todo App Full-Stack Implementation

**Branch**: `001-todo-app` | **Date**: 2026-01-08 | **Spec**: ../spec.md
**Input**: Feature specification from `/specs/001-todo-app/spec.md`

**Note**: This template is filled in by the `/sp.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

Implementation of a full-stack todo application featuring user authentication via Better Auth, REST API backend with Python, Neon PostgreSQL persistence, and a responsive Next.js frontend. The application enforces user data isolation, allowing users to create, manage, and track completion of their personal todos.

## Technical Context

**Language/Version**: Python 3.11 (Backend), TypeScript 5.x (Frontend)
**Primary Dependencies**: FastAPI (Backend), Next.js 14+ (Frontend), Better Auth, SQLModel, Neon PostgreSQL driver
**Storage**: Neon Serverless PostgreSQL database
**Testing**: pytest (Backend), Jest/React Testing Library (Frontend)
**Target Platform**: Web application (Responsive - Desktop/Mobile browsers)
**Project Type**: Web application (Full-stack with separate frontend and backend)
**Performance Goals**: <2 second API response times, <100 concurrent users initially
**Constraints**: No AI/agents, no background workers, JSON REST API, secure user isolation
**Scale/Scope**: Individual user todos, multi-tenant data isolation, responsive UI

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- **Phase Compliance**: ✅ Uses Phase II technologies as specified in constitution
- **Backend**: ✅ Python REST API allowed in Phase II
- **Database**: ✅ Neon Serverless PostgreSQL allowed in Phase II
- **ORM/Data Layer**: ✅ SQLModel allowed in Phase II
- **Frontend**: ✅ Next.js (React, TypeScript) allowed in Phase II
- **Authentication**: ✅ Better Auth allowed in Phase II
- **Architecture**: ✅ Full-stack web application aligns with Phase II
- **Constraints**: ✅ No AI or agents used (complies with Phase II rules)

## Project Structure

### Documentation (this feature)

```text
specs/001-todo-app/
├── plan.md              # This file (/sp.plan command output)
├── research.md          # Phase 0 output (/sp.plan command)
├── data-model.md        # Phase 1 output (/sp.plan command)
├── quickstart.md        # Phase 1 output (/sp.plan command)
├── contracts/           # Phase 1 output (/sp.plan command)
└── tasks.md             # Phase 2 output (/sp.tasks command - NOT created by /sp.plan)
```

### Source Code (repository root)

```text
backend/
├── src/
│   ├── models/
│   │   ├── user.py
│   │   └── todo.py
│   ├── services/
│   │   ├── auth_service.py
│   │   ├── user_service.py
│   │   └── todo_service.py
│   ├── api/
│   │   ├── routes/
│   │   │   ├── auth.py
│   │   │   ├── users.py
│   │   │   └── todos.py
│   │   └── main.py
│   ├── database/
│   │   └── connection.py
│   └── utils/
│       ├── validators.py
│       └── exceptions.py
└── tests/
    ├── unit/
    ├── integration/
    └── contract/

frontend/
├── src/
│   ├── components/
│   │   ├── auth/
│   │   │   ├── SignupForm.tsx
│   │   │   └── SigninForm.tsx
│   │   ├── todos/
│   │   │   ├── TodoItem.tsx
│   │   │   ├── TodoList.tsx
│   │   │   └── TodoForm.tsx
│   │   └── layout/
│   │       ├── Header.tsx
│   │       └── Layout.tsx
│   ├── pages/
│   │   ├── signup.tsx
│   │   ├── signin.tsx
│   │   ├── dashboard.tsx
│   │   └── index.tsx
│   ├── services/
│   │   ├── api.ts
│   │   └── auth.ts
│   ├── hooks/
│   │   └── useAuth.ts
│   └── types/
│       └── index.ts
├── public/
├── styles/
└── tests/
    ├── unit/
    └── integration/
```

**Structure Decision**: Selected Option 2: Web application structure with separate backend and frontend directories to clearly separate concerns. Backend handles API and data persistence while frontend manages UI and user interactions.

## Phase 0: Research & Unknown Resolution

### Backend Framework Research
- **Decision**: Use FastAPI for Python REST API
- **Rationale**: FastAPI provides automatic API documentation, Pydantic validation, async support, and excellent performance for REST APIs
- **Alternatives considered**: Flask (more verbose), Django (overkill for simple API), Starlette (too low-level)

### Authentication Integration Research
- **Decision**: Integrate Better Auth for user management
- **Rationale**: Better Auth is specifically designed for Next.js applications and provides secure, easy-to-implement authentication
- **Alternatives considered**: Auth0 (external dependency), custom JWT implementation (security complexity)

### Database Connection Research
- **Decision**: Use SQLModel as ORM with Neon PostgreSQL
- **Rationale**: SQLModel provides type hints, validation, and combines SQLAlchemy and Pydantic features
- **Alternatives considered**: Pure SQLAlchemy (less type safety), Tortoise ORM (async-only), Peewee (less modern)

### API Communication Strategy Research
- **Decision**: REST API with JSON for frontend-backend communication
- **Rationale**: Simple, well-understood pattern that fits the requirements without over-engineering
- **Alternatives considered**: GraphQL (complexity overhead), gRPC (not suitable for web frontend)

## Phase 1: Data Model & API Contracts

### Data Models
- **User Model**: Contains id, email, password hash (managed by Better Auth), created_at timestamp
- **Todo Model**: Contains id, title, description, completed status, user_id (foreign key), created_at, updated_at timestamps
- **Relationship**: One-to-many (one user to many todos), with foreign key constraint and cascade delete

### API Endpoints
- **POST /api/auth/signup** - User registration
- **POST /api/auth/signin** - User authentication
- **GET /api/todos** - Retrieve user's todos
- **POST /api/todos** - Create new todo
- **PUT /api/todos/{id}** - Update todo
- **DELETE /api/todos/{id}** - Delete todo
- **PATCH /api/todos/{id}/toggle** - Toggle completion status

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| Separate backend/frontend | Clear separation of concerns | Monolithic approach would mix UI and API logic |
| SQLModel ORM | Type safety and validation | Direct SQL queries would lack type checking and validation |
