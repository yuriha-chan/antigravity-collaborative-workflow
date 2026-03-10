# Antigravity Collaborative Workflow: The Absorptive Partner

**A Dialogue-First AI Coding Workflow**

This repository contains a suite of advanced, human-centric workflows designed for Antigravity, fundamentally shifting the AI from an immediate "task executor" to a "collaborative architect."

## Core Philosophy: Think Before You Type

In modern software development, building the wrong thing quickly and efficiently is one of the most sophisticated form of failure.
Today's AI coding agents rush through life too fast. Upon receiving a prompt, they immediately dive into code generation, leading to architectural inconsistencies, bloated codebases, and deviations from requirements. To avoid such failures, we need a wise workflow that fosters healthy communication between AI and humans.

The **Absorptive Partner** philosophy rests on three pillars:
1. **Prioritize Dialogue:** During the “absorption phase,” questions are used to listen, probe, and clarify implicit assumptions, design philosophies, and the anti-goals. Destructive tool invocations or code generation are prohibited. The AI is instructed to speak in an intellectual tone, akin to a university seminar.
2. **Visualizing Tacit Knowledge:** Rather than treating human prompts as literal specifications, the workflow positions them as a starting point. It leverages structured dialogue flows to uncover hidden complexities users haven't explicitly stated.
3. **Ensuring Rigorous Consistency:** The AI transcribes agreed-upon points from discussions. The AI is required to obtain user's approval of this document before planning of implementation. This document, alignment summary, includes quotations from the conversation and defines a “Universal Language” (shared terminology), embedding “statistically rare” innovative ideas as reliable reference points.

## Feature Synopsis

The system is organized into a core "Meta-Orchestrator" and several highly specialized execution sub-prompts, located in `.agents/workflows/`.

*   **`absorptive_partner.md`**: The central orchestrator. It manages the infinite absorption loop, the Alignment Checkpoint (Phase 2), and Synthesis (Phase 3). Once aligned, it assesses the project's priorities and routes execution to a specialist sub-prompt.

**Execution Sub-Prompts (Specialists):**
*   **`tdd_partner.md`**: Enforces strict Red-Green-Refactor cycles. It explicitly refuses to write implementation code until it sees a verifiable test failure in the terminal output.
*   **`secops_partner.md`**: Injects Zero-Trust principles. It mandates threat modeling before execution, focuses on least privilege, and actively mitigates OWASP Top 10 vulnerabilities (including LLM-specific Prompt Injections).
*   **`mvp_partner.md`**: Optimizes for speed-to-market. It imposes ruthless prioritization, establishing strict numerical boundaries on features (3-5 core tasks max) and heavily leverages managed services.
*   **`uiux_partner.md`**: Prioritizes sensory and aesthetic excellence, enforcing visual-first implementation, responsive layouts, and universal accessibility (a11y) from the first line of code.
*   **`gradual_restructuring.md`**: Handles deep legacy code and extreme technical debt by teaching the AI to build defensive 'Anti-Corruption Layers' rather than attempting impossible global rewrites.
*   **`visualize_logic.md`**: A focused tool to force the visual mapping of ambiguous logic via `Mermaid.js`.

**Research Methodologies:**
**`web_survey.md`**: A rigorous, formalized “plan, approve, execute” workflow for conducting targeted web surveys. Outputs Survey Strategy as artifacts, executes searches only after user approval. Automates sophisticated, broad surveys using proxy search terms to prevent low-quality results from web information pollution. Furthermore, search quality reports are provided, enabling further iteration on the survey strategy.

## How to use
1. Place the `workflow/` and `rules/` directories into the `.agents/` directory in the workspace.
2. If any, place the existing ideas (notes, excerpts from chat conversations, conceptual codes or documents, etc.) in the workspace directory.
3. Start the `absorptive_partner.md` workflow. You can start the workflow by saying `/absorptive_partner I want to create an application for [purpose]. Look into the conversation log @log.txt` for example. (If your Antigravity fails to recognize the workflow document, @[.agents/workflows/absorptive_partner.md] works.)

## Notes
The Claude models tend to obey the "do not hurry" instructions in the workflow documents very well. If you get tired to have a long discussion, you are responsible to move on to other topics by refering the Task list. The tricky instruction of duplicating standpoint generation task is intended to offer infinite design discussion in Phase 1, but the task list may get confused. If so, please tidy out.

When you use Gemini models, the conversation pace will be more hurried in Phase 1. You can instruct the agent to add more standpoints using `@phase1_standpoints_generation.md` to continue the discussion.
