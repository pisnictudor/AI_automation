def parse_ai_response(ai_text):
    summary = ""
    tone = ""
    priority = ""
    recommended_action = ""

    lines = ai_text.splitlines()

    for line in lines:
        if line.startswith("Summary:"):
            summary = line.replace("Summary:", "").strip()
        elif line.startswith("Tone:"):
            tone = line.replace("Tone:", "").strip()
        elif line.startswith("Priority:"):
            priority = line.replace("Priority:", "").strip()
        elif line.startswith("Recommended Action:"):
            recommended_action = line.replace("Recommended Action:", "").strip()

    return summary, tone, priority, recommended_action