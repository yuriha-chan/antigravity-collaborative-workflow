---
description: Test-Driven Development (TDD) execution sub-prompt
---

# TDD Partner Workflow

This workflow is dynamically invoked by the meta-orchestrator when the Absorptive Partner identifies that *Test-Driven Development (TDD)*, rigorous reliability, or complex algorithmic correctness is the highest priority for the current project phase.

## Phase Progression

### Phase 1: Setup

1. Set up phases and RED-GREEN-REFACTOR tasks in the Task ledger.
2. Ensure there is a directory for test codes, and testing framework is available.

### Phase 2: Red-Green-Refactor Loop 

- **RED**:
  1. Identify the API-level functions intended to be accessed by other modules.
  2. Write a test for the identified API-level functions based on the agreed-upon Implementation Plan.
  3. The test MUST be a functional test. It should not test any internal structures.
  4. You MUST edit existing test rather than creating new one if the objective is to change the current behavior.
  5. When you mock the dependencies, you should mock high-level APIs, that don't relies on implementational details.
  6. When you mock the dependencies, you should test for mock calls.
  7. Write multiple tests for one function to test differing inputs.
  8. You MUST consider edge cases and write tests for boundary conditions, not just the "happy path".
  9. You MUST write tests that expects exceptions where there will be an error for some input.
  10. You MUST run the test and explicitly observe the failure output (`stdout`/`stderr`).
  11. You MUST first create skelton modules when the test does not run because of new modules are not existent.
  12. Do NOT proceed until a verifiable test failure is produced.
- **GREEN**:
  1. Write the minimum implementation code, or make the minimum code modification required to make the test pass.
  2. Do not add speculative features.
  3. You MUST run the test and observe the test succeeds.
  4. If not, edit the source again and retry the test.
  5. If the error persists and you struggle, you MUST give up early and report to the user and ask for resolution ideas.
- **REFACTOR**:
  1. Review the code edit and consider structural refactoring relating to the edit. Refactoring choices include (but are not limited to) changes in data types, modifying the class properties, introduction of new enum types, new variables to track intermediate states.
  2. Actively detect any parallel abstractions, duplicated responsibilities, or incompatible data models. Refactor regorously to avoid them.
  3. If there are multiple design choices to consider, you MUST stop editing and ask for the user's opinion.
  4. The inquiry to the user can be skipped ONLY IF the decision is obvious based on the past choices explicitly made by the user.
  5. If you decide not to refactor, you must devise rationale for non-editing e.g. the changes are naturally fitting within the existing framework or flow of procedure.
  6. You MUST run the test again to ensure the test is still passing. 

### Phase 3: Test integration, regression check & report 

1. If you have created new test scripts, consider integrating them into existing test scripts if it is structuraly natural.
2. Run the full test for checking regression.
3. Create Walkthrough focusing on the tests you created and your refactoring decisions. Always include complete reports on all modified or deleted tests if any.

## Operational Constraints

1. **Test-First Mandate**: You must NEVER write implementation code before writing the corresponding test file.
2. **Execution Pacing**: Do not attempt to implement more than one feature or unit of work at a time.
