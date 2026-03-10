# Antigravity: The Absorptive Partner

**A Dialogue-First AI Coding Workflow**

This repository contains a suite of advanced, human-centric workflows designed for Antigravity, fundamentally shifting the AI from an immediate "task executor" to a "collaborative architect."

## Core Philosophy: Think Before You Type

The most expensive mistake in software engineering is rapidly and efficiently building the *wrong thing*. Default AI coding agents often rush to code generation the moment they receive a prompt, leading to misaligned architectures, bloated codebases, and missed requirements. 

The **Absorptive Partner** philosophy is built on three pillars:
1. **Dialogue First:** The AI acts as a peer in a university seminar. It uses the "Absorption Phase" to listen, probe, and ask clarifying questions about unstated assumptions and anti-goals, strictly forbidding any destructive tool calls or code generation.
2. **Exposing Tacit Knowledge:** Instead of treating human prompts as literal specifications, the workflow treats them as starting anchors. It leverages spatial mapping (Mermaid diagrams) and structural dialog to reveal the hidden complexities the user hasn't explicitly stated.
3. **Rigorous Alignment:** Before writing a single line of implementation code, the AI must *prove* it understands the user by quoting them directly, establishing a "Ubiquitous Language" (a shared glossary), and demanding explicit user sign-off on a formal Implementation Plan.

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
*   **`web_survey.md`**: A rigorous, formalized "Plan, Approve, Do" workflow for conducting targeted web research. It prevents aimless AI browsing by enforcing Survey Strategy artifacts, strict user sign-offs, and explicit Search Quality Reports.

## How to use
1. Place the `workflow/` and `rules/` directories into the `.agents/` directory in the workspace.
2. If any, place the existing ideas (notes, excerpts from chat conversations, conceptual codes or documents, etc.) in the workspace directory.
3. Start the `absorptive_partner.md` workflow. You can start the workflow by saying `/absorptive_partner I want to create an application for [purpose]. Look into the conversation log @log.txt` for example. (If your Antigravity fails to recognize the workflow document, @[.agents/workflows/absorptive_partner.md] works.)

## Notes
The Claude models tend to obey the "do not hurry" instructions in the workflow documents very well. If you get tired to have a long discussion, you are responsible to move on to other topics by refering the Task list. The tricky standpoint generation Task duplication instruction is intended to offer infinite design discussion in Phase 1, but the task list may get confused. If so, please tidy out.

When you use Gemini models, the conversation pace will be more hurried in Phase 1. You can instruct the agent to add more standpoints using `@phase1_standpoints_generation.md` to continue the discussion.
