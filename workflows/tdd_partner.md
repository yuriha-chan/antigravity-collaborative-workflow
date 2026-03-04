---
description: Test-Driven Development (TDD) execution sub-prompt
---

# TDD Partner Workflow

This workflow is dynamically invoked by the meta-orchestrator when the Absorptive Partner identifies that *Test-Driven Development (TDD)*, rigorous reliability, or complex algorithmic correctness is the highest priority for the current project phase.

## Operational Constraints

1. **Test-First Mandate**: You must NEVER write implementation code before writing the corresponding test file.
2. **Red-Green-Refactor Loop**: 
   - **RED**: Write a failing test based on the agreed-upon Implementation Plan. You MUST run the test and explicitly observe the failure output (`stdout`/`stderr`). Do NOT proceed until a verifiable test failure is produced.
   - **GREEN**: Write the absolute minimum implementation code required to make the test pass. Do not add speculative features ("YAGNI" - You Aren't Gonna Need It).
   - **REFACTOR**: Once passing, evaluate the code for readability, optimization, and structural cleanliness. Make changes while ensuring tests continue to pass.
3. **Execution Pacing**: Do not attempt to implement more than one feature or unit of work at a time. Present the failing test to the user, or run it yourself and show the output, before proceeding to the implementation.
4. **Boundary Focus**: Actively consider and write tests for edge cases, null states, and boundary conditions, not just the "happy path".
