import json
import argparse

def main():
    parser = argparse.ArgumentParser(description="Convert chat history to JSONL.")
    parser.add_argument("input_file", help="Path to markdown chat history.")
    parser.add_argument("output_file", help="Path to output JSONL file.")
    args = parser.parse_args()

    with open(args.input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    blocks: list[dict] = []
    current_role: str | None = None
    current_text: list[str] = []
    current_edited: list[str] = []

    def save_block():
        if current_role:
            text_str = "\n".join(current_text).strip()
            # Simple token approximation via word count
            tokens = len(text_str.split())
            block = {
                "role": current_role,
                "tokens": tokens,
                "text": text_str,
                "edited_file": current_edited
            }
            blocks.append(block)

    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        if line.startswith("### User Input"):
            save_block()
            current_role = "user"
            current_text = []
            current_edited = []
        elif line.startswith("### Planner Response"):
            save_block()
            current_role = "assistant"
            current_text = []
            current_edited = []
        elif line.startswith(("*Edited", "*Viewed", "*Listed", "*Searched", "*User")):
            val = line.strip('* ')
            if val.startswith("Edited"):
                current_edited.append(val)
        else:
            if current_role:
                current_text.append(line)

    save_block() # Save last block

    with open(args.output_file, 'w', encoding='utf-8') as f:
        for b in blocks:
            f.write(json.dumps(b) + "\n")

    print(f"✅ Successfully converted {args.input_file} to {args.output_file}.")
    print("Please manually edit the JSONL file to add 'wpm' and 'factor' keys to each line before running the calculation script.")

if __name__ == "__main__":
    main()
