---
description: Dialogue-first workflow for abstract requirement elicitation
---

# Dialogue-First Workflow (Absorptive Partner)

Use this workflow when the user presents a vague or abstract idea that requires conceptual and architectural exploration before execution. In this stage, task-oriented behavior is minimized and deep understanding by intellectual dialogue is prioritized.

## Phase 0: Initialization

**Initial Action**: Before engaging in the absorption phase (Phase 1), you MUST explicitly set up the `Task.md` artifact in the brain directory. This file must be initialized with the top-level checkpoints for Phase 1 (Absorption), Phase 2 (Alignment Checkpoint), Phase 3 (Plan Synthesis), and Phase 4 (Post-Plan Critique). To prevent context decay, EVERY phase in your `task.md` MUST explicitly start with the instruction: "Review `.agents/workflows/absorptive_partner.md` and update the Task list". You MUST stick strictly to this `task.md` to track your progression. Skipping any entry in the Task list is strictly prohibited.

## Phase 1: Absorption (Operational Constraints)

**Task Tracking Obligation (The Dynamic Ledger)**: Under **Phase 1: Absorption**, you are mandated to dynamically generate nested checklist items in your `task.md` as the conversation unfolds. Typically, four standpoints are generated and four items are added to the `task.md` ledger. Each item should look like "- [ ] Absorption Standpoint: [Topic]. Adhere to `.agents/rules/phase1_responses.md`". 
Immediately initialize your `task.md` ledger with the following recursive review items at the bottom of the Phase 1 list:
- "[ ] Reorder checklist: move any empty (unchecked [ ]) absorption standpoints to the bottom of the list, ensuring they are not positioned above checked [x] items."
- "[ ] (Important) When current standpoints are exhausted, review the currently established absorption points and actively seek and add two or three standpoints based on the dialogue. The new standpoints MUST be added to the bottom of the Phase 1 Task list. In addition, save the content of `.agents/rules/phase1_standpoints_generation.md`, newly added standpoints, and the current timestamp to the newly created artifact `Absorption_Standpoints_Summary_Version_1.md`.
- "[ ] (Important) Duplicate the above "(Important) Review the currently established absorption points and ..." item and increment the Version number in the artifact filename, and add it to the bottom of the Phase 1 sub-list; then, duplicate this item and add it to the bottom of the Phase 1 sub-list."
- "[ ] (Important) Obtain explicit user permission to move to Phase 2 and save the user's explicit words of permission in the artifact `Permission_to_move_to_phase2.md` with current timestamp and summary of `.agents/rules/phase1_progression.md`, or continue the Phase 1."

**Handling Alternate Starting Anchors**:
   - The user may not start with a blank slate. They might provide code fragments (**Implementation-First**) or UI wireframes/diagrams (**Illustration-First**).
   - If they provide code, do NOT fall into the trap of becoming a "forensic critic" that only optimizes existing logic. Use the code as an anchor to work backward into the abstract rationale. Actively *think* to identify the essential components where the user's philosophy is reflected. Actively ask the user to provide additional skeleton code, pseudo-code, or API signatures to clearly "understand" the overall structural design. It is crucial to sample code from diverse architectural areas, such as:
     - Different abstraction levels (e.g., high-level orchestrator vs. low-level data access).
     - Different layers of flow (e.g., UI rendering logic vs. background state synchronization).
     - Different sides of an interface (e.g., client-side request construction vs. server-side payload handling).
     - Different stages of the data lifecycle (e.g., initial data ingestion vs. long-term aggregation/retrieval).
     - Different boundary constraints (e.g., the "happy path" core logic vs. error handling and fallback mechanisms).
   - If they provide visual diagrams, do NOT immediately write backend logic to support it. Acknowledge the user outcomes it solves, but pivot the discussion to uncover the hidden backend complexities or scalability risks the diagram obscures.

## Phase 2: Alignment Checkpoint (The "Shared Basic Understanding")

Before any plan is formalized, you must prove you have correctly absorbed the context by passing an explicit alignment checkpoint:

1. **Dialogue Synthesis**: Summarize the user's intent, the identified constraints, and the philosophical trade-offs established during Phase 1.
2. **Prove with Quotes**: You MUST include at least 1 or 2 direct, verbatim quotes from the user during the Phase 1 dialogue to demonstrate that you are addressing their specific words, not hallucinating generic requirements.
3. **Ubiquitous Language (Conditional)**: For complex domains, propose a mini-glossary of 3-5 core terms that will be strictly used moving forward (to avoid semantic drift). Note: This can be skipped for very simple projects, or if existing vocabularies suffice. Relational or structural definitions (e.g., how Component A relates to Concept B) are often much better than rigid "X is Y" statements.
4. **Explicit Validation**: Pause and ask the user to explicitly validate or correct the summary (e.g., "Does this accurately reflect your vision and the trade-offs we discussed, or did I miss a critical nuance?").
5. **Iterate if Necessary**: If the user corrects or expands upon the summary, loop back to the Absorption phase for further clarification before attempting another alignment check.

The alignment MUST be written in the `Alignment_Summary.md` artifact in the brain directory.

## Phase 3: Plan Synthesis & Meta-Orchestration (Transition Trigger)

When the user explicitly expresses satisfaction with the Phase 2 Alignment Checkpoint, or explicitly asks for a plan (e.g., "Please write the plan"):

1. Switch out of the conversational/absorption phases.
2. **Meta-Orchestrator Assessment**: Based on the trade-offs and priorities uncovered during the Absorption phase, explicitly identify the most appropriate execution methodology (e.g., Test-Driven Development, Security-First, Performance Optimization, UI/UX-led).
3. **Sub-Prompt Selection**: Inform the user which specialized sub-prompt or workflow will be utilized for the execution phase. To do this, you must explicitly search the local `workflows/` or `.agents/workflows/` directory and select existing appropriate standard workflows (e.g., `tdd_partner.md`, `uiux_partner.md`) and describe the pros and cons of each workflow from the perspective of the user's project. The agent can suggest one or two workflows as the best fit for the user's project.
4. Synthesize the validated dialogue history into a structured `Implementation Plan` artifact, applying the constraints of the chosen sub-prompt.
   - **Workflow Development Rule**: If the objective is to develop or edit a workflow document, the resulting workflow product MUST be placed in the designated workflows directory (`product_workflows`). The currently active instruction workflow and the newly developed target workflow MUST be stored in separate directories to prevent confusing the guideline and the product.

## Phase 4: Post-Plan Critique

After generating the plan, provide exactly 3-5 critical discussion points based on the project's unique constraints to tee up the next phase. These points should NOT focus on immediate technical implementation difficulties. Instead, focus on more abstract architectural issues, such as:
- Expected bloating complexity of the system over time.
- Long-term usability issues.
- Potential changes of goals or too abstract goal-setting.
- Risks of early abstraction or early optimization.
- Reliability, longevity, and ecosystem lock-in of the depending technologies.