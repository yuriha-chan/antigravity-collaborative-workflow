---
description: Gradual Restructuring & Anti-Corruption Layer sub-prompt
---

# Gradual Restructuring Partner Workflow

This workflow is dynamically invoked by the meta-orchestrator when the project involves deep legacy codebase integration, extreme technical debt, or highly ambiguous external dependencies where a complete redesign is impossible or unsafe.

## Operational Constraints

1. **Defensive Architecture**: Do not attempt to perfectly model or rewrite the ambiguous/legacy system. Instead, prioritize building defensive boundaries (Anti-Corruption Layers - ACL) around new development. 
2. **Translation Interfaces**: Ensure that new, clean domain models do not leak into the legacy system, and legacy terms/data structures are translated immediately at the boundary. Create explicit Facades, Adapters, or Translators between the old and the new.
3. **Strangler Fig Application**: Approach restructuring gradually. Identify small, low-risk vertical slices of legacy logic to intercept or replace without disrupting the entire monolith.
4. **Preserve Existing Behavior**: When wrapping legacy logic, the primary goal is to preserve existing behavior behind a clean interface. Do not optimize or "fix" the legacy logic itself unless it is explicitly scoped into the current vertical slice.
