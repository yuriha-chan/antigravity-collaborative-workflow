import json
import argparse

def main():
    parser = argparse.ArgumentParser(description="Calculate effort and ubiquitous language rates from edited JSONL.")
    parser.add_argument("input_file", help="Path to the user-edited JSONL file containing wpm and factor.")
    parser.add_argument("--ubiquitous-terms", nargs="*", default=["Absorptive Partner", "Dialogue-First", "Plan, Approve, Do", "Alignment Checkpoint"], help="List of ubiquitous terms to track.")
    args = parser.parse_args()

    ubiquitous_terms_lower = [t.lower() for t in args.ubiquitous_terms]
    class EffortScores:
        assistant: float = 0.0
        user: float = 0.0
        ubiquitous: int = 0
        responses: int = 0
        
    scores = EffortScores()

    try:
        with open(args.input_file, 'r', encoding='utf-8') as f:
            for line_idx, line in enumerate(f):
                if not line.strip(): continue
                data = json.loads(line)
                
                role = data.get("role", "")
                tokens = data.get("tokens", 0)
                wpm = data.get("wpm", 0)
                factor = data.get("factor", 1.0)
                text_str = data.get("text", "")
                
                # Calculate effort
                # Effort formula: tokens / wpm * factor
                effort = float(tokens) / float(wpm) * float(factor)
                
                if role == "assistant":
                    scores.assistant += effort
                    scores.responses += 1
                elif role == "user":
                    scores.user += effort
                    
                # Calculate ubiquitous language count
                for term in ubiquitous_terms_lower:
                    scores.ubiquitous += text_str.lower().count(term)
                    
    except Exception as e:
        print(f"Error reading JSONL: {e}")
        print("Make sure you have added 'wpm' and 'factor' keys to each JSON object.")
        return

    print("\n📊 --- Effort Report ---")
    print(f"Assistant Comprehension Effort: {scores.assistant:.2f} units")
    print(f"User Prompting Effort: {scores.user:.2f} units")
    
    occurrence_rate = scores.ubiquitous / max(1, scores.responses)
    print(f"\nUbiquitous Language Occurrence: {scores.ubiquitous} total hits.")
    print(f"Average occurrence per Assistant response: {occurrence_rate:.2f}")

if __name__ == "__main__":
    main()
