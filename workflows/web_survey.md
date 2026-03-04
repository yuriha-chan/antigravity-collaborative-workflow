---
description: Web Survey execution sub-prompt
---

# Web Survey Methodology: Plan, Approve, Do

This document formalizes the rigorous procedure and search strategies used to conduct targeted web research for agentic workflows. By following a strict "Plan, Approve, Do" lifecycle, the research ensures high precision, relevance, and alignment with the user's goals before any execution cycles are spent.

---

## Phase 1: Plan (The Survey Strategy)
Before executing any searches, a formal **Survey Strategy** artifact must be drafted. This prevents aimless browsing and focuses the agent's inference on specific analytical dimensions.

**Strategic Components:**
1.  **Survey Objectives (Topics for Analysis):** Explicitly list the concepts, frameworks, archetypes, tools, or general topics being investigated (e.g., "Copilot Chat," "SWE-agent," "Cursor IDE", or abstract concepts like "meta-level workflow handling").
2.  **Dimensions of Analysis:** Define exactly *what* aspects of those topics are being evaluated. (e.g., "How do they prevent premature code generation?" or "How is the transition from 'Dialogue' to 'Execution' handled?"). Additionally, the dimensions must never be strictly predetermined; they must always include a heuristic discovery dimension to capture unforeseen insights (e.g., "Summary of found missing points of the discussion").
3.  **Execution Method & Query Design:** Formulate explicit, high-recall/high-precision search queries. This is the most critical step for open-source research. Depending on the query, you can employ advanced search techniques:
    *   **Negative Prompt Formulation:** Use exclusionary terms to filter out low-value noise. Avoid naive exclusions like `-tutorial` (since tutorials from official libraries are highly valuable). Instead, employ proxy phrases that pinpoint unwanted low-value content (e.g., `-coursework`, `-assignment`, or specific phrases commonly found in SEO spam).
    *   **Colocational Technical Terms & High-Quality Domain Filters (Optional Strategy):** Especially when many SEO or attention-seeking articles are expected to pollute search results, use metadata constraints (e.g., `site:arxiv.org`, `site:acm.org`, `site:infoq.com`) to limit results to reliable authors. Combine this with authoritative technical proxy terms (e.g., `"empirical review"`, `"case study"`, `"practitioner report"`) to ensure the results come from experienced engineering or academic backgrounds.
    *   **Proxy Search Strategy:** If direct literature is likely scarce due to specific obstacles, use broader **proxy concepts** for your search queries. Use proxies for:
        *   **Anachronisms** (e.g., proxying "AI" to "human facilitator").
        *   **Hyper-specificity** (e.g., proxying highly niche app names to broad category labels).
        *   **Proprietary constraints** (e.g., proxying internal tools to general industry equivalents).
        *   **Nascent fields** (e.g., proxying very recent tech to established adjacent tech).
    *   **Depth & Conflict:** Actively survey for *intra-framework debates* (internal frictions, controversies, and differing opinions and objectives within a single philosophy, an area of study, or a group of people). **Employ multiple queries for searching on a single topic instead of a single broad query.**
    *   **Multi-Step Search Strategies:** Do not always rely on one massive query. For abstract concepts, first execute a foundational search to discover concrete examples (e.g., the name of a famous framework or specific algorithm) connected to the concept. Then, using that specific example in a secondary search **can** produce much better, highly rigorous results than searching for the initial abstract concept itself.

**Example Strategies Used (GitHub/Web Search Formulation):**
To find meta-level workflow handling in open-source AI projects, the following boolean and keyword strategies were employed:
*   *Finding Architecture/Role Definitions:* `(filename:system_prompt.txt OR filename:instructions.md) AND ("plan" AND "execute" AND "gather")`
*   *Finding Dynamic Prompting Frameworks:* `"meta-prompt" OR "meta-orchestrator" OR "workflow manager" AND (agent OR llm) in:readme`
*   *Finding Specific Methodologies:* `"requirement elicitation" AND "llm" AND "agent"`
*   *Finding Behavioral Constraints:* `"prevent premature" AND ("coding" OR "execution") AND agent in:readme`

---

## Phase 2: Approve
Once the Survey Strategy artifact is drafted, the agent must halt and present the plan to the user for explicit approval.

**Why this is necessary:**
*   **Query Calibration:** The user may have domain-specific knowledge that refines the search queries (e.g., instructing the agent to focus on "high-recall/high-precision" open-source meta-workflows).
*   **Scope Adjustment:** Ensures the agent isn't going to spend time researching irrelevant avenues. 
*   **Action:** The agent uses the `notify_user` tool with `BlockedOnUser: true` to request sign-off on the proposed queries and target systems.

---

## Phase 3: Do (Execution & Synthesis)
Only after user approval does the agent execute the planned research.

3.  **Search Quality Report (Initial Evaluation):** After running the targeted queries, evaluate the results by adding a Search Quality Report section to the final document. The report must cover:
    *   **Numerical data added to Quality report:** Include source quality and composition metrics (number of valid sources, percentage of sources by type (e.g. academic, government, blog, etc.)).
    *   **Illustrative Quotes:** Quote specific examples from the search results demonstrating any noise, bias, or insufficiency.
    *   **Potential Biases:** Note if the results lean too heavily toward a specific toolstack, mindset, or one side of the stakeholders.
    *   **Proposed Refinements:** Propose new refined queries if structural gaps are evident.
4.  **Verifiable insights:** Analyze snippets against the "Dimensions of Analysis" and **provide explicit citations for all findings** in your final report, explicitly looking for heuristic discoveries and missing points.
5.  **Synthesize Findings:** Group the raw data into actionable patterns rather than a list of links.
6.  **Actionable Recommendations:** The final section of the output *must* translate the research findings directly into proposed updates for the user's project codebase or prompt instructions.
7.  **User Review (Iterate or Proceed):** Pause and present the complete survey report (containing the Search Quality Report, Synthesis, and Recommendations) to the user. The user will review the report and decide whether to instruct you to execute the refined analysis iteration or accept the current recommendations.

**Example Synthesis Outcomes (from the Absorptive Partner survey):**
*   *Pattern Recognized:* "The Conductor-Expert Pattern" (Separating the task-breaker prompt from the executor prompt).
*   *Actionable Recommendation:* "Explicitly reinforce the 'Requirement Conductor' identity in Phase 1 of our prompt, and introduce stakeholder simulation."
