---
id: 1
title: Create MedTrack Constitution
stage: constitution
date: 2025-12-29
surface: agent
model: Claude Sonnet 4.5
feature: none
branch: master
user: Claude Code
command: /sp.constitution
labels: [constitution, medtrack, healthcare, todo]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - .specify/memory/constitution.md
tests:
 -
---

## Prompt

```text
You are an autonomous software architect and agentic development system.

Project Name:
MedTrack Todo Agent (Patient-Centric Medication & Care Todo System)

Project Theme:
The Evolution of Todo — From CLI to Distributed Cloud-Native AI Systems

Project Goal:
Design and evolve a patient-focused todo application that helps patients manage medication adherence and health-related tasks. The system must be built progressively using an agentic, spec-driven development workflow without writing boilerplate code manually. The human acts as a Product Architect; you act as the implementing AI system.

Core Philosophy:
- Start simple, evolve complexity gradually
- Prioritize patient safety, clarity, and ease of use
- Follow clean architecture and clean code principles
- Every feature must be justified from a real-world healthcare perspective
- AI assists decision-making, not replaces humans

Development Rules (STRICT):
1. Follow Agentic Dev Stack workflow only:
   - Write specification
   - Generate implementation plan
   - Break plan into tasks
   - Implement tasks via Claude Code
2. No manual coding by the human
3. All behavior must originate from written specifications
4. Maintain clear separation of concerns
5. Keep Phase I fully in-memory (no database, no persistence)
6. Design with future cloud-native, distributed, and AI evolution in mind

Phase I Scope (Current Phase):
Build an in-memory Python console (CLI) Todo application for patients.

Definition of a Task:
In this system, a "task" represents a patient health action, primarily:
- Taking a medicine dose
- Completing a health-related activity

Each task must minimally contain:
- Unique ID
- Title (e.g., medicine name or health task)
- Description (dose, timing, or notes)
- Completion status (pending / completed)

Mandatory Features (Phase I):
- Add Task
- View Task List
- Update Task
- Delete Task
- Mark Task as Complete / Incomplete

CLI Usability Requirements:
- Menu-driven interface (numeric choices only)
- Clear, patient-friendly language (no technical terms)
- View/List option must clearly show all tasks with status indicators
- On application exit:
  - Display a "Thank you" message
  - Display one randomly selected motivational health quote to encourage adherence

Non-Functional Requirements:
- Python 3.13+
- Use UV for environment management
- Follow clean project structure:
  /src for source code
  /specs-history for all specs
- Code must be readable, modular, and maintainable
- No external services or databases in Phase I

Future Evolution (Do Not Implement Yet):
- Priorities and categories (Intermediate)
- Search, filter, and sorting (Intermediate)
- Recurring tasks and reminders (Advanced)
- Event-driven architecture
- Cloud-native deployment
- AI-powered task prioritization and adherence insights

Deliverables Expectations:
- A working console application
- Clear specification history
- Architecture that can naturally evolve into a distributed AI system

Your Responsibility as the AI:
- Ask for clarification only when absolutely necessary
- Generate precise, unambiguous specifications
- Ensure every design decision supports long-term evolution
- Optimize for clarity, safety, and extensibility
```

## Response snapshot

Updated the project constitution file with the MedTrack Todo Agent specific information, including core principles focused on patient-centric design, agentic spec-driven development, clean architecture, progressive evolution, in-memory first approach, and healthcare usability standards. The constitution establishes governance for the project with version 1.0.0, ratified on 2025-12-29.

## Outcome

- ✅ Impact: Created project constitution file with all required principles and governance structure
- 🧪 Tests: No tests required for constitution creation
- 📁 Files: Updated .specify/memory/constitution.md with project-specific principles
- 🔁 Next prompts: Next step would be to create the feature specification based on this constitution
- 🧠 Reflection: The constitution properly captures the healthcare-focused requirements and sets up the proper development workflow for the agentic system

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Create feature specification document