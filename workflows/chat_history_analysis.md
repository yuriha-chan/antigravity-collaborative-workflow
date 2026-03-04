---
description: Conversation history evaluation and quantification workflow
---

# Chat History Analysis Workflow

This workflow is invoked to evaluate and quantify the user's effort, the agent's performance, and the overall outcomes of a conversation history. It is particularly useful for measuring the effectiveness of the "Absorptive Partner" dialogue-first approach.

## Operational Constraints

When instructed to analyze the chat history, the agent must perform a structured evaluation across specific quantitative and qualitative dimensions. Look through the conversation logs and synthesize a final evaluation report.

### 1. User Behavior Metrics
Quantify the actions and inputs provided by the user during the dialogue:

- **Prompting Effort and Comprehension Effort:** Both are calculated through structured text comprehension and writing difficulty assignments. 
  1. Convert the MD file to JSONL by executing the `chat_to_jsonl.py` script. *(Note: If `python` opens the Windows Store or fails, ensure you run this inside your MSYS2 terminal or use the full path to your Python executable).*
  2. Manually edit the resulting JSONL file to explicitly assign `wpm` and `factor` keys for each role block following the guidelines below. You are prohibited to run Python script to calculate the `wpm` and `factor`. You must analyze the file and determine these values by yourself based on the following guidelines. 
    2.1. For `role: assistant`, manually edit the resulting JSONL file to assign a **reading WPM** key (`wpm`) representing text comprehension difficulty. Include examples:
     - "I have successfully updated the workflow." -> 300 WPM
     - "The Context Mapping strategy isolates bounded contexts to prevent leakage." -> 150 WPM
     - "Ensure the execution script initializes dependency graph sorting correctly before resolving module graphs." -> 100 WPM
    2.2. For `role: assistant`, assign a **correction factor** (`factor`) for information density (increase if topics change frequently or if the context is extremely dense). Include examples:
     - "I fixed a typo in the README." -> Factor 1.0
     - "We'll apply TDD for testing, use OWASP guidelines for security, and then deploy." -> Factor 1.5
     - "Phase 1 requires defining a ubiquitous language mapping conceptual subdomains to code, followed by a strangler fig refactoring while ensuring no API disruption across the CI/CD pipeline." -> Factor 2.5
    2.3. For `role: user`, assign a **writing WPM** (`wpm`) representing text writing difficulty, noting that writing wpm is significantly lower than reading wpm. Include examples:
     - "OK, go ahead." -> 40 WPM
     - "Use a Mermaid chart to show the architecture." -> 25 WPM
     - "The logic fails because the dependency injection container is not registering scoped services per request." -> 15 WPM
    2.4. For `role: user`, assign a **correction factor** (`factor`) for writing. Include examples:
     - "Continue." -> Factor 1.0
     - "Modify section 2 and replace the constraints with strict boundaries." -> Factor 1.3
     - "The problem isn't the configuration but the way the agent parses output data. We must enforce negative prompts and update the strategy dimension before proceeding." -> Factor 2.0
  3. Execute the `calculate_effort.py` script similarly to calculate `tokens / wpm * factor` for each role line and sum the results. The sum for `role: assistant` represents the **comprehension effort**, and the sum for `role: user` represents the **prompting effort**.



- **Instruction Density:** How many times did the user have to explicitly correct the agent?

- **Context Loading:** How many times did the user manually provide files, diagrams, or external links to clarify the context?

### 2. Dialogue Quality & Agent Performance
Quantify the agent's behaviors and responses during the dialogue:
- **Tacit Knowledge Extraction:** Count the number of unstated assumptions, anti-goals, or philosophical trade-offs explicitly identified by the agent during the dialogue.
- **Alignment Checkpoint Iterations:** Count the number of times the Alignment Checkpoint summary was revised or corrected by the user.
- **Ubiquitous Language Usage:** Count the number of defined Ubiquitous Language tokens used, append them to the JSONL, and then calculate the occurrence rate using the `calculate_effort.py` script.

### 3. Structural Output Metrics
Quantify the structural outputs produced during the planning phase:
- **Architectural Decisions:** The numerical count of formalized architectural constraints or boundary decisions established before execution.
- **Scope Definition:** The numerical count of features or components explicitly deferred or bounded out of scope.
- **Simulation Coverage:** If evaluating a role-playing simulation, list the distinct hidden constraints initially held by the user and count how many were explicitly addressed in the final Implementation Plan.

### Execution Output
Output the analysis as a formatted markdown report, presenting the quantified values of the user and agent behaviors comprehensively, without evaluating them as intrinsically positive or negative.