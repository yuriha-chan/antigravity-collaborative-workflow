---
description: Logic Visualization (Mermaid.js) execution sub-prompt
---

# Logic Visualization Workflow

This workflow is invoked **only when explicitly requested by the user** (e.g., "visualize this," "draw a diagram," "show me the architecture").

## Operational Constraints

1. **Mermaid.js Exclusive**: You must use Mermaid.js syntax inside standard fenced code blocks (`````mermaid ... `````) for all architectural, behavioral, or state-based visualizations. Do not use ASCII art or attempt other pseudo-graphical formats.
2. **Focus on Tacit Logic**: The goal of a diagram is to expose contradictions or confirm shared understanding, not just to draw boxes. Focus the diagram on visualizing complex decision trees, state transitions, or component interactions where logic might be ambiguous.
3. **Avoid Boilerplate**: Only map the parts of the system relevant to the current discussion. Avoid drawing every single database table or every utility function if they do not contribute to clarifying the immediate ambiguity.
4. **Relational Clarity**: Ensure arrows and relationships are explicitly labeled. A visual representation is most powerful when it clarifies *how* entities interact, not just *that* they exist.
