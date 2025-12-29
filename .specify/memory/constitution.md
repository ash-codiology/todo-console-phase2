<!-- SYNC IMPACT REPORT:
Version change: N/A (initial creation) → 1.0.0
Modified principles: N/A
Added sections: All principles and sections as specified for MedTrack Todo Agent
Removed sections: N/A
Templates requiring updates:
  - .specify/templates/plan-template.md ✅ updated
  - .specify/templates/spec-template.md ✅ updated
  - .specify/templates/tasks-template.md ✅ updated
  - .specify/templates/commands/*.md ⚠ pending
  - README.md ⚠ pending
Follow-up TODOs: None
-->
# MedTrack Todo Agent Constitution

## Core Principles

### Patient-Centric Design
Every feature and interaction must prioritize patient safety, clarity, and ease of use. All functionality must be justified from a real-world healthcare perspective, ensuring the system serves patient needs above technical sophistication.

### Agentic Spec-Driven Development
Follow the Agentic Dev Stack workflow: Write specification → Generate implementation plan → Break plan into tasks → Implement tasks via Claude Code. No manual coding by humans; all behavior must originate from written specifications.

### Clean Architecture & Separation of Concerns
Maintain clear separation of concerns following clean architecture principles. Design with future cloud-native, distributed, and AI evolution in mind while keeping Phase I fully in-memory with no persistence.

### Progressive Evolution
Start simple and evolve complexity gradually. Every design decision must support long-term evolution from CLI to distributed cloud-native AI systems. Optimize for clarity, safety, and extensibility.

### In-Memory First (Phase I)
Keep Phase I fully in-memory with no database or persistence. Use Python 3.13+ with UV for environment management. Follow clean project structure with /src for source code and /specs-history for all specifications.

### Healthcare Usability Standards
Implement menu-driven interface with numeric choices only. Use clear, patient-friendly language avoiding technical terms. Ensure View/List option clearly shows all tasks with status indicators. Include motivational elements to encourage adherence.

## Non-Functional Requirements

Technology Stack: Python 3.13+, UV for environment management
Project Structure: /src for source code, /specs-history for specifications
Code Quality: Readable, modular, maintainable code following clean principles
Phase I Constraints: No external services or databases, in-memory only

## Development Workflow

### Implementation Process
1. Write detailed specifications before any implementation
2. Generate implementation plans from specifications
3. Break plans into testable tasks
4. Implement tasks via Claude Code without manual boilerplate writing
5. Maintain clear separation between business logic and technical implementation

### Quality Standards
- All features must be justified from healthcare perspective
- Code must be readable and maintainable
- Every design decision supports long-term evolution
- Clear specification history must be maintained
- Architecture must naturally evolve into distributed AI system

### Feature Requirements
Each task must minimally contain: Unique ID, Title, Description, Completion status
Mandatory features: Add Task, View Task List, Update Task, Delete Task, Mark Task as Complete/Incomplete
Definition of a Task: Patient health action (taking medicine dose, completing health-related activity)

## Governance

This constitution supersedes all other development practices for the MedTrack Todo Agent project. All implementation must comply with these principles. Amendments require explicit documentation, approval, and migration planning. All development activities must verify compliance with patient-centric design and agentic spec-driven development workflows.

**Version**: 1.0.0 | **Ratified**: 2025-12-29 | **Last Amended**: 2025-12-29