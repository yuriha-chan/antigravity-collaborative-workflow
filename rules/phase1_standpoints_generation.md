---
trigger: manual
---

1. **Absorption Standpoint Generation: Deep Understanding**:
   - Focus on establishing shared "basic understandings" before delving into any details. 
   - What constitutes "understanding"? It means grasping the core problem to solve, the user's underlying motives and interests, the nature of the phenomenon to be modeled or simulated, technical architectures and frameworks and design paradigms and their complexities, analyzing the differences from existing solutions, capturing the user's core philosophical trade-offs, outlining the "anti-goals" (what the project explicitly should *not* be), and uncovering unstated assumptions.
   - Utilize rewording and summarization of the user's ideas to clarify and test whether your understanding matches the user's intent.
   - The standpoints must be diverse in aspects, technical and non-technical. Prioritize diversity over consistency.
2. **Absorption Standpoint Generation: Intellectual Exploration**:
   - Center questioning and suggestions around overall designs and theoretical implications, rather than implementational specifics or goal-oriented discussions.
   - Delay questioning detailed edge cases until the overarching foundational concepts are fully and mutually understood.
   - **Deep Research Integration**: If the domain is entirely novel, heavily ambiguous, or requires competitive analysis, seamlessly propose conducting a rigorous `web_survey` as a natural continuation of the discussion. Creatively synthesize and propose the specific topics or dimensions that need to be surveyed to resolve the ambiguity, rather than abruptly "pausing" the dialogue. **When conducting or proposing a `web_survey`, you must explicitly follow the rigorous standards defined in `workflows/web_survey.md`.**
3. **Absorption Standpoint Generation: Stakeholder and Persona Exploration**:
   - Briefly explore the perspective of expected stakeholders or users to deepen requirements.
   - **Skip this entirely** if the project aims to deliver a purely mathematical or algorithmic solution without human stakeholders.
   - If the project is focused on demographics, personalities, or interests (e.g., a standalone game), explore those aspects rather than traditional business "stakes".
   - Do NOT determine the stakeholder intent yourself. Use conversation to simulate stakeholder thoughts, aiming to reveal the distance between the user's expected image of the stakeholders and stereotypical understandings (e.g., imagining system administrators who love chaos and hate limiting end-user permissions rather than typical locked-down admins).